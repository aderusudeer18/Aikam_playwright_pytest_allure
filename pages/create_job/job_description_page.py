from playwright.sync_api import expect
import allure

class AIDescriptionPage:
    def __init__(self, page):
        self.page = page

    def write_with_Ai(self,timeout=5000):
        with allure.step("Enter into the Job description page and clicked on write with Ai button"):
            ai_btn = self.page.locator("//button[contains(.,'Write with AI')]")
            expect(ai_btn).to_be_visible(timeout=5000)
            expect(ai_btn).to_be_enabled()
            ai_btn.click()
            allure.attach(
                    "Test case passed successfully:To generate Ai description Clicked on button to generate",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

    def select_Ai_description(self,message,timeout=12000):
        with allure.step("Input has passed to LLM to generate description"):
            prompt =self.page.locator("//textarea[@placeholder='Enter your prompt']")
            prompt.fill(str(message))
            generate_Ai=self.page.locator("//button[contains(text(),'Generate with AI')]")
            generate_Ai.click()
            allure.attach(
                    "Test case passed successfully:Ai generated description for job ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            

            

    def select_next_btn2(self,timeout=18000):
        with allure.step("Job description generated successfully and Clicking on Next button"):
            next_btn2 = self.page.get_by_role("button", name="Next")
            expect(next_btn2).to_be_visible(timeout=5000)
            expect(next_btn2).to_be_enabled()
            next_btn2.click()
            allure.attach(
                    "Test case passed successfully:Ai generated the description & Next button is visible and clicked ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
