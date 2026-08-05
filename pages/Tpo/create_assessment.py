from playwright.sync_api import sync_playwright, expect
import allure 
import pytest 
 
class CreateAssessment:
    def __init__(self,page):
        self.page=page
        
    def test_create_assessment(self,timeout=2000):
        with allure.step("click on create assessment"):
            try:
                create_assessment=self.page.locator("//button[contains(text(),'Create Assessment')]")
                expect(create_assessment).to_be_visible(timeout=timeout)
                create_assessment.click()
                allure.attach(
                        "Test case passed successfully:Create Assessment icon is clicked ",
                        name="Success",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to click Create Assessment icon: {e}")