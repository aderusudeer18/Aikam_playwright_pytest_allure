from playwright.sync_api import sync_playwright 
import pytest 
import allure



class SignUp:
    def __init__(self,page):
        self.page=page

    def open(self):
        self.page.goto("https://aikam-app-qa-793571778940.asia-south1.run.app/")

    def sign_up(self,signup_email,timeout=2000):
        with allure.step("Verifying sign up with valid email"):
            try:
                self.page.locator('//a[contains(text(),"Sign up")]').click()
                sign_up_email=self.page.locator('//input[@name="email"]')
                sign_up_email.fill(signup_email)
                sign_up_btn=self.page.locator('//button[@type="submit"]')
                sign_up_btn.click()
                self.page.reload()
                allure.attach("Test case passed successfully: Sign up submitted", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Sign up failed: {e}")