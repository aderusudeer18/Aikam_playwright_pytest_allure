from playwright.sync_api import sync_playwright ,expect
import pytest
import allure 



class JobsPage:
    def __init__(self, page):
        self.page = page

    def wait_until_jobs_page(self):
        with allure.step("Wait until redirected and Jobs page is ready"):
            try:
                self.page.get_by_text("Jobs Control Center")
                self.page.wait_for_selector('//input[@placeholder="Search Job Title"]', state="visible", timeout=20000)
                allure.attach("Test case passed successfully: Redirected to Jobs page", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to load Jobs page: {e}")

    def verify_job_created(self, job_title_option,job_title):
        with allure.step("Verify created job appears in Jobs list"):
            try:
                job_row = self.page.locator('//input[@placeholder="Search Job Title"]')
                job_row.click()
                job_row.fill(job_title)
                view_job_btn=self.page.locator('//button[contains(text(),"View Job")]').nth(0)
                view_job_btn.click()
                allure.attach(f"Job '{job_title}' verified and clicked successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Job verification failed for '{job_title}': {str(e)}")
