from playwright.sync_api import sync_playwright,expect 
import pytest 
import allure



class ImportResume:
    def __init__(self,page):
        self.page=page
    def test_import_resumes(self,timeout=3000):
        with allure.step("Verify resumes has imported "):
            import_resume=self.page.locator("//span[contains(text(),'Import Resumes')]").click()
            self.page.set_input_files('input[type="file"]', r"C:\Users\Sudeer\Downloads\Aikam_Rakesh_Mekala_Resume.pdf")
            self.page.wait_for_selector("//button[contains(text(),'Import')]").click()
            
            applicant_name=self.page.locator("text=Rakesh Mekala")
            expect(applicant_name).to_be_visible(timeout=70000)
            self.page.reload()
          