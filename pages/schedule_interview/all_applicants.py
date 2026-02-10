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
            try:
                self.page.on("dialog",lambda dialog:dialog.accept())
                
                # Click Schedule AI Interview button
                schedule_btn = self.page.locator('//button[contains(text(),"Schedule AI Interview")]')
                schedule_btn.wait_for(state="visible", timeout=5000)
                schedule_btn.click()
                
                # Wait for the modal/form to load
                self.page.wait_for_load_state("networkidle")
                self.page.wait_for_timeout(1000)
                
                # Select Video Interview
                video_interview = self.page.locator('//label[contains(text(),"Video Interview")]')
                video_interview.wait_for(state="visible", timeout=5000)
                video_interview.click()
                
                # Select Coding Assessment
                coding_assessment = self.page.locator('//label[contains(text(),"Coding Assessment")]')
                coding_assessment.wait_for(state="visible", timeout=5000)
                coding_assessment.click()
                
                # Click Next buttons (3 times)
                for i in range(3):
                    next_btn = self.page.get_by_role("button", name="Next")
                    next_btn.wait_for(state="visible", timeout=5000)
                    next_btn.click()
                    self.page.wait_for_timeout(500)
                
                # Click Schedule button
                schedule_final_btn = self.page.get_by_role("button", name="Schedule", exact=True)
                schedule_final_btn.wait_for(state="visible", timeout=5000)
                schedule_final_btn.click()
                
                allure.attach(
                        "Test case passed successfully: Interview scheduled",
                        name="Test_Success_Message",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"Failed to schedule interview: {e}")


