from playwright.sync_api import sync_playwright, expect
import allure 
import pytest 


class SendMail:
    def __init__(self,page):
        self.page=page
    
    def test_send_mail(self,timeout=2000):
        with allure.step("click on send mail"):
            try:
                send_mail=self.page.locator("//button[contains(text(),'Send Mail')]")
                expect(send_mail).to_be_visible(timeout=timeout)
                send_mail.click()
                allure.attach(
                        "Test case passed successfully:Send Mail icon is clicked ",
                        name="Success",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to click Send Mail icon: {e}")