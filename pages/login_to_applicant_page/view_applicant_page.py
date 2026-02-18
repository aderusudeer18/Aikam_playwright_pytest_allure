from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 


class ViewJob:
    def __init__(self,page):
        self.page=page 
    
    def view_job(self, timeout=10000):
        with allure.step("Click 'View Applicants'"):
            import re
            
            # Refactored: Semantic 'View Applicants' locator
            # It's typically a button or a p/span inside a clickable container
            btn = self.page.get_by_role("button", name=re.compile(r"View Applicants", re.I))
            if btn.count() == 0:
                btn = self.page.get_by_text("View Applicants", exact=False).first
            
            try:
                btn.wait_for(state="visible", timeout=timeout)
                btn.click()
                allure.attach("Clicked 'View Applicants' successfully", name="Success")
            except Exception as e:
                # Force click fallback
                btn.click(force=True)
                allure.attach(f"Clicked 'View Applicants' with force. Error was: {e}", name="Success (Force)")
           
            
            