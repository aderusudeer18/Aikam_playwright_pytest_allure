from playwright.sync_api import sync_playwright ,expect
import allure
import pytest 

class SendMail:
    def __init__(self,page):
          self.page=page


    def test_select_applicant(self,applicant_name):
        with allure.step(f"Select applicant for send mail: {applicant_name}"):
            try:
                container = self.page.locator("button", has_text=applicant_name).first
                expect(container).to_be_visible(timeout=15000)
                checkbox = container.get_by_role("checkbox").first
                expect(checkbox).to_be_visible(timeout=5000)
                checkbox.click()
                allure.attach(f"Test case passed successfully: Applicant {applicant_name} selected for email", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to select applicant {applicant_name} for email: {e}")
                    
    def test_send_mail(self,timeout=3000):
        with allure.step("verify send icon to send mail to applicant"):
            try:
                self.page.on("dialog",lambda dialog:dialog.accept())
                send_mail = self.page.locator('button:has(svg.lucide-mail)').first
                send_mail.click()
                
                # Handle "Email Not Integrated" modal if it appears
                continue_btn = self.page.locator('//*[contains(text(),"Continue with aikam email")]').first
                if continue_btn.count() > 0:
                    try:
                        continue_btn.wait_for(state="visible", timeout=3000)
                        continue_btn.click()
                    except Exception:
                        pass
            
                email_btn = self.page.locator("//button[contains(text(),'Send Email')]")
                email_btn.wait_for(state="visible",timeout=5000)
                email_btn.click()
                
                # Wait for the email modal to close and the page to settle
                email_btn.wait_for(state="hidden", timeout=15000)
                self.page.wait_for_timeout(5000)
                
                allure.attach(
                        "Test case passed successfully:All the check boxs has checked",
                        name="Test_Success_Message",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to send email: {e}")