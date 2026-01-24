from playwright.sync_api import sync_playwright ,expect
import pytest 
import allure 

class Dashboard:

    def __init__(self,page):
        self.page=page

        
    def job_icon(self,timeout=2000):
        with allure.step("click on jobs icon"):
            icon=self.page.locator("svg.lucide-briefcase-business")
            icon.click(force=True)
            allure.attach(
                    "Test case passed successfully:Jobs icon is clicked ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)


    
    


    

