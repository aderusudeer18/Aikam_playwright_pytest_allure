from playwright.sync_api import expect
import allure
import pytest
import re

class ShareApplicant:
    def __init__(self, page):
        self.page = page

    def test_select_applicant(self, applicant_name):
        with allure.step(f"Select applicant for share: {applicant_name}"):
            self.page.wait_for_timeout(3000)
            
            # Using globally successful checkbox selection as reported by user
            checkbox = self.page.locator('input[type="checkbox"]').nth(1)
            
            # Robust fallback to row-specific checkbox
            if checkbox.count() == 0 or not checkbox.is_visible():
                applicant_text = self.page.get_by_text(re.compile(re.escape(applicant_name), re.I)).first
                if applicant_text.count() > 0:
                    row = applicant_text.locator("xpath=ancestor::tr | ancestor::div[role='row'] | ancestor::div[contains(@class,'row')] | ancestor::div[contains(@class,'card')]").first
                    checkbox = row.locator("input[type='checkbox'], [role='checkbox'], span[role='checkbox']").first

            expect(checkbox).to_be_visible(timeout=15000)
            if not checkbox.is_checked():
                checkbox.check(force=True)
            
            if not checkbox.is_checked():
                checkbox.click(force=True)
                
            allure.attach(f"Applicant '{applicant_name}' selected", name="Success")

    def test_share_applicant(self, email="aderu.sudeer@gmail.com", timeout=15000):
        with allure.step(f"Share applicant with: {email}"):
            try:
                self.page.locator("//div[@data-state='closed']").nth(6).click()
                email_input = self.page.get_by_placeholder("Enter email and press Enter")
                email_input.wait_for(state="visible", timeout=3000)
                email_input.fill(email)
                email_input.press("Enter")
                allure.attach(
                            "Test case passed successfully:applicant selected and share details",
                            name="Test_Success_Message",
                            attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to share applicant: {e}")
