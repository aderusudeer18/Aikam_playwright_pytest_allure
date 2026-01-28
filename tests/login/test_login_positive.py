from pages.create_job.login_page import LoginPage
from pages.create_job.dashboard_page import DashboardPage
from pages.create_job.job_key_details import CreateJobPage
from pages.create_job.job_description_page import AIDescriptionPage
from pages.create_job.preview_page import PreviewPage
from pages.create_job.company_details import CompanyDetails
from pages.create_job.jobs_page import JobsPage
from pages.create_job.ai_clarify_ques import AiclarifyQuestions
from pages.create_job.publish_job import PublishBtn
from pages.create_job.view_applicant import ViewJob
from pages.create_job.import_resume import ImportResume
from pages.create_job.schedule_interview import ScheduleInterview
from pages.create_job.send_mail import SendMail
from pages.create_job.share_applicant import ShareApplicant


def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    login.login("liliya.moka@symphonize.com", "Liliya@123") 

    dashboard=DashboardPage(page)
    dashboard.job_icon()
    dashboard.test_create_job()



    job_key_details = CreateJobPage(page)
    job_key_details.select_job_title("python developer")
    job_key_details.select_job_type("Full-time")
    job_key_details.select_worktype("On-site")
    job_key_details.select_location("Hyderabad")
    job_key_details.select_project_team_size("21-50")
    job_key_details.select_work_experience("3","5")
    job_key_details.salary_range("40000", "60000")
    job_key_details.select_target_deadline("21-04-2026")
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
    publish_btn.wait_for_jobs_redirect()

    jobs_list=JobsPage(page)
    jobs_list.wait_until_jobs_page()
    jobs_list.verify_job_created("Python developer") 


    view_btn=ViewJob(page)
    view_btn.view_job()

    resume=ImportResume(page)
    resume.test_import_resumes()

    send_mail=SendMail(page)
    send_mail.test_select_applicant("Rakesh Mekala")
    send_mail.test_send_mail()  

    schedule_interview=ScheduleInterview(page)
    schedule_interview.test_select_applicant("Rakesh Mekala") 
    schedule_interview.test_schedule_interview() 
    
    share_applicant_details=ShareApplicant(page)
    share_applicant_details.test_select_applicant("Rakesh Mekala") 
    share_applicant_details.test_share_applicant()



    



  