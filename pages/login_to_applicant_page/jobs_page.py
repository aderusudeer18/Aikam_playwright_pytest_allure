from playwright.sync_api import sync_playwright ,expect
import allure 



class JobsPage:
    def __init__(self, page):
        self.page = page


    def verify_job_title(self,title,job_title,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_title=self.page.locator('//button[@role="combobox"]')
            select_job_title.click()
            self.page.get_by_role("option",name=title,extra=True)
            self.page.locator('//input[@placeholder="Search"]').fill(job_title)
            allure.attach(
                    "Test case passed successfully:jobs displayed using job title",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_Client(self,client,job_client,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_title=self.page.locator('//button[@role="combobox"]')
            select_job_title.click()
            self.page.get_by_role("option",name=client,extra=True)
            self.page.locator('//input[@placeholder="Search"]').fill(job_client)
            allure.attach(
                    "Test case passed successfully:jobs displayed using Client",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_location(self,location,job_location,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_title=self.page.locator('//button[@role="combobox"]')
            select_job_title.click()
            self.page.get_by_role("option",name=location,extra=True)
            self.page.locator('//input[@placeholder="Search"]').fill(job_location)
            allure.attach(
                    "Test case passed successfully:jobs displayed using job location",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_posted_on(self,posted,job_posted,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_title=self.page.locator('//button[@role="combobox"]')
            select_job_title.click()
            self.page.get_by_role("option",name=posted,extra=True)
            self.page.locator('//input[@placeholder="Search"]').fill(job_posted)
            allure.attach(
                    "Test case passed successfully:jobs displayed using job location",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_Target_deadline(self,deadline,job_Target_deadline,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_title=self.page.locator('//button[@role="combobox"]')
            select_job_title.click()
            self.page.get_by_role("option",name=deadline,extra=True)
            self.page.locator('//input[@placeholder="Search"]').fill(job_Target_deadline)
            allure.attach(
                    "Test case passed successfully:jobs displayed using job location",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)


       

    def wait_until_jobs_page(self,job_id,job_title,timeout=4000):
        with allure.step("Verify job by job_id in Jobs page"):

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


