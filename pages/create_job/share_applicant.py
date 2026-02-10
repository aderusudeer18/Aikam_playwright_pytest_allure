from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 


class ShareApplicant:
    def __init__(self,page):
        self.page=page 
    
    def test_select_applicant(self,applicant_name):
        with allure.step("verify send mail to applicant"):
            container = self.page.locator("div",has=self.page.get_by_text(applicant_name, exact=True)).first
            expect(container).to_be_visible(timeout=15000)
            checkbox = container.locator("input[type='checkbox']").nth(1)
            expect(checkbox).to_be_visible(timeout=5000)
            checkbox.check(force=True)

    def test_share_applicant(self, email="aderu.sudeer@gmail.com", timeout=3000):
        with allure.step("verify share applicant button is visible to share applicant details"):
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

            
