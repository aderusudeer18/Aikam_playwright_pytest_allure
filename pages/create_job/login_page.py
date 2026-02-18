from playwright.sync_api import playwright, expect
import allure
import re
import pytest

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://persimmon.tekworks.ai/")

    def login_invalid_email(self, email, password):
        with allure.step("Login with invalid email"):
            import re
            self.page.get_by_label(re.compile(r"email", re.I)).fill(email)
            self.page.get_by_label(re.compile(r"password", re.I)).fill(password)
            self.page.get_by_role("button", name=re.compile(r"Login", re.I)).click()
            
            error = self.page.get_by_text("Please enter a valid email address")
            expect(error).to_be_visible(timeout=5000)
            allure.attach("Error message displayed successfully", name="Success")

    def login_invalid_password(self, email, password):
        with allure.step("Login with invalid password"):
            import re
            self.page.get_by_label(re.compile(r"email", re.I)).fill(email)
            self.page.get_by_label(re.compile(r"password", re.I)).fill(password)
            self.page.get_by_role("button", name=re.compile(r"Login", re.I)).click()
            
            error = self.page.get_by_text("Invalid email or password")
            expect(error).to_be_visible(timeout=5000)
            allure.attach("Error message displayed successfully", name="Success")

    def login(self, email, password):
        with allure.step("Login with valid email and password"):
            import re
            # Refactored: Semantic inputs
            email_field = self.page.get_by_label(re.compile(r"email", re.I))
            if email_field.count() == 0:
                email_field = self.page.get_by_placeholder(re.compile(r"email", re.I))
            
            pass_field = self.page.get_by_label(re.compile(r"password", re.I))
            if pass_field.count() == 0:
                pass_field = self.page.get_by_placeholder(re.compile(r"password", re.I))
            
            email_field.fill(email)
            pass_field.fill(password)
            
            login_btn = self.page.get_by_role("button", name=re.compile(r"Login", re.I))
            if login_btn.count() == 0:
                login_btn = self.page.get_by_text("Login", exact=True).first
            
            login_btn.click()
            
            # Wait for login success
            try:
                self.page.wait_for_url(re.compile(r".*/(dashboard|jobs)"), timeout=15000)
                allure.attach("Login successful", name="Success")
            except Exception as e:
                # Check for visible error message
                error_msg = self.page.get_by_text(re.compile(r"Invalid|Error", re.I))
                if error_msg.is_visible():
                    pytest.fail(f"Login failed: {error_msg.inner_text()}")
                raise e
            
    
            
