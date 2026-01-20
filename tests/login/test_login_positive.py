from pages.create_job.login_page import LoginPage
from pages.create_job.dashboard_page import DashboardPage
from pages.create_job.job_key_details import CreateJobPage
from pages.create_job.job_description_page import AIDescriptionPage
from pages.create_job.preview_page import PreviewPage
from pages.create_job.company_details import CompanyDetails
from pages.create_job.ai_clarify_ques import AiclarifyQuestions
from pages.create_job.publish_job import PublishBtn


def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    login.login("himakar.vempati@tekworks.in", "Admin!@3") 

    dashboard=DashboardPage(page)
    dashboard.test_create_job()



    job_key_details = CreateJobPage(page)
    job_key_details.select_job_title("Software Engineer")
    job_key_details.select_job_type("Full-time")
    job_key_details.select_worktype("On-site")
    job_key_details.select_location("Chennai")
    job_key_details.select_project_team_size("1-5")
    job_key_details.select_work_experience(2,5)
    job_key_details.salary_range("40000", "60000")
    job_key_details.select_target_deadline("31-01-2026")
    job_key_details.select_next_btn1()


    job_description=AIDescriptionPage(page)
    job_description.write_with_Ai()
    job_description.select_Ai_description("Job description python and java full stack with any degree and 4 years of experience with postman tool")
    job_description.select_next_btn2()

    
    company_details=CompanyDetails(page)
    company_details.select_next_btn3()

    ai_clarifying_ques=AiclarifyQuestions(page)
    ai_clarifying_ques.select_ai_clarify() 


    preview=PreviewPage(page)
    preview.selecxt_next_btn5() 

    publish_btn=PublishBtn(page)
    publish_btn.select_publish_btn()


  