from playwright.sync_api import expect
import allure


class CompanyDetails:
    def __init__(self,page):
        self.page=page

    def select_next_btn3(self,timeout=5000):
        with allure.step("Clicking on Next button"):
            next_btn3 = self.page.get_by_role("button", name="Next")
            expect(next_btn3).to_be_visible(timeout=5000)
            expect(next_btn3).to_be_enabled()
            next_btn3.click()


