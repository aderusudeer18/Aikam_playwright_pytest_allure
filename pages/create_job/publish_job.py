from playwright.sync_api import sync_playwright,expect  
import allure

class PublishBtn:
    def __init__(self,page):
        self.page=page
    def select_publish_btn(self,timeout=5000):
        with allure.step("After all steps Completed the Publish button is visible and clicked successfully"):
            try:
                publish_btn = self.page.locator('//button[@name="publish"]')
                expect(publish_btn).to_be_visible(timeout=5000)
                expect(publish_btn).to_be_enabled()
                publish_btn.click()
                allure.attach("Publish button clicked successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                raise Exception(f"Failed to click Publish button: {e}")

    def wait_for_jobs_redirect(self):
        with allure.step("Wait until redirected to Jobs page"):
            try:
                self.page.wait_for_url("**/jobs**", timeout=15000)
                allure.attach("Redirected to Jobs page successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                raise Exception(f"Failed to redirect to Jobs page after publishing: {e}")
    
    