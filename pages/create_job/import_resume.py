from playwright.sync_api import sync_playwright, expect
import pytest
import allure
import os
import time
import re

class ImportResume:
    def __init__(self, page):
        self.page = page

    def test_import_resumes(self, applicant_name="Rakesh Mekala", timeout=20000):
        with allure.step("Click 'Import Resumes' and upload file"):
            import_resume=self.page.locator("//span[contains(text(),'Import Resumes')]")
            import_resume.click()
            
            resume_path = os.path.join(os.path.expanduser("~"), "Downloads", "LILIYA_MOKA_Resume.pdf")
            
            try:
                self.page.set_input_files('input[type="file"]', resume_path)
                self.page.wait_for_selector("//button[contains(text(),'Import')]").click()
                applicant_locator=self.page.locator(f"text={applicant_name}")
                expect(applicant_locator).to_be_visible(timeout=70000)
            except Exception as e:
                
                error_toast = self.page.locator("text=Error uploading file") 
                if error_toast.is_visible():
                    pytest.fail(f"Resume Upload Failed: {error_toast.inner_text()}")
                else:
        
                    page_text = self.page.inner_text("body")
                    allure.attach(page_text, name="Page_Text_Debug", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail(f"Resume verification failed. Expected '{applicant_name}' to be visible. Error: {e}")
            
            self.page.reload()
