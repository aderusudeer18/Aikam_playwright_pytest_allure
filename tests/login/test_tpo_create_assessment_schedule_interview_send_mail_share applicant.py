from pages.Tpo.login import LoginPage
from pages.Tpo.dashboard import DashboardPage 
from pages.Tpo.create_assessment import CreateAssessment
from pages.Tpo.import_resumes import ImportResumes
from pages.Tpo.send_mail import SendMail
from pages.Tpo.schedule_interview import ScheduleInterview
from pages.Tpo.share_applicant import ShareApplicant




def test_login_valid_credtionals(page):
    
    login = Logindetails(page)
    login.open()
    login.login("liliya.moka@symphonize.com", "Liliya@123") 
  

    dashboard=Dashboard(page)
    dashboard.job_icon()


    select_job=jobsPage(page)
    select_job.jobs_page("Sym0080 Software Engineer") 


    view_applicant=ViewJob(page)
    view_applicant.view_job() 


    select_applicant= AllApplicant(page)
    select_applicant.all_applicant("gggggg") 
   


    schedule_btn=AllApplicant(page) 
    schedule_btn.test_send_mail()


   






