from playwright.sync_api import sync_playwright ,expect
import allure 



class JobsPage:
    def __init__(self, page):
        self.page = page
        self.jobs_list = page.locator("//table | //div[contains(@class,'job')]")

    def wait_until_jobs_page(self):
        with allure.step("Wait until redirected and Jobs page is ready"):
            self.page.wait_for_url("**/jobs**", timeout=20000)
            self.jobs_list.first.wait_for(state="visible", timeout=20000)

    def verify_job_created(self, job_title):
        with allure.step("Verify created job appears in Jobs list"):
            self.page.reload()
            job_row = self.page.locator("a.text-primary", has_text=job_title).first
            expect(job_row).to_be_visible(timeout=15000)
            job_row.click()
