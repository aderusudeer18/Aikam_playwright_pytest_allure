from pages.share_applicant.login import Logindetails 
from pages.share_applicant.dashboard import Dashboard
from pages.share_applicant.jobs_page import jobsPage 
from pages.share_applicant.view_applicant import ViewJob
from pages.share_applicant.all_applicants import AllApplicant 
import allure 

def test_share_applicant(page):
    login=Logindetails(page)
    login.open()
    login.login("liliya.moka@symphonize.com","Liliya@123")  

    dashboard=Dashboard(page)
    dashboard.job_icon() 

    jobs=jobsPage(page)
    jobs.jobs_page("Sym0080 Software Engineer") 

    view_btn=ViewJob(page)
    view_btn.view_job()

    applicant=AllApplicant(page)
    applicant.all_applicant_page(applicant_name="Mahesh")  

    applicant.share_applicant("aderu.sudeer@gmail.com")



