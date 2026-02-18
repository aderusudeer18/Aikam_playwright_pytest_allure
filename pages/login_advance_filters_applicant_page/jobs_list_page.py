from playwright.sync_api import sync_playwright ,expect
import allure 
import pytest



class JobsPage:
    def __init__(self, page):
        self.page = page


    def _get_filter_trigger(self):
        # Helper to find the main filter combobox
        return self.page.get_by_role("combobox").first

    def _apply_filter(self, choice_text):
        import re
        with allure.step(f"Apply filter: {choice_text}"):
            trigger = self._get_filter_trigger()
            trigger.wait_for(state="visible")
            trigger.click()
            
            option = self.page.get_by_role("option", name=re.compile(choice_text, re.I))
            option.wait_for(state="visible")
            option.click()

    def _search_and_locate_row(self, search_text, job_id):
        with allure.step(f"Search for '{search_text}' and locate row with ID '{job_id}'"):
            search = self.page.get_by_placeholder("Search")
            search.wait_for(state="visible")
            search.fill(search_text)
            
            # Locate row by job ID (usually in a cell)
            row = self.page.locator("tr").filter(has_text=job_id)
            return row

    def verify_job_title(self, title, job_title, job_id, timeout=10000):
        with allure.step("verify filter using Job title"):
            import re
            self._apply_filter(title)
            row = self._search_and_locate_row(job_title, job_id)

            if row.count() == 0:
                pytest.fail(f"Job ID {job_id} not found after searching title {job_title}")

            # Robust menu click
            three_dots = row.get_by_role("button", name=re.compile(r"menu|more|actions", re.I))
            if three_dots.count() == 0:
                three_dots = row.locator("button[aria-haspopup='menu']").first
            
            three_dots.wait_for(state="visible")
            three_dots.click()

            # Robust menu item selection
            # Instead of nth(1), try to find by text like 'Inactive' or 'Edit'
            inactive_item = self.page.get_by_role("menuitem", name=re.compile(r"Inactive", re.I))
            if inactive_item.count() == 0:
                inactive_item = self.page.locator("//div[@role='menuitem']").nth(1)
            
            inactive_item.click()
            
            confirm_btn = self.page.get_by_role("button", name=re.compile(r"Inactive", re.I))
            confirm_btn.wait_for(state="visible")
            confirm_btn.click()

            allure.attach(
                    "Successfully filtered and set job to Inactive",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)

    def verify_job_Client(self, client, job_client, job_id, timeout=10000):
        with allure.step("verify filter using Client"):
            import re
            self._apply_filter(client)
            row = self._search_and_locate_row(job_client, job_id)

            if row.count() == 0:
                pytest.fail(f"Job ID {job_id} not found after searching client {job_client}")

            three_dots = row.get_by_role("button", name=re.compile(r"menu|more|actions", re.I))
            if three_dots.count() == 0:
                three_dots = row.locator("button[aria-haspopup='menu']").first
            
            three_dots.wait_for(state="visible")
            three_dots.click()

            # Instead of nth(1), assume it's "Close" or similar based on original code's context
            close_item = self.page.get_by_role("menuitem", name=re.compile(r"Close", re.I))
            if close_item.count() == 0:
                close_item = self.page.locator("//div[@role='menuitem']").nth(1)
            
            close_item.click()
            
            confirm_close = self.page.get_by_role("button", name=re.compile(r"Close", re.I))
            confirm_close.click()

            allure.attach(
                    "Successfully filtered and closed job",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_location(self, location, job_location, job_id, timeout=10000):
        with allure.step("verify filter using Job location"):
            import re
            self._apply_filter(location)
            row = self._search_and_locate_row(job_location, job_id)

            if row.count() == 0:
                pytest.fail(f"Job ID {job_id} not found after searching location {job_location}")

            three_dots = row.get_by_role("button", name=re.compile(r"menu|more|actions", re.I))
            if three_dots.count() == 0:
                three_dots = row.locator("button[aria-haspopup='menu']").first
            
            three_dots.wait_for(state="visible")
            three_dots.click()

            delete_item = self.page.get_by_role("menuitem", name=re.compile(r"Delete", re.I))
            if delete_item.count() == 0:
                 delete_item = self.page.locator("//div[@role='menuitem']").nth(2)
            
            delete_item.click()
            
            confirm_delete = self.page.get_by_role("button", name=re.compile(r"Delete", re.I))
            confirm_delete.click()
            
            allure.attach(
                    "Successfully filtered and deleted job",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_posted_on(self, posted, job_posted, timeout=10000):
        with allure.step("verify filter using Job posted on"):
            self._apply_filter(posted)
            search = self.page.get_by_placeholder("Search")
            search.wait_for(state="visible")
            search.fill(job_posted)
            
            allure.attach(
                    "Successfully filtered by posted date",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)
            
    def verify_job_Target_deadline(self, deadline, job_Target_deadline, timeout=10000):
        with allure.step("verify filter using Target deadline"):
            self._apply_filter(deadline)
            search = self.page.get_by_placeholder("Search")
            search.wait_for(state="visible")
            search.fill(job_Target_deadline)
            
            allure.attach(
                    "Successfully filtered by target deadline",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)

    def verify_job_id(self, job_id, job_title, timeout=10000):
        with allure.step(f"Verify job by job_id: {job_id}"):
            import re
            search = self.page.get_by_placeholder("Search")
            search.fill(job_id)
            
            # Using semantic locator for the job link
            job_row = self.page.get_by_role("link", name=re.compile(job_title, re.I))
            if job_row.count() == 0:
                 job_row = self.page.locator("a.text-primary", has_text=re.compile(job_title, re.I))
            
            try:
                job_row.first.wait_for(state="visible", timeout=timeout)
                job_row.first.scroll_into_view_if_needed()
                job_row.first.click()
                allure.attach(
                    f"Job '{job_title}' (ID: {job_id}) is visible and clicked",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)
            except Exception:
                raise AssertionError(f"Job not found. Job ID: {job_id}, Job Title: {job_title}")



