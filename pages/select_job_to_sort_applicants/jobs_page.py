from playwright.sync_api import sync_playwright ,expect
import allure 



class JobsPage:
    def __init__(self, page):
        self.page = page
       

    def wait_until_jobs_page(self,job_id,job_title,timeout=4000):
        with allure.step("Verify job by job id in Jobs page"):

            self.page.locator('//input[@placeholder="Search"]').fill(job_id)
            self.page.wait_for_timeout(500)  

            job_row = self.page.locator("a.text-primary", has_text=job_title)

            if job_row.count() > 0:
                job_row.first.scroll_into_view_if_needed()
                job_row.first.click()
                allure.attach(
                    "Test case passed successfully:job is visible and clickable",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Job not found. Job ID: {job_id}, Job Title: {job_title}")



    '''def verify_job_created(self, job_title):
        with allure.step("Verify created job appears in Jobs list"):
            self.page.reload()
            job_row = self.page.locator("a.text-primary", has_text=job_title).first
            expect(job_row).to_be_visible(timeout=15000)
            job_row.click()'''
