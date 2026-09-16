import pytest
import allure
import time
import os

from pages.Tpo.login import LoginPage
from pages.Tpo.dashboard import DashboardPage
from pages.Tpo.import_resumes import ImportResumes
from pages.Tpo.tpo_advanced_actions import TpoAdvancedActions
from pages.Tpo.share_applicant import ShareApplicant

@allure.title("Test TPO Advanced Actions: Filters, Preferences, Search, Import, Sort By, Share, Export")
def test_tpo_advanced_actions(page):
    # 1. Login
    login = LoginPage(page) 
    login.open()
    login.login("soloya9603@inraud.com", "Symphonize8*") 
    
    # 2. Dashboard - click job icon or navigate to job
    dashboard = DashboardPage(page)
    dashboard.test_dashboard_page()
    
    # Click on View Applicants for the first job/assessment available
    with allure.step("Navigate into Assessment"):
        view_applicants_btn = page.locator('button:has-text("View Applicants")').first
        view_applicants_btn.wait_for(state="visible", timeout=20000)
        view_applicants_btn.click()
        page.wait_for_timeout(3000)
        
    # 3. Import Resumes  
    resume = ImportResumes(page)
    
    resume_paths = [
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_MdShahnawaz[3y_2m] - Copy.pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_MdShahnawaz[3y_2m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_M.SameeraBegum.[4y_0m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_LAKSHMIPRASANNAKOLUSU[2y_0m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_JalandharBhoi[3y_11m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_KaavatiRohith[2y_1m].pdf"
    ]
    
    # Names expected to be visible after upload
    applicant_names = ["MD SHAHNAWAZ", "Sameera", "LAKSHMI PRASANNA", "Jalandhar Bhoi", "Kaavati Rohith"]
    resume.test_import_resumes(applicant_names, resume_paths)

    # 4. Advanced Actions
    advanced_actions = TpoAdvancedActions(page)
    
    # Search
    advanced_actions.search_by_name("MD SHAHNAWAZ")
    
    # Preferences
    advanced_actions.preferences()
    
    # Advance Filters
    advanced_actions.advance_filters("Python", "Java")
    
    # Sort By
    advanced_actions.sort_applicant()
    
    # 5. Share Applicant
    share = ShareApplicant(page)
    # Using one of the applicant names we expect to be visible
    share.test_select_applicant("MD SHAHNAWAZ")
    share.test_share_applicant("soloya9603@inraud.com")
    
    # 6. Export to Excel (button should be visible since an applicant is selected)
    advanced_actions.export_to_excel()

