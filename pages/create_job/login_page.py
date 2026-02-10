from playwright.sync_api import playwright, expect
import allure
import re

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://app.aikam.ai/")

    def login_invald_email(self, email, password):
        with allure.step("Login with invalid email"):
            self.page.wait_for_selector('//input[@type="email"]').fill(email)
            self.page.wait_for_selector('//input[@type="password"]').fill(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            error =self.page.get_by_text("Please enter a valid email address")
            try:
                expect(error).to_be_visible(timeout=5000)
                allure.attach("Error message displayed successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                # Screenshot handled by conftest
                raise e
    
    def login_invalid_password(self, email, password):
        with allure.step("Login with invalid invalid password"):
            self.page.wait_for_selector('//input[@type="email"]').fill(email)
            self.page.wait_for_selector('//input[@type="password"]').fill(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            error =self.page.get_by_text("Invalid email or password")
            try:
                expect(error).to_be_visible(timeout=5000)
                allure.attach("Error message displayed successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                # Screenshot handled by conftest
                raise e

    def login(self, email, password):
        with allure.step("Login with valid email and password"):
            self.page.wait_for_selector('//input[@type="email"]').fill(email)
            self.page.wait_for_selector('//input[@type="password"]').fill(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            
            # Wait for login success (Dashboard or Jobs - depends on user role)
            try:
                # Use regex to match either dashboard or jobs
                self.page.wait_for_url(re.compile(r".*/(dashboard|jobs)"), timeout=15000)
            except Exception as e:
                # Screenshot handled by conftest
                
                # Check if an error message is visible to provide a clearer error
                error_msg = self.page.locator("text=Invalid email or password")
                if error_msg.is_visible():
                     raise Exception(f"Login failed: '{error_msg.inner_text()}' message displayed.")
                
                # Otherwise re-raise the timeout
                raise e
            
            allure.attach("Login successful and redirected to Dashboard/Jobs page", name="Success", attachment_type=allure.attachment_type.TEXT)
            
            
