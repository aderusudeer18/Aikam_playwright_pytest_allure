from playwright.sync_api import expect
import allure


class CompanyDetails:
    def __init__(self,page):
        self.page=page

    def select_next_btn3(self,timeout=5000):
        with allure.step("Clicking on Next button"):
            try:
                # Refactored: Find the "Next" button more specifically
                next_btn3 = self.page.get_by_role("button", name="Next")
                if next_btn3.count() > 1:
                    next_btn3 = next_btn3.last
                
                expect(next_btn3).to_be_visible(timeout=5000)
                expect(next_btn3).to_be_enabled()
                next_btn3.click()
                allure.attach("Company Details 'Next' clicked successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                raise Exception(f"Failed to click Next on Company Details page: {e}")


