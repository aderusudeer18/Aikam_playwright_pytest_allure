from playwright.sync_api import expect
import allure
import pytest

class DashboardPage:
    def __init__(self, page):
        self.page = page

    def job_icon(self,timeout=5000):
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

    def test_create_job(self,timeout=5000):
        with allure.step("Clicked on Create job button in the jobs page"):
            try:
                create_job = self.page.locator("//button[contains(text(),'Create Job')]")
                expect(create_job).to_be_visible(timeout=timeout)
                create_job.click()
                allure.attach("Clicked 'Create Job' successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                 pytest.fail(f"Failed to click Create Job button: {e}")
