from playwright.sync_api import sync_playwright,expect 
import pytest 
import allure 

class jobsPage:
    def __init__(self,page):
        self.page=page

    def jobs_page(self, job_name, timeout=15000):
        with allure.step(f"Select job: {job_name}"):
            self.page.wait_for_load_state("networkidle")
            
            # Try to select 'Assessment Title' or 'Job Title' from the combobox if it exists
            combobox = self.page.locator('//button[@role="combobox"]')
            if combobox.count() > 0 and combobox.first.is_visible():
                combobox.first.click()
                # Find the option that contains 'Title'
                option = self.page.get_by_role("option", name="Title", exact=False).first
                if option.is_visible():
                    option.click()
            
            # The search input is now configured for Title
            search_box = self.page.locator('//input[@placeholder="Search"]')
            
            search_box.first.wait_for(state="visible", timeout=timeout)
            search_box.first.click() 
            search_box.first.fill(job_name)
            search_box.first.press("Enter")
            self.page.wait_for_timeout(3000) # Wait for filtering to complete
            
            try:
                # After filtering, click the View Job button
                view_job_btn = self.page.locator('//button[contains(text(),"View Job")]').first
                
                view_job_btn.wait_for(state="visible", timeout=timeout)
                view_job_btn.scroll_into_view_if_needed()
                view_job_btn.click()
                
                # Wait for navigation to complete before returning
                self.page.wait_for_load_state("networkidle")

                allure.attach(
                    "Test case passed successfully:job title is in the list and clicked",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            except Exception:
                raise AssertionError(f"Job '{job_name}' not found or View Job button missing.")

