from playwright.sync_api import sync_playwright, expect
import allure 
import pytest 

class ShareApplicant:
    def __init__(self,page):
        self.page=page
    
    def test_share_applicant(self,timeout=2000):
        with allure.step("click on share applicant"):
            try:
                share_applicant=self.page.locator("//button[contains(text(),'Share Applicant')]")
                expect(share_applicant).to_be_visible(timeout=timeout)
                share_applicant.click()
                allure.attach(
                        "Test case passed successfully:Share Applicant icon is clicked ",
                        name="Success",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to click Share Applicant icon: {e}")