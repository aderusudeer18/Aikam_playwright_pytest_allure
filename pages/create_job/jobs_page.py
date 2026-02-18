from playwright.sync_api import expect
import pytest
import allure
import re

class JobsPage:
    def __init__(self, page):
        self.page = page

    def wait_until_jobs_page(self, timeout=60000):
        with allure.step("Wait until redirected and Jobs page is ready"):
            try:
                # Wait for URL to contain "jobs"
                self.page.wait_for_url(re.compile(r".*/jobs"), timeout=timeout)
                self.page.wait_for_selector("table, [role='grid'], .job-list, .card", timeout=timeout, state="attached")
                
                self.page.wait_for_load_state("networkidle", timeout=timeout)
                allure.attach("Jobs page loaded", name="Success")

            except Exception as e:
                allure.attach(f"Initial wait failed, reloading: {str(e)}", name="Warning")
                self.page.reload()
                self.page.wait_for_load_state("networkidle", timeout=30000)

    def verify_job_created(self, job_title, timeout=30000):
        
        with allure.step("Verify created job appears in Jobs list"):
            try:
                self.page.reload()
                job_row = self.page.locator("a.text-primary", has_text=job_title).first
                expect(job_row).to_be_visible(timeout=15000)
                job_row.click()
                allure.attach(f"Job '{job_title}' verified and clicked successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                
                # Conftest handles screenshot
                pytest.fail(f"Job verification failed for '{job_title}': {str(e)}")
