from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 


class ShareApplicant:
    def __init__(self,page):
        self.page=page 
    
    def test_select_applicant(self,applicant_name):
        with allure.step("verify send mail to applicant"):
            try:
                container = self.page.locator("button", has_text=applicant_name).first
                expect(container).to_be_visible(timeout=15000)
                checkbox = container.get_by_role("checkbox").first
                expect(checkbox).to_be_visible(timeout=5000)
                checkbox.click()
                allure.attach(f"Test case passed successfully: Applicant {applicant_name} selected for sharing", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to select applicant {applicant_name} for sharing: {e}")

    def test_share_applicant(self, email="aderu.sudeer@gmail.com", timeout=3000):
        with allure.step("verify share applicant button is visible to share applicant details"):
            try:
                self.page.locator('button:has(svg.lucide-send)').first.click()
                email_input = self.page.get_by_placeholder("Enter email and press Enter")
                email_input.wait_for(state="visible", timeout=15000)
                email_input.fill(email)
                email_input.press("Enter")
                allure.attach(
                            "Test case passed successfully:applicant selected and share details",
                            name="Test_Success_Message",
                            attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to share applicant: {e}")

            
