from playwright.sync_api import sync_playwright,expect  
import allure

class PublishBtn:
    def __init__(self,page):
        self.page=page
    def select_publish_btn(self,timeout=5000):
        with allure.step("After all steps Completed the Publish button is visible and clicked successfully"):
            publish_btn = self.page.locator('//button[@name="publish"]')
            expect(publish_btn).to_be_visible(timeout=5000)
            expect(publish_btn).to_be_enabled()
            publish_btn.click()

    def wait_for_jobs_redirect(self):
        with allure.step("Wait until redirected to Jobs page"):
            self.page.wait_for_url("**/jobs**", timeout=15000)
    
    