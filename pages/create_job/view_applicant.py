from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 


class ViewJob:
    def __init__(self,page):
        self.page=page 
    
    def view_job(self, timeout=10000):
        with allure.step("Click View Applicants"):
            # Refactored: Use a robust locator for the "View Applicants" button
            # We try role-based first, then text-based
            import re
            btn = self.page.get_by_role("button", name=re.compile("View Applicants", re.I))
            if btn.count() == 0:
                btn = self.page.locator("button:has-text('View Applicants')")
            
            if btn.count() == 0:
                btn = self.page.get_by_text("View Applicants", exact=False).locator("xpath=ancestor::button")

            # Final fallbacks for span/p if not already inside a button
            if btn.count() == 0:
                btn = self.page.locator("p:has-text('View Applicants')").first

            # Wait and click aggressively
            try:
                btn.wait_for(state="visible", timeout=timeout)
                btn.scroll_into_view_if_needed()
                btn.click(timeout=5000)
            except Exception:
                try:
                    btn.click(force=True, timeout=5000)
                except Exception:
                    self.page.evaluate("el => el.click()", btn)
            
            allure.attach(
                "Successfully clicked View Applicants button",
                name="Success",
                attachment_type=allure.attachment_type.TEXT)

                
            