from playwright.sync_api import expect
import allure
import pytest

class DashboardPage:
    def __init__(self, page):
        self.page = page

    def job_icon(self, timeout=15000):
        with allure.step("Click on Jobs icon/link"):
            import re
            
            # 1. Wait for the dashboard to load sufficiently
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(2000) # Give UI a moment to settle animations

            # 2. Define robust candidate locators
            # We use first() on candidates to let Playwright's auto-waiting handle visibility
            candidates = [
                self.page.get_by_role("link", name=re.compile(r"^Jobs$", re.I)),
                self.page.locator("a[href*='/jobs']"),
                self.page.get_by_label(re.compile(r"Jobs", re.I)),
                self.page.locator("svg.lucide-briefcase-business").locator("xpath=.."), # parent of briefcase icon
                self.page.get_by_text("Jobs", exact=True)
            ]
            
            clicked = False
            for loc in candidates:
                try:
                    if loc.count() > 0:
                        # Ensure it's attached and try to click
                        loc.first.scroll_into_view_if_needed()
                        loc.first.click(timeout=3000)
                        clicked = True
                        allure.attach(f"Clicked Jobs icon using locator: {loc}", name="Success")
                        break
                except Exception:
                    continue
            
            if not clicked:
                # Last resort: search for ANY element with text 'Jobs' that is clickable
                try:
                    self.page.get_by_text(re.compile(r"Jobs", re.I)).first.click(timeout=5000)
                    clicked = True
                except:
                    allure.attach(self.page.content(), name="Error_Dashboard_Snapshot", attachment_type=allure.attachment_type.HTML)
                    pytest.fail("Could not find or click the 'Jobs' icon/link after login.")

            self.page.wait_for_load_state("load")

    def test_create_job(self, timeout=10000):
        with allure.step("Click on Create Job button"):
            import re
            
            # Refactored: Semantic Create Job button lookup
            create_btn = self.page.get_by_role("button", name=re.compile(r"Create Job", re.I))
            
            try:
                create_btn.wait_for(state="visible", timeout=timeout)
                create_btn.click()
                allure.attach("'Create Job' button clicked successfully", name="Success")
            except Exception as e:
                # Direct evaluation fallback if standard click fails
                try:
                    self.page.evaluate("el => el.click()", create_btn.first)
                except:
                    pytest.fail(f"Failed to click Create Job button: {e}")
