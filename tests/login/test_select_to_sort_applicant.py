from pages.select_job_to_sort_applicants.login_page import LoginPage
from pages.select_job_to_sort_applicants.dashboard_page import DashboardPage 
from pages.select_job_to_sort_applicants.jobs_page import JobsPage
from pages.select_job_to_sort_applicants.view_applicant_page import ViewJob
from pages.select_job_to_sort_applicants.all_applicant_page import AllApplicant



def test_login_valid_credtionals(page):
    
    login = LoginPage(page)
    login.open()
    login.login("liliya.moka@symphonize.com", "Liliya@123") 

    dashboard=DashboardPage(page)
    dashboard.job_icon()
    

    job_page=JobsPage(page)
    job_page.wait_until_jobs_page("Sym0135","Python Developer") 

    view_btn=ViewJob(page)
    view_btn.view_job() 


    applicant_page=AllApplicant(page)
    applicant_page.search_by_name("Surya Mahathi Korada") 
    applicant_page.all_applicant("Surya Mahathi Korada")
    applicant_page.download_excel_btn()

    applicant_page.all_applicant("Surya Mahathi Korada")
    applicant_page.move_to_applicant_btn("Surya Mahathi Korada")


    applicant_page.sort_applicant()

    '''applicant_page.advance_filters("Flipkart")
    applicant_page.re_set_changes()
    applicant_page.search_by_name_to_delete("KUSHAL AGARWAL")
    applicant_page.aapplicant_to_delete("KUSHAL AGARWAL")'''








    

    



  