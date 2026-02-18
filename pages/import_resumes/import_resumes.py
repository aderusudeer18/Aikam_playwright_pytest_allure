from playwright.sync_api import sync_playwright,expect 
import pytest 
import allure



class ImportResume:
    def __init__(self,page):
        self.page=page
    def test_import_resumes(self,timeout=3000):
        with allure.step("Verify resumes has imported "):
            # Refactored: Use a robust locator for the "Import Resumes" button
            import_resume = self.page.get_by_role("button", name="Import Resumes")
            if not import_resume.is_visible():
                import_resume = self.page.get_by_text("Import Resumes", exact=True).locator("xpath=ancestor::button")
            
            if not import_resume.is_visible():
                 import_resume = self.page.locator("//span[contains(text(),'Import Resumes')]")

            # Use an aggressive click strategy
            try:
                import_resume.click(timeout=5000)
            except Exception:
                try:
                    import_resume.click(force=True, timeout=5000)
                except Exception:
                    self.page.evaluate("el => el.click()", import_resume)
            self.page.set_input_files('input[type="file"]', r"C:\Users\Sudeer\Downloads\Aikam_Rakesh_Mekala_Resume.pdf")
            # Refactored: Standardize the "Import" button click
            import_btn_final = self.page.get_by_role("button", name="Import", exact=True)
            import_btn_final.click()
            
            applicant_name=self.page.locator("text=Rakesh Mekala")
            expect(applicant_name).to_be_visible(timeout=70000)
            self.page.reload()
          