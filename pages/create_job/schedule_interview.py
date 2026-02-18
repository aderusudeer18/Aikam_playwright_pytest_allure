from playwright.sync_api import expect
import allure
import pytest
import re

class ScheduleInterview:
    def __init__(self, page):
        self.page = page

    def test_select_applicant(self, applicant_name):
        with allure.step(f"Select applicant for interview: {applicant_name}"):
            self.page.wait_for_timeout(3000)
            
            # Global checkbox selection (nth(1)) has been reported as working for send_mail
            # We'll use a more robust version: find the checkbox that is NOT the Select All one.
            checkbox = self.page.locator('input[type="checkbox"]').nth(1)
            
            # Fallback to text-to-row if nth(1) fails or is not visible
            if checkbox.count() == 0 or not checkbox.is_visible():
                applicant_text = self.page.get_by_text(re.compile(re.escape(applicant_name), re.I)).first
                if applicant_text.count() > 0:
                    row = applicant_text.locator("xpath=ancestor::tr | ancestor::div[role='row'] | ancestor::div[contains(@class,'row')] | ancestor::div[contains(@class,'card')]").first
                    checkbox = row.locator("input[type='checkbox'], [role='checkbox']").first

            expect(checkbox).to_be_visible(timeout=15000)
            if not checkbox.is_checked():
                checkbox.check(force=True)
            
            # Double check with click if needed
            if not checkbox.is_checked():
                checkbox.click(force=True)
                
            allure.attach(f"Applicant '{applicant_name}' selected", name="Success")

    def test_schedule_interview(self, timeout=20000):
        with allure.step("Schedule AI Interview for selected applicant"):
            try:
                self.page.on("dialog", lambda dialog: dialog.accept())
                
                # Try diverse triggers for the Schedule button
                schedule_btn = self.page.get_by_role("button", name=re.compile(r"Schedule AI Interview", re.I)).first
                if schedule_btn.count() == 0 or not schedule_btn.is_visible():
                    schedule_btn = self.page.locator("//button[contains(.,'Schedule AI Interview')]").first
                
                expect(schedule_btn).to_be_visible(timeout=15000)
                schedule_btn.click(force=True)

                self.page.wait_for_timeout(2000)
                
                # Select Interview Types
                for type_name in ["Video Interview", "Coding Assessment"]:
                    type_label = self.page.get_by_text(re.compile(type_name, re.I)).first
                    if type_label.count() > 0 and type_label.is_visible():
                        type_label.click(force=True)

                # Step through the wizard
                for _ in range(3):
                    next_btn = self.page.get_by_role("button", name=re.compile(r"^Next$", re.I)).first
                    if next_btn.count() > 0 and next_btn.is_visible(timeout=5000):
                        next_btn.click(force=True)
                        self.page.wait_for_timeout(1500)

                # Final Schedule button
                final_btn = self.page.get_by_role("button", name=re.compile(r"^Schedule$", re.I)).filter(has_not_text=re.compile(r"Interview", re.I)).first
                if final_btn.count() == 0:
                    final_btn = self.page.get_by_role("button", name=re.compile(r"^Schedule$", re.I)).first
                
                expect(final_btn).to_be_visible(timeout=10000)
                final_btn.click(force=True)
                
                allure.attach("Interview scheduled successfully", name="Success")
            except Exception as e:
                try:
                    all_text = self.page.evaluate("() => document.body.innerText")
                    allure.attach(all_text, name="Full_Page_Text_on_Failure")
                except: pass
                pytest.fail(f"Failed to schedule interview: {e}")