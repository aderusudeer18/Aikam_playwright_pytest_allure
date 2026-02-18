from playwright.sync_api import expect
import allure

class PreviewPage:
    def __init__(self, page):
        self.page = page
    
    def select_next_btn5(self,timeout=5000):
        with allure.step("Verified the details in the preview page and clicked on the Next button"):
            try:
                # Refactored: Use get_by_role for standard button
                nxt_button = self.page.get_by_role("button", name="Next")
                expect(nxt_button).to_be_visible(timeout=5000)
                expect(nxt_button).to_be_enabled()
                nxt_button.click()
                allure.attach("Preview Page 'Next' clicked successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                raise Exception(f"Failed to click Next on Preview page: {e}")
