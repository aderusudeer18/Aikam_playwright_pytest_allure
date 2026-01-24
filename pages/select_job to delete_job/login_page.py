from playwright.sync_api import playwright, expect
import allure

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://aikam-app-qa-793571778940.asia-south1.run.app/")

    def login_invald_email(self, email, password):
        with allure.step("Login with invalid email"):
            self.page.wait_for_selector('//input[@type="email"]').type(email)
            self.page.wait_for_selector('//input[@type="password"]').type(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            error =self.page.get_by_text("Please enter a valid email address")
            expect(error).to_be_visible(timeout=5000)
    
    def login_invalid_password(self, email, password):
        with allure.step("Login with invalid invalid password"):
            self.page.wait_for_selector('//input[@type="email"]').type(email)
            self.page.wait_for_selector('//input[@type="password"]').type(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            error =self.page.get_by_text("Invalid email or password")
            expect(error).to_be_visible(timeout=5000)

    def login(self, email, password):
        with allure.step("Login with valid email and password"):
            self.page.wait_for_selector('//input[@type="email"]').type(email)
            self.page.wait_for_selector('//input[@type="password"]').type(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            
            
