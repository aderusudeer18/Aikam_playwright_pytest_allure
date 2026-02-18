from playwright.sync_api import sync_playwright, expect 
import allure 
import pytest 

class LoginPage:
    def __init__(self,page):
        self.page=page
    def open(self):
        self.page.goto("https://aikam-app-qa-793571778940.asia-south1.run.app/")



    def login_with_credentials(self, email, password, expect_success=True, timeout=10000):
        with allure.step(f"Login with {email}, expect_success={expect_success}"):
            import re
            
            # Refactored: Semantic inputs
            email_input = self.page.get_by_label(re.compile(r"email", re.I))
            if email_input.count() == 0:
                 email_input = self.page.get_by_placeholder(re.compile(r"email", re.I))
            
            password_input = self.page.get_by_label(re.compile(r"password", re.I))
            if password_input.count() == 0:
                 password_input = self.page.get_by_placeholder(re.compile(r"password", re.I))
            
            login_btn = self.page.get_by_role("button", name=re.compile(r"Login", re.I))
            if login_btn.count() == 0:
                 login_btn = self.page.get_by_text("Login", exact=True).locator("xpath=ancestor::button|.")
            
            # Fill and Click
            # Fill and Click - Explicitly clear to avoid field corruption
            email_input.fill("")
            email_input.fill(email)
            
            password_input.fill("")
            password_input.fill(password)
            login_btn.first.click()
            
            if expect_success:
                # Wait for navigation/dashboard indicator
                try:
                    # Briefcase icon is a common indicator of dashboard loading
                    self.page.wait_for_selector("svg.lucide-briefcase-business", state="visible", timeout=timeout)
                    allure.attach("Login successful - Dashboard loaded", name="Success")
                except Exception as e:
                    # Fallback success check: check URL change
                    if "aikam" in self.page.url and "login" not in self.page.url:
                        allure.attach("Login likely successful based on URL change", name="Success (URL)")
                    else:
                        pytest.fail(f"Login failed or Dashboard timed out: {e}")
            else:
                # Wait for error message semantically
                error_msg = self.page.get_by_text(re.compile(r"Invalid|Error|failed", re.I))
                try:
                    expect(error_msg.first).to_be_visible(timeout=timeout)
                    allure.attach(f"Error caught: {error_msg.first.inner_text()}", name="Expected Error")
                except:
                    pytest.fail("Expected error message not found")
        
    
    