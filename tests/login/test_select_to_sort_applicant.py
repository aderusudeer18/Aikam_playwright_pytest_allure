from pages.select_job_to_sort_applicants.login_page import LoginPage
from pages.select_job_to_sort_applicants.dashboard_page import DashboardPage 
from pages.select_job_to_sort_applicants.jobs_page import JobsPage
from pages.select_job_to_sort_applicants.view_applicant_page import ViewJob
from pages.select_job_to_sort_applicants.all_applicant_page import AllApplicant



def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    #login.verify_forget_password("himakar.vempati@symphonize.com")
    login.login("liliya.moka@symphonize.com", "Aikam@123") 

    dashboard=DashboardPage(page)
    dashboard.job_icon()
    

    job_page=JobsPage(page)
    job_page.wait_until_jobs_page("Sym0071","Python developer") 

    view_btn=ViewJob(page)
    view_btn.view_job() 


    applicant_page=AllApplicant(page)
    applicant_page.search_by_name("SURESH PAGAR") 
    applicant_page.all_applicant_page("SURESH PAGAR")
    applicant_page.download_excel_btn()

    applicant_page.all_applicant_pre_screened("SURESH PAGAR")
    applicant_page.move_to_applicant_pre_screened("SURESH PAGAR")


    applicant_page.search_by_name("Rakesh Mekala")
    applicant_page.all_applicant_shortlisted("Rakesh Mekala")
    applicant_page.move_to_applicant_shortlisted()
    

    applicant_page.search_by_name("RAHUL KUMAR")
    applicant_page.all_applicant_interviewing("RAHUL KUMAR")
    applicant_page.move_to_applicant_interviewing()

    applicant_page.search_by_name("KUSHAL AGARWAL")
    applicant_page.all_applicant_selected("KUSHAL AGARWAL")
    applicant_page.move_to_applicant_selected()
    
    applicant_page.search_by_name("FAKHRUDDIN SHAIK")
    applicant_page.all_applicant_rejected("FAKHRUDDIN SHAIK")
    applicant_page.move_to_applicant_rejected()


    applicant_page.sort_applicant()

    








    

    



  