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
    applicant_page.search_by_name("MOHAMMED IMRAN") 
    applicant_page.all_applicant_page("MOHAMMED IMRAN")
    applicant_page.download_excel_btn()

    applicant_page.all_applicant_pre_screened("MOHAMMED IMRAN")
    applicant_page.move_to_applicant_pre_screened("MOHAMMED IMRAN")


    applicant_page.search_by_name("CHITTAJALLU HEMANTH")
    applicant_page.all_applicant_shortlisted("CHITTAJALLU HEMANTH")
    applicant_page.move_to_applicant_shortlisted()  
    

    applicant_page.search_by_name("MIRTHIPATI DURGALAKSHMI")
    applicant_page.all_applicant_interviewing("MIRTHIPATI DURGALAKSHMI")
    applicant_page.move_to_applicant_interviewing()

    applicant_page.search_by_name("JAGADISH B")
    applicant_page.all_applicant_selected("JAGADISH B")
    applicant_page.move_to_applicant_selected()
    
    applicant_page.search_by_name("KAVYA GIDDALA")
    applicant_page.all_applicant_rejected("KAVYA GIDDALA")
    applicant_page.move_to_applicant_rejected()


    applicant_page.sort_applicant()

    








    

    



  