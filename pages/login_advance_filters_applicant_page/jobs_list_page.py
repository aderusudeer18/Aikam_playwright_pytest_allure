from playwright.sync_api import sync_playwright ,expect
import allure 
import pytest



class JobsPage:
    def __init__(self, page):
        self.page = page


    def verify_job_title(self,title,job_title,job_id,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_title = self.page.locator('//button[@role="combobox"]')
            select_job_title.wait_for(state="visible")
            select_job_title.click()

            option = self.page.get_by_role("option", name=title)
            option.wait_for(state="visible")
            option.click()

            search = self.page.locator('//input[@placeholder="Search"]')
            search.wait_for(state="visible")
            search.fill(job_title)

            row = self.page.locator("tr", has_text=job_id)

            if row.count() == 0:
                pytest.fail(f"Job ID {job_id} not found after searching title {job_title}")

            three_dots = row.locator("//button[@aria-haspopup='menu']")
            three_dots.wait_for(state="visible")
            three_dots.click()

            select_option = self.page.locator("//div[@role='menuitem']").nth(1)
            select_option.click()
            confirn_inactive=self.page.locator('//button[contains(text(),"Inactive")]')
            confirn_inactive.click()

            allure.attach(
                    "Test case passed successfully:jobs displayed using job title",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            


            
    def verify_job_Client(self,client,job_client,job_id,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_client = self.page.locator('//button[@role="combobox"]')
            select_job_client.wait_for(state="visible")
            select_job_client.click()

            option = self.page.get_by_role("option", name=client)
            option.wait_for(state="visible")
            option.click()

            search = self.page.locator('//input[@placeholder="Search"]')
            search.wait_for(state="visible")
            search.fill(job_client)
            row = self.page.locator("tr", has_text=job_id)

            if row.count() == 0:
                pytest.fail(f"Job ID {job_id} not found after searching title {job_client}")

            three_dots = row.locator("//button[@aria-haspopup='menu']")
            three_dots.wait_for(state="visible")
            three_dots.click()

            select_option = self.page.locator("//div[@role='menuitem']").nth(1)
            select_option.click()
            confirm_close=self.page.get_by_role("button", name="Close")
            confirm_close.click()

            allure.attach(
                    "Test case passed successfully:jobs displayed using Client",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_location(self,location,job_location,job_id,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_location = self.page.locator('//button[@role="combobox"]')
            select_job_location.wait_for(state="visible")
            select_job_location.click()

            option = self.page.get_by_role("option", name=location)
            option.wait_for(state="visible")
            option.click()

            search = self.page.locator('//input[@placeholder="Search"]')
            search.wait_for(state="visible")
            search.fill(job_location)

            row = self.page.locator("tr", has_text=job_id)

            if row.count() == 0:
                pytest.fail(f"Job ID {job_id} not found after searching title {job_location}")

            three_dots = row.locator("//button[@aria-haspopup='menu']")
            three_dots.wait_for(state="visible")
            three_dots.click()

            select_option = self.page.locator("//div[@role='menuitem']").nth(2)
            select_option.click()
            confirm_delete=self.page.get_by_role("button",name="Delete")
            confirm_delete.click()
            allure.attach(
                    "Test case passed successfully:jobs displayed using job location",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_posted_on(self,posted,job_posted,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_posted = self.page.locator('//button[@role="combobox"]')
            select_job_posted.wait_for(state="visible")
            select_job_posted.click()

            

            option = self.page.get_by_role("option", name=posted)
            option.wait_for(state="visible")
            option.click()

            search = self.page.locator('//input[@placeholder="Search"]')
            search.wait_for(state="visible")
            search.fill(job_posted)
            allure.attach(
                    "Test case passed successfully:jobs displayed using job location",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_Target_deadline(self,deadline,job_Target_deadline,timeout=2000):
        with allure.step("verify filter using Job title"):
            select_job_client = self.page.locator('//button[@role="combobox"]')
            select_job_client.wait_for(state="visible")
            select_job_client.click()

            

            option = self.page.get_by_role("option", name=deadline)
            option.wait_for(state="visible")
            option.click()

            search = self.page.locator('//input[@placeholder="Search"]')
            search.wait_for(state="visible")
            search.fill(job_Target_deadline)
            allure.attach(
                    "Test case passed successfully:jobs displayed using job location",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)


       

    def verify_job_id(self,job_id,job_title,timeout=4000):
        with allure.step("Verify job by job_id in Jobs page"):

            self.page.locator('//input[@placeholder="Search"]').fill(job_id)
            self.page.locator('//input[@placeholder="Search"]').fill(job_id)
            
            job_row = self.page.locator("a.text-primary", has_text=job_title)
            
            # Wait for search results to update/appear
            try:
                job_row.first.wait_for(state="visible", timeout=timeout)
                job_row.first.scroll_into_view_if_needed()
                job_row.first.click()
                allure.attach(
                    "Test case passed successfully:job is visible and clickable",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            except Exception:
                raise AssertionError(f"Job not found. Job ID: {job_id}, Job Title: {job_title}")



