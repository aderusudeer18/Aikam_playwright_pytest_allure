from playwright.sync_api import sync_playwright ,expect
import allure 



class JobsPage:
    def __init__(self, page):
        self.page = page
       

    def wait_until_jobs_page(self,job_id,job_title,timeout=4000):
        with allure.step("Verify job by job id in Jobs page"):

            self.page.locator('//input[@placeholder="Search"]').fill(job_id)
            self.page.wait_for_timeout(500)  

            # Locate the specific job card containing the Job ID
            job_card = self.page.locator("div", has=self.page.get_by_text(job_id)).first
            
            # Locate the View Job button inside the card
            view_job_btn = job_card.locator('//button[contains(text(),"View Job")]').first

            if view_job_btn.count() > 0:
                view_job_btn.scroll_into_view_if_needed()
                view_job_btn.click()
                allure.attach(
                    "Test case passed successfully: View Job button clicked",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Job not found or View Job button missing. Job ID: {job_id}, Job Title: {job_title}")


    def view_applicant_btn(self,timeout=2000):
        with allure.step("view applicant button is visible and clickable"):
            view_btn=self.page.locator('//button[contains(text(),"View Applicants")]')
            view_btn.wait_for(timeout=timeout)
            expect(view_btn).to_be_visible()
            allure.attach(
                "Test case passed successfully:view applicant button is visible and clickable",
                name="Test_Success_Message",
                attachment_type=allure.attachment_type.TEXT)
    
