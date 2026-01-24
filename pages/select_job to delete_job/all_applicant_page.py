from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 
 

class AllApplicant:
    def __init__(self,page):
        self.page=page 

   
    def all_applicant(self, applicant_name):
        with allure.step(f"Select applicant: {applicant_name}"):

            found = False
            max_pages = 10

            for _ in range(max_pages):

                self.page.wait_for_load_state("networkidle")
                self.page.wait_for_timeout(2000)

                applicant = self.page.get_by_text(applicant_name, exact=True)

                if applicant.count() > 0:
                    applicant.first.scroll_into_view_if_needed()

                    app_box = applicant.first.bounding_box()
                    checkboxes = self.page.locator("input[type='checkbox']")

                    closest_checkbox = None
                    closest_distance = float("inf")

                    for i in range(checkboxes.count()):
                        box = checkboxes.nth(i).bounding_box()
                        if box:
                            distance = abs(box["y"] - app_box["y"])
                            if distance < closest_distance:
                                closest_distance = distance
                                closest_checkbox = checkboxes.nth(i)

                    if closest_checkbox:
                        closest_checkbox.scroll_into_view_if_needed()
                        closest_checkbox.click(force=True)
                        found = True
                        break

                # Handle Next button
                next_btn = self.page.get_by_text("Next")

                if next_btn.count() == 0:
                    break

                if not next_btn.is_enabled():
                    allure.attach(
                        self.page.screenshot(),
                        name="Next_Disabled_Applicant_Not_Found",
                        attachment_type=allure.attachment_type.PNG
                    )
                    assert False, f"Applicant '{applicant_name}' not found and Next is disabled"

                next_btn.scroll_into_view_if_needed()
                next_btn.click()
                self.page.wait_for_load_state("networkidle")

            
                assert False, f"Applicant '{applicant_name}' not found"
    





    def schedule_interview(self):
        with allure.step("verify clicked on schedule interview button to schedule interview"):
            self.page.on("dialog",lambda dialog:dialog.accept())
            self.page.locator('//button[contains(text(),"Schedule AI Interview")]').click()
            self.page.wait_for_selector('//label[contains(text(),"Video Interview")]').click()
            self.page.wait_for_selector('//label[contains(text(),"Coding Assessment")]').click()
            self.page.locator("//button[contains(text(),'Next')]").click()
            self.page.get_by_role("button", name="Next").click()
            self.page.get_by_role("button", name="Next").click()
            self.page.get_by_role("button", name="Schedule", exact=True).click()
            allure.attach(
                    "Test case passed successfully:All the check boxs has",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)


