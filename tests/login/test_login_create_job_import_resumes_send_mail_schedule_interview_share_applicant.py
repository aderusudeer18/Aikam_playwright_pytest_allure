from pages.create_job.sign_up import SignUp
from pages.create_job.login_page import LoginPage
from pages.create_job.dashboard_page import DashboardPage
from pages.create_job.job_key_details import CreateJobPage
from pages.create_job.jobs_page import JobsPage
from pages.create_job.view_applicant import ViewJob
from pages.create_job.import_resume import ImportResume
from pages.create_job.schedule_interview import ScheduleInterview
from pages.create_job.send_mail import SendMail
from pages.create_job.share_applicant import ShareApplicant



def test_login_valid_credtionals(page):
    '''sign_up_user=SignUp(page)
    sign_up_user.open()
    sign_up_user.sign_up("virat@infosys.com")'''
    
    login = LoginPage(page)
    login.open()
    login.login("snigdha.dalavai@symphonize.com", "Symphonize8*") 

    dashboard=DashboardPage(page)
    dashboard.job_icon()
    dashboard.test_create_job()



    job_key_details = CreateJobPage(page)
    # First verify job description using AI, which pre-fills some fields on the next page
    job_key_details.verify_job_description("Job description python and java full stack with any degree and 4 years of experience with postman tool")
    
    # Fill remaining empty fields
    job_key_details.select_job_title("Full stack developer")
    job_key_details.select_job_type("Full-time")
    job_key_details.select_worktype("On-site")
    job_key_details.select_location("Hyderabad")
    job_key_details.select_project_team_size("21-50")
    job_key_details.select_work_experience("4","5")
    job_key_details.salary_range("20000", "30000")
    job_key_details.select_target_deadline("21-09-2026")

    job_key_details.publish_btn()

    jobs_list=JobsPage(page)
    #jobs_list.wait_until_jobs_page()
    jobs_list.verify_job_created("Job Title","Full stack developer") 


    view_btn=ViewJob(page)
    view_btn.view_job()

    resume=ImportResume(page)
    resume.test_import_resumes("A.Balaji")

    send_mail=SendMail(page)
    send_mail.test_select_applicant("A.Balaji")
    send_mail.test_send_mail()  

    schedule_interview=ScheduleInterview(page)
    schedule_interview.test_select_applicant("A.Balaji") 
    schedule_interview.test_schedule_interview() 
    
    share_applicant_details=ShareApplicant(page)
    share_applicant_details.test_select_applicant("A.Balaji") 
    share_applicant_details.test_share_applicant("persimmonqa@gmail.com")
  