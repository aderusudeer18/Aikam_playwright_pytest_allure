from pages.send_mail.login import Logindetails 
from pages.send_mail.job_page import jobsPage 
from pages.send_mail.dashboard import Dashboard 
from pages.send_mail.all_applicant import AllApplicant 
from pages.send_mail.view_applicant import ViewJob
import allure




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


   






