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

    # 3. Schedule Interview
    schedule = ScheduleInterview(page)
    schedule.test_select_applicant("gggggg")
    schedule.test_schedule_interview()

    # 4. Send Mail
    # The applicant "gggggg" is already selected by the previous step, so we just send mail
    send_mail = SendMail(page)
    send_mail.test_send_mail()

    # 5. Share Applicant
    share = ShareApplicant(page)
    share.test_share_applicant()
