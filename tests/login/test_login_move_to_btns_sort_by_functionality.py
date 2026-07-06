from pages.select_job_to_sort_applicants.login_page import LoginPage
from pages.select_job_to_sort_applicants.dashboard_page import DashboardPage 
from pages.select_job_to_sort_applicants.jobs_page import JobsPage
from pages.select_job_to_sort_applicants.view_applicant_page import ViewJob
from pages.select_job_to_sort_applicants.all_applicant_page import AllApplicant



def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    #login.verify_forget_password("himakar.vempati@symphonize.com")
    login.login("liliya.moka@symphonize.com", "Liliya@5") 

    dashboard=DashboardPage(page)
    dashboard.job_icon()
    

    job_page=JobsPage(page)
    job_page.wait_until_jobs_page("Sym0993","Android developer") 
    view_btn=ViewJob(page)
    view_btn.view_job() 


    applicant_page=AllApplicant(page)
    applicant_page.search_by_name("Ratul Gangopadhyay") 
    applicant_page.all_applicant_page("Ratul Gangopadhyay")
    applicant_page.download_excel_btn()

    applicant_page.all_applicant_pre_screened("Ratul Gangopadhyay")
    applicant_page.move_to_applicant_pre_screened("Ratul Gangopadhyay")


    applicant_page.search_by_name("Mariselvam R")
    applicant_page.all_applicant_shortlisted("Mariselvam R")
    applicant_page.move_to_applicant_shortlisted()  
    

    applicant_page.search_by_name("Bala Sri Ram Vankayala")
    applicant_page.all_applicant_interviewing("Bala Sri Ram Vankayala")
    applicant_page.move_to_applicant_interviewing()

    applicant_page.search_by_name("Sarvana Kumar R")
    applicant_page.all_applicant_selected("Sarvana Kumar R")
    applicant_page.move_to_applicant_selected()
    
    applicant_page.search_by_name("Venkata Sai Eluri")
    applicant_page.all_applicant_rejected("Venkata Sai Eluri")
    applicant_page.move_to_applicant_rejected()


    applicant_page.sort_applicant()

    








    

    



  