from playwright.sync_api import expect,sync_playwright 
import allure

class AiclarifyQuestions:
    def __init__(self,page):
        self.page=page 

    def select_ai_clarify(self,timeout=5000):
        with allure.step("Entering AI Clarifying Questions and Clicking on Next button"):
            nxt_btn4=self.page.get_by_role("button", name="Next").nth(-1)
            expect(nxt_btn4).to_be_visible(timeout=5000)
            expect(nxt_btn4).to_be_enabled()
            nxt_btn4.click()
