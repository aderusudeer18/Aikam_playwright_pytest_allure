from pages.schedule_interview.login import LoginPage 
from pages.schedule_interview.jobs_page import jobsPage 
from pages.schedule_interview.dashboard import Dashboard
from pages.schedule_interview.view_job import ViewJob 
from pages.schedule_interview.all_applicants import AllApplicant 
import allure 



def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    login.login("liliya.moka@symphonize.com", "Liliya@123") 
  

    dashboard=Dashboard(page)
    dashboard.job_icon()


    select_job=jobsPage(page)
    select_job.jobs_page("Sym0074 DevOps Engineer") 


    view_applicant=ViewJob(page)
    view_applicant.view_job() 


    select_applicant= AllApplicant(page)
    select_applicant.all_applicant("Kolle Naveen") 
   


    schedule_btn=AllApplicant(page) 
    schedule_btn.schedule_interview()


   






