from playwright.sync_api import sync_playwright, expect 
import allure 
import pytest 

class LoginPage:
    def __init__(self,page):
        self.page=page
    def open(self):
        self.page.goto("https://app.aikam.ai/")



    def login_with_credentials(self, email, password, expect_success=True, timeout=5000):
        with allure.step(f"Login with {email}, expect_success={expect_success}"):
            self.page.wait_for_selector('//input[@type="email"]').fill(email)
            self.page.wait_for_selector('//input[@type="password"]').fill(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            
            if expect_success:
                # Wait for dashboard icon to ensure login is complete/stable
                try:
                    self.page.wait_for_selector("svg.lucide-briefcase-business", state="visible", timeout=timeout)
                    allure.attach(
                        "Login successful and Dashboard is visible",
                        name="Success",
                        attachment_type=allure.attachment_type.TEXT)
                except Exception as e:
                    allure.attach(
                        f"Login failed or Dashboard not loaded: {str(e)}",
                        name="Error",
                        attachment_type=allure.attachment_type.TEXT)
                    raise e
            else:
                # Wait for error message
                # Note: You may need to update the selector below with the actual error text/element ID
                try:
                    error_locator = self.page.locator("//div[contains(text(), 'Invalid') or contains(text(), 'Error') or contains(text(), 'failed')]")
                    expect(error_locator.first).to_be_visible(timeout=timeout)
                    allure.attach(
                        f"Login failed as expected. Error: {error_locator.first.inner_text()}",
                        name="Error Checked",
                        attachment_type=allure.attachment_type.TEXT)
                except Exception as e:
                     allure.attach(
                        f"Expected error message not found: {str(e)}",
                        name="Validation Error",
                        attachment_type=allure.attachment_type.TEXT)
                     raise e
        
    
    