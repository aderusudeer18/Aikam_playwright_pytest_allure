from pages.move_to_applicants.login import Logindetails 
from pages.move_to_applicants.dashboard import Dashboard 
from pages.move_to_applicants.jobs_page import jobsPage 
from pages.move_to_applicants.view_applicant import ViewJob 
from pages.move_to_applicants.all_applicant import AllApplicant 
import allure 


def test_verify_applicant_stage(page):
    login=Logindetails(page)
    login.open()
    login.login("liliya.moka@symphonize.com","Liliya@123") 

    dashboard_page=Dashboard(page)
    dashboard_page.job_icon() 

    job_page=jobsPage(page)
    job_page.jobs_page("Sym0085 Python Developer") 

    view_applicant_page=ViewJob(page)
    view_applicant_page.view_job() 

    all_applicant_page=AllApplicant(page)
    all_applicant_page.all_applicant("KUSHAL AGARWAL") 

    all_applicant_page.move_to_applicant("Pre-Screened") 



    all_applicant_page.check_stage(applicant_name="KUSHAL AGARWAL",stage_name="Pre-Screened")





