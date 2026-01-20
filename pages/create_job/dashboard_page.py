from playwright.sync_api import expect
import allure

class DashboardPage:
    def __init__(self, page):
        self.page = page

    '''def job_icon(self,timeout=2000):
        with allure.step("Login sucessfully & Clicked on jobs Icon"):
            icon=self.page.locator("svg.lucide-briefcase-business")
            expect(icon).to_be_visible(timeout=10000)
            icon.click()'''

    def test_create_job(self,timeout=5000):
        with allure.step("Clicked on Create job button in the jobs page"):
            create_job = self.page.locator("//button[contains(text(),'Create Job')]")
            #expect(create_job).to_be_visible()
            create_job.click()
