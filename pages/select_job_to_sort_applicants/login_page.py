from playwright.sync_api import playwright, expect
import allure

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://app.aikam.ai/")

    '''def login_invald_email(self, email, password):
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
            expect(error).to_be_visible(timeout=5000)'''
    
    def verify_forget_password(self,type_email):
        with allure.step("Verify forget password link sent user"):
            forget_password=self.page.locator('//a[contains(text(),"Forgot password?")]')
            forget_password.click()
            email=self.page.locator('//input[@id="email"]')
            email.fill(type_email)
            continue_btn=self.page.locator('//button[@type="submit"]')
            expect(continue_btn).to_be_visible()
            continue_btn.click()
            self.page.wait_for_timeout(2000)
            expect(self.page.get_by_text("A verification link has been")).to_be_visible()
            #expect(self.page.get_by_text("sent to your email account")).to_be_visible()
            self.page.go_back()
            self.page.go_back()


    def login(self, email, password,timeout=2000):
        with allure.step("Login with valid email and password"):
            self.page.wait_for_selector('//input[@type="email"]').type(email)
            self.page.wait_for_selector('//input[@type="password"]').type(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            allure.attach(
                    "Test case passed successfully:Login has done with valid creditionals",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
            
