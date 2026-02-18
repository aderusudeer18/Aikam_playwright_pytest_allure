from playwright.sync_api import expect
import allure
import pytest
import re

class SendMail:
    def __init__(self, page):
        self.page = page

    def test_select_applicant(self, applicant_name):
        with allure.step(f"Select applicant for send mail: {applicant_name}"):
            select_applicant_check_box = self.page.locator('//input[@type="checkbox"]').nth(1)
            select_applicant_check_box.click(force=True)
                    
    def test_send_mail(self, timeout=15000):
        with allure.step("verify send icon to send mail to applicant"):
            try:
                self.page.on("dialog",lambda dialog:dialog.accept())
                self.page.locator('//div[@data-state="closed"]').nth(5).click()
            
                email_btn = self.page.locator("//button[contains(text(),'Send Email')]")
                email_btn.wait_for(state="visible",timeout=2000)
                email_btn.click()
                
                allure.attach(
                        "Test case passed successfully:All the check boxs has checked",
                        name="Test_Success_Message",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to send email: {e}")