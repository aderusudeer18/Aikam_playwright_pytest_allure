from playwright.sync_api import sync_playwright,expect 
import pytest 
import allure 

class jobsPage:
    def __init__(self,page):
        self.page=page

    def jobs_page(self, job_name,timeout=3000):
        with allure.step(f"Select job: {job_name}"):
            job_row = self.page.get_by_role("row", name=job_name).get_by_role("link")
            if job_row.count() == 0:
                allure.attach(
                    "Test case passed successfully:job title is in the list and clicked",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
                assert False, f"Job '{job_name}' not found on the page"

            if not job_row.first.is_visible() or not job_row.first.is_enabled():
                assert False, f"Job '{job_name}' exists but is disabled or not visible"
            job_row.first.click()





