from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 


class ViewJob:
    def __init__(self,page):
        self.page=page 
    
    def view_job(self,timeout=3000):
        with allure.step("Click View Applicants"):

            btn = self.page.locator("//p[contains(text(),'View Applicants')]")

            if btn.count() > 0 and btn.first.is_visible():
               
                btn.first.click()
                allure.attach(
                    "Test case passed successfully:view applicant button is clicked",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                assert False, "View Applicants button not found or not visible on the page"

                
            