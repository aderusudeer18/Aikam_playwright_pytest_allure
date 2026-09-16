from pages.Tpo.login import LoginPage
from pages.Tpo.dashboard import DashboardPage 
from pages.Tpo.create_assessment import CreateAssessment
from pages.Tpo.import_resumes import ImportResumes
from pages.Tpo.send_mail import SendMail
from pages.Tpo.schedule_interview import ScheduleInterview
from pages.Tpo.share_applicant import ShareApplicant

from pages.Tpo.job_page import jobsPage
from pages.Tpo.view_applicant import ViewJob
from pages.Tpo.all_applicant import AllApplicant

def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    login.login("soloya9603@inraud.com", "Symphonize8*") 
  
    dashboard=DashboardPage(page)
    dashboard.test_dashboard_page()

    # 1. Create Assessment
    assessment = CreateAssessment(page)
    assessment.test_create_assessment()
    assessment.test_step1_select_skill("Python")
    assessment.test_step2_fill_details_and_publish("Python Entry Level Test")

    # 2. Select Job and View Applicants
    select_job=jobsPage(page)
    select_job.jobs_page("Python Entry Level Test") 

    view_applicant=ViewJob(page)
    view_applicant.view_job() 

    # 2.5. Import Resumes
    resume = ImportResumes(page)
    resume_paths = [
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_MdShahnawaz[3y_2m] - Copy.pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_MdShahnawaz[3y_2m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_M.SameeraBegum.[4y_0m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_LAKSHMIPRASANNAKOLUSU[2y_0m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_JalandharBhoi[3y_11m].pdf",
        r"C:\Users\Sudeer\Downloads\CST 2\CST 2\resumes_10\Naukri_KaavatiRohith[2y_1m].pdf"
    ]
    applicant_names = ["MD SHAHNAWAZ", "Sameera", "LAKSHMI PRASANNA", "Jalandhar Bhoi", "Kaavati Rohith"]
    resume.test_import_resumes(applicant_names, resume_paths)

    # 3. Schedule Interview
    schedule = ScheduleInterview(page)
    schedule.test_select_applicant("MD SHAHNAWAZ")
    schedule.test_schedule_interview()

    # 4. Send Mail
    send_mail = SendMail(page)
    send_mail.test_select_applicant("MD SHAHNAWAZ")
    send_mail.test_send_mail()

    # 5. Share Applicant
    share = ShareApplicant(page)
    share.test_select_applicant("MD SHAHNAWAZ")
    share.test_share_applicant()
