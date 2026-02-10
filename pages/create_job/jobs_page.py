from playwright.sync_api import sync_playwright ,expect
import pytest
import allure 



class JobsPage:
    def __init__(self, page):
        self.page = page
       #self.jobs_list = page.locator("//table | //div[contains(@class,'job')]")

    def wait_until_jobs_page(self):
        with allure.step("Wait until redirected and Jobs page is ready"):
            self.jobs_list = self.page.locator("//table | //div[contains(@class,'job')]")
            self.page.wait_for_url("**/jobs**", timeout=20000)
            self.jobs_list.first.wait_for(state="visible", timeout=20000)


    

    def verify_job_created(self, job_title):
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
