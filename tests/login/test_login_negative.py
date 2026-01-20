from pages.create_job.login_page import LoginPage
from pages.create_job.dashboard_page import DashboardPage
from pages.create_job.job_key_details import CreateJobPage
from pages.create_job.job_description_page import AIDescriptionPage
from pages.create_job.preview_page import PreviewPage
from pages.create_job.company_details import CompanyDetails
from pages.create_job.ai_clarify_ques import AiclarifyQuestions
from pages.create_job.publish_job import PublishBtn
from pages.create_job.job_description_page import AIDescriptionPage,expect

def test_login_invald_email(page):
    login = LoginPage(page)
    login.open()
    login.login("himakar", "Admin!@3")
    
   


def test_login_invalid_password(page):
    login = LoginPage(page)
    login.open()
    login.login("himakar.vempati@tekworks.in","Admin!")
    

