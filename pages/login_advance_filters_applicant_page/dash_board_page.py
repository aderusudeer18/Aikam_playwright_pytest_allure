from playwright.sync_api import expect
import allure

class DashboardPage:
    def __init__(self, page):
        self.page = page

    def job_icon(self, timeout=10000):
        with allure.step("Click on Jobs icon"):
            import re
            
            # Refactored: Use a semantic locator for the Jobs icon/link
            # We try role-based first (as a link), then text-based
            icon = self.page.get_by_role("link", name=re.compile(r"Jobs", re.I))
            if icon.count() == 0:
                icon = self.page.get_by_label(re.compile(r"Jobs", re.I))
            
            if icon.count() == 0:
                # Fallback to the SVG if semantic ones fail
                icon = self.page.locator("svg.lucide-briefcase-business")
            
            if icon.count() == 0:
                # Final fallback: look for text "Jobs" anywhere that might be clickable
                icon = self.page.get_by_text("Jobs", exact=False).first

            # Wait and click aggressively
            try:
                icon.wait_for(state="visible", timeout=timeout)
                icon.scroll_into_view_if_needed()
                icon.click(timeout=5000)
            except Exception:
                icon.click(force=True, timeout=5000)
            
            allure.attach(
                    "Successfully clicked Jobs icon",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)
            



   

   
