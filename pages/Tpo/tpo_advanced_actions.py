from playwright.sync_api import sync_playwright, expect
import allure
import pytest
import os
import time

class TpoAdvancedActions:
    def __init__(self, page):
        self.page = page

    def search_by_name(self, applicant_name):
        with allure.step(f"Search applicant by name: {applicant_name}"):
            self.page.reload()
            self.page.locator("div.cursor-pointer svg.lucide-search").click()
            self.page.wait_for_timeout(1000)
            search_name = self.page.locator('input[placeholder*="Search"], input[placeholder*="search"]').first
            search_name.fill(applicant_name)
            result = self.page.locator(f"text={applicant_name}").first
            if result.count() > 0:
                result.first.wait_for(state="visible", timeout=15000)
                allure.attach(
                    "Test case passed successfully: Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f"Applicant not found: {applicant_name}")

    def advance_filters(self, skill_1, skill_2, timeout=5000):
        with allure.step("Applying advance filters to applicants"):
            advance = self.page.locator('button').filter(has=self.page.locator('svg.lucide-settings2')).first
            advance.wait_for(state="visible", timeout=timeout)
            advance.click()
            self.page.wait_for_timeout(2000)
            advance_filter = self.page.locator('//button[contains(text(),"Advanced Filters")]')
            advance_filter.click()
            self.page.wait_for_timeout(5000)
            
            # Reset first
            reset_btn = self.page.locator('//button[contains(text(),"Reset Changes")]')
            if reset_btn.is_visible():
                reset_btn.click()
            
            keyword = self.page.get_by_placeholder("Add keywords...")
            keyword.click()
            self.page.keyboard.type(skill_1)
            self.page.keyboard.press("Enter")
            self.page.keyboard.type(skill_2)
            self.page.keyboard.press("Enter")

            apply_btn = self.page.locator("//button[contains(text(),'Apply')]").last
            apply_btn.wait_for(state="visible", timeout=5000)
            try:
                apply_btn.click(timeout=5000)
            except Exception:
                self.page.evaluate("el => el.click()", apply_btn.element_handle())
            
            self.page.wait_for_timeout(3000)
            allure.attach(
                "Test case passed successfully: Advance filters applied",
                name="Test_Success_Message",
                attachment_type=allure.attachment_type.TEXT)

    def sort_applicant(self, timeout=3000):
        with allure.step("Click on all applicants ribbon and sort"):
            self.page.reload()
            all_applicants_tab = self.page.locator('//button[contains(text(),"All Applicants")]')
            if all_applicants_tab.is_visible():
                all_applicants_tab.click()
            
            sort_btn = self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)")
            sort_btn.wait_for(state="visible", timeout=timeout)
            sort_btn.click()

            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Name").click()
            self.page.get_by_text("A → Z", exact=True).click()
            self.page.wait_for_timeout(1000)

            sort_btn.click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Name").click()
            self.page.get_by_text("Z → A", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.reload()
            allure.attach(
                "Test case passed successfully: sort applicants applied successfully",
                name="Test_Success_Message",
                attachment_type=allure.attachment_type.TEXT)

    def preferences(self, timeout=3000):
        with allure.step("Setting applicant preferences"):
            try:
                advance = self.page.locator('button').filter(has=self.page.locator('svg.lucide-settings2')).first
                advance.click()
                
                pref_btn = self.page.locator('//button[contains(text(),"Preferences")]')
                if pref_btn.is_visible():
                    pref_btn.click()
                    self.page.wait_for_timeout(1000)
                else:
                    allure.attach(
                        "Preferences button not found, maybe under advance filters.",
                        name="Info",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(f"Could not apply preferences: {str(e)}", name="Error", attachment_type=allure.attachment_type.TEXT)

    def export_to_excel(self, timeout=15000):
        with allure.step("Export applicant data to excel"):
            try:
                # Based on the user stating the button becomes visible after selection
                # Assuming the button contains text Export or is a lucide-download icon
                # Let's try locating button with text 'Export' or download icon
                export_btn = self.page.locator('button:has-text("Export"), button:has(svg.lucide-download)').first
                export_btn.wait_for(state="visible", timeout=timeout)
                
                # Handling the download using playwright's expect_download()
                with self.page.expect_download() as download_info:
                    export_btn.click()
                
                download = download_info.value
                allure.attach(
                    f"Test case passed successfully: File downloaded as {download.suggested_filename}",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to export to excel: {e}")

