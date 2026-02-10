from playwright.sync_api import sync_playwright ,expect
import allure 
import pytest 


class ScheduleInterview:
    def __init__(self,page):
        self.page=page 
    
    def test_select_applicant(self,applicant_name):
        with allure.step(f"Select applicant for interview: {applicant_name}"):
            container = self.page.locator("div",has=self.page.get_by_text(applicant_name, exact=True)).first

            expect(container).to_be_visible(timeout=15000)
            checkbox = container.locator("input[type='checkbox']").nth(1)

            expect(checkbox).to_be_visible(timeout=5000)
            checkbox.check(force=True)

            '''self.page.wait_for_selector("tr, div[data-applicant]", timeout=20000)

            # 2️⃣ Locate applicant row safely
            row = self.page.locator(
                "tr, div",
                has=self.page.get_by_text(applicant_name, exact=True)
            ).first

            expect(row).to_be_visible(timeout=15000)

            # 3️⃣ Locate checkbox ONLY inside that row
            checkbox = row.locator("input[type='checkbox']").first

            expect(checkbox).to_be_visible(timeout=5000)

            # 4️⃣ Select checkbox
            checkbox.check(force=True)'''


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
                self.page.get_by_role("button", name="Schedule", exact=True).click()
                allure.attach("Interview scheduled successfully", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to schedule interview: {e}")
            allure.attach(
                    "Test case passed successfully:All the check boxs has selected and check clicked on schedule button",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)