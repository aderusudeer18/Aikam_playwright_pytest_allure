from playwright.sync_api import sync_playwright, expect
import pytest 
import allure 

class DashboardPage: 
    def __init__(self,page):
        self.page=page 
    def test_dashboard_page(self,timeout=2000):
        with allure.step("click on jobs icon"):
            try:
                icon=self.page.locator("svg.lucide-briefcase-business")
                expect(icon).to_be_visible(timeout=timeout)
                icon.click()
                allure.attach(
                        "Test case passed successfully:Jobs icon is clicked ",
                        name="Success",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to click jobs icon: {e}")