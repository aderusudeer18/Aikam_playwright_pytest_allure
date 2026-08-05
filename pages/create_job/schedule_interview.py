from playwright.sync_api import sync_playwright ,expect
import allure 
import pytest 


class ScheduleInterview:
    def __init__(self,page):
        self.page=page 
    
    def test_select_applicant(self,applicant_name):
        with allure.step(f"Select applicant for interview: {applicant_name}"):
            try:
                container = self.page.locator("button", has_text=applicant_name).first
                expect(container).to_be_visible(timeout=15000)
                checkbox = container.get_by_role("checkbox").first
                expect(checkbox).to_be_visible(timeout=5000)
                checkbox.click()
                allure.attach(f"Test case passed successfully: Applicant {applicant_name} selected", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to select applicant {applicant_name}: {e}")



    def test_schedule_interview(self):
        with allure.step("verify to schedule interview to applicant"):
            try:
                self.page.on("dialog",lambda dialog:dialog.accept())
                schedule_ai_interview=self.page.locator('//button[contains(text(),"Schedule AI Interview")]')
                schedule_ai_interview.click()
                self.page.locator('//label[contains(text(),"Video Interview")]').click()
                self.page.locator('//label[contains(text(),"Coding Assessment")]').click()
                self.page.locator("//button[contains(text(),'Next')]").click()
                self.page.get_by_role("button", name="Next").click()
                self.page.get_by_role("button", name="Next").click()
                schedule_btn = self.page.get_by_role("button", name="Schedule", exact=True)
                schedule_btn.click()
                schedule_btn.wait_for(state="hidden", timeout=15000)
                self.page.wait_for_timeout(5000)
                
                allure.attach("Interview scheduled successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to schedule interview: {e}")
            allure.attach(
                    "Test case passed successfully:All the check boxs has selected and check clicked on schedule button",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)