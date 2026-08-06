import pytest
import allure
import time
import os

from pages.Tpo.login import LoginPage
from pages.Tpo.dashboard import DashboardPage
from pages.Tpo.create_assessment import CreateAssessment

# Applicant Action imports from Tpo
from pages.Tpo.import_resumes import ImportResumes
from pages.Tpo.send_mail import SendMail
from pages.Tpo.share_applicant import ShareApplicant
from pages.Tpo.schedule_interview import ScheduleInterview

# Import advance filters page
from pages.login_advance_filters_applicant_page.all_applicant_advance_filters_page import Allapplicant

@allure.title("Test TPO Complete End-to-End Assessment Flow")
def test_tpo_full_flow(page):
    # 1. Login
    login = LoginPage(page)
    login.open()
    login.login("soloya9603@inraud.com", "Symphonize8*") 
    
    # 2. Dashboard
    dashboard = DashboardPage(page)
    dashboard.test_dashboard_page()
    
    # 3. Create Assessment Flow
    create_assessment = CreateAssessment(page)
    create_assessment.test_create_assessment()
    create_assessment.test_step1_select_skill("Python")
    create_assessment.test_step2_fill_details_and_publish("Python Entry Level Test")
    
    # 6. Click on the newly created assessment (it's the first one in the list typically)
    with allure.step("Navigate into Assessment"):
        view_applicants_btn = page.locator('button:has-text("View Applicants")').first
        view_applicants_btn.wait_for(state="visible", timeout=15000)
        view_applicants_btn.click()
        page.wait_for_timeout(3000)
    
    # 7. Import Resumes
    resume = ImportResumes(page)
    # The import_resumes page object looks for this name after upload
    resume.test_import_resumes("A.Balaji") 
    
    # 8. Send Mail
    send_mail = SendMail(page)
    send_mail.test_select_applicant("A.Balaji")
    send_mail.test_send_mail()
    
    # 9. Schedule Interview
    schedule = ScheduleInterview(page)
    schedule.test_select_applicant("A.Balaji")
    schedule.test_schedule_interview()
    
    # 10. Share Applicant
    share_applicant = ShareApplicant(page)
    share_applicant.test_select_applicant("A.Balaji")
    share_applicant.test_share_applicant("soloya9603@inraud.com")
    
    # 11. Apply Filters
    all_applicant = Allapplicant(page)
    all_applicant.advance_filters("Python", "Java", "SQL", "test@test.com", "9876543210", "Hyderabad", "Bangalore")
