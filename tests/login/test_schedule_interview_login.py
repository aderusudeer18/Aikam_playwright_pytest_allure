from pages.schedule_interview.login import LoginPage 
from pages.schedule_interview.jobs_page import jobsPage 
from pages.schedule_interview.view_job import ViewJob 
from pages.schedule_interview.all_applicants import AllApplicant  


def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    login.login("liliya.moka@symphonize.com", "Liliya@123") 


    select_job=jobsPage(page)
    select_job.jobs_page("Tek0034 Software Engineer") 


    view_applicant=ViewJob(page)
    view_applicant.view_job() 


    select_applicant= AllApplicant(page)
    select_applicant.all_applicant() 


    schedule_btn=AllApplicant(page) 
    schedule_btn.schedule_interview()






    



  



