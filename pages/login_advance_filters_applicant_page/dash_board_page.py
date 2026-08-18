from playwright.sync_api import expect
import allure

class DashboardPage:
    def __init__(self, page):
        self.page = page

    def job_icon(self,timeout=2000):
        with allure.step("click on jobs icon"):

            icon_1=self.page.locator("svg.lucide-briefcase-business")
            self.page.wait_for_timeout(3000)
            icon_1.click(force=True)
            
            icon=self.page.locator("svg.lucide-briefcase-business")
            self.page.wait_for_timeout(3000)
            icon.click(force=True)
            
            self.page.wait_for_timeout(3000)
            allure.attach(
                    "Test case passed successfully:Jobs icon is clicked ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            



   

   
