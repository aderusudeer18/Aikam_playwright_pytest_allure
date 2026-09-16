from playwright.sync_api import sync_playwright,expect 
import pytest 
import allure
import os



class ImportResume:
    def __init__(self,page):
        self.page=page
    def test_import_resumes(self, applicant_name, timeout=7000):
        with allure.step("Verify resumes has imported "):
            resume_paths = [
                os.path.join(os.path.expanduser("~"), "Downloads", "Aikam_A.Balaji_Resume.pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_MdShahnawaz[3y_2m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_M.SameeraBegum.[4y_0m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_LAKSHMIPRASANNAKOLUSU[2y_0m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_JalandharBhoi[3y_11m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_KaavatiRohith[2y_1m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_JayaBhargavaKotturu[3y_2m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_MohammadImran[2y_5m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_MdArbaaz[3y_9m].pdf"),
                os.path.join(os.path.expanduser("~"), "Downloads", "CST 2", "CST 2", "resumes_10", "Naukri_MDurgalakshmi[2y_6m].pdf")
            ]
            
            try:
                self.page.wait_for_load_state("networkidle")
                import_resume=self.page.locator("//span[contains(text(),'Import Resumes')]")
                import_resume.wait_for(state="visible", timeout=15000)
                import_resume.click()
                
                # Wait for modal to appear and input to be attached
                self.page.wait_for_selector('input[type="file"]', state="attached", timeout=15000)
                self.page.set_input_files('input[type="file"]', resume_paths)
                self.page.wait_for_selector("//button[contains(text(),'Import')]").click()
                
                # Wait for 2 minutes for processing
                self.page.wait_for_timeout(140000)
                
                # Reload the page to make the applicant visible
                self.page.wait_for_timeout(7000)
                
                applicant_locator=self.page.locator(f"text={applicant_name}")
                expect(applicant_locator).to_be_visible(timeout=90000)
                allure.attach("Test case passed successfully: Resumes are imported and applicant is visible", name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                
                error_toast = self.page.locator("text=Error uploading file") 
                if error_toast.is_visible():
                    pytest.fail(f"Resume Upload Failed: {error_toast.inner_text()}")
                else:
        
                    page_text = self.page.inner_text("body")
                    allure.attach(page_text, name="Page_Text_Debug", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail(f"Resume verification failed. Expected '{applicant_name}' to be visible. Error: {e}") 

            self.page.reload() 

   


