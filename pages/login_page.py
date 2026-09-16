from playwright.sync_api import playwright, expect
import allure
import re

from constants.urls import URLs
from constants.messages import ErrorMessages
from constants.locators import LoginLocators

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(URLs.BASE_URL)

    def login_invald_email(self, email, password):
        with allure.step("Login with invalid email"):
            self.page.locator(LoginLocators.EMAIL_INPUT_TYPE).fill(email)
            self.page.locator(LoginLocators.PASSWORD_INPUT).fill(password)
            self.page.locator(LoginLocators.LOGIN_BTN).click()
            error =self.page.get_by_text(ErrorMessages.INVALID_EMAIL)
            try:
                expect(error).to_be_visible(timeout=5000)
                allure.attach("Error message displayed successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                # Screenshot handled by conftest
                raise e
    
    def login_invalid_password(self, email, password):
        with allure.step("Login with invalid invalid password"):
            self.page.locator(LoginLocators.EMAIL_INPUT_TYPE).fill(email)
            self.page.locator(LoginLocators.PASSWORD_INPUT).fill(password)
            self.page.locator(LoginLocators.LOGIN_BTN).click()
            error =self.page.get_by_text(ErrorMessages.INVALID_CREDENTIALS)
            try:
                expect(error).to_be_visible(timeout=5000)
                allure.attach("Error message displayed successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                # Screenshot handled by conftest
                raise e

    def login(self, email, password):
        with allure.step("Login with valid email and password"):
            self.page.locator(LoginLocators.EMAIL_INPUT_ID).fill(email)
            
            self.page.locator(LoginLocators.PASSWORD_INPUT).fill(password)
            self.page.locator(LoginLocators.LOGIN_BTN).click()
            
            # Wait for login success (Dashboard or Jobs - depends on user role)
            try:
                # Use regex to match either dashboard or jobs
                self.page.wait_for_url(re.compile(r".*/(dashboard|jobs)"), timeout=15000)
            except Exception as e:
                # Screenshot handled by conftest
                
                error_msg = self.page.locator(ErrorMessages.INVALID_CREDENTIALS_LOCATOR_TEXT)
                if error_msg.is_visible():
                     raise Exception(f"Login failed: '{error_msg.inner_text()}' message displayed.")
                
                # Otherwise re-raise the timeout
                raise e
            
            allure.attach("Login successful and redirected to Dashboard/Jobs page", name="Success", attachment_type=allure.attachment_type.TEXT)
            
            
