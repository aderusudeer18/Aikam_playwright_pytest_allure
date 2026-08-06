from playwright.sync_api import sync_playwright,expect 
import pytest 
import allure
import os



class ImportResumes:
    def __init__(self,page):
        self.page=page
    def test_import_resumes(self, applicant_name, timeout=3000):
        with allure.step("Verify resumes has imported "):
            import_resume=self.page.locator("//span[contains(text(),'Import Resumes')]")
            import_resume.click()
            
            resume_path = os.path.join(os.path.expanduser("~"), "Downloads", "Aikam_A.Balaji_Resume.pdf")
            
            try:
                self.page.set_input_files('input[type="file"]', resume_path)
                self.page.wait_for_selector("//button[contains(text(),'Import')]").click()
                
                # Wait for 2 minutes for processing
                self.page.wait_for_timeout(120000)
                
                # Reload the page to make the applicant visible
                self.page.wait_for_timeout(5000)
                
                applicant_locator=self.page.locator(f"text={applicant_name}")
                expect(applicant_locator).to_be_visible(timeout=70000)
                allure.attach("Test case passed successfully: Resume imported and applicant is visible", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                
                error_toast = self.page.locator("text=Error uploading file") 
                if error_toast.is_visible():
                    pytest.fail(f"Resume Upload Failed: {error_toast.inner_text()}")
                else:
        
                    page_text = self.page.inner_text("body")
                    allure.attach(page_text, name="Page_Text_Debug", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail(f"Resume verification failed. Expected '{applicant_name}' to be visible. Error: {e}") 

            self.page.reload() 

   


