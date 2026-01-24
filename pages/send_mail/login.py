from playwright.sync_api import sync_playwright ,expect
import allure 
import pytest 



class Logindetails:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://aikam-app-qa-793571778940.asia-south1.run.app/")

    
    def login(self, email, password,timeout=3000):
        with allure.step(f"Login attempt with email: {email}"):

            # Fill credentials
            self.page.fill('//input[@type="email"]', email)
            self.page.fill('//input[@type="password"]', password)

            # Click Login
            login_btn = self.page.locator('//div[text()="Login"]')
            login_btn.click()
            allure.attach(
            "Test case passed successfully: Entered valid email and password",
            name="Test_Success_Message",
            attachment_type=allure.attachment_type.TEXT)


            # Wait shortly for either success or error message
            self.page.wait_for_timeout(1500)  


            error_msg = self.page.locator("//*[contains(text(),'Invalid email or password')]")

            if error_msg.count() > 0 and error_msg.is_visible():
                # Fail the test with message
                pytest.fail(f"Login failed: Invalid email or password '{email}'")
    
  
    
        
     


    


    

    
  

    
  