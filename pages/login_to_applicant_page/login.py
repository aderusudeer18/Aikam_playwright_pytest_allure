from playwright.sync_api import sync_playwright 
import allure 
import pytest 

class LoginPage:
    def __init__(self,page):
        self.page=page
    def open(self):
        self.page.goto("https://aikam-app-qa-793571778940.asia-south1.run.app/")



    def test_login_email_password(self,email,password,timeout=3000):
        with allure.step(f"verify valid {email},{password}"):
            self.page.wait_for_selector('//input[@type="email"]').type(email)
            self.page.wait_for_selector('//input[@type="password"]').type(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()
            allure.attach(
                    "Test case passed successfully:Login has done with valid creditionals",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
        
    
    