from pages.login_advance_filters_applicant_page.login_page import LoginPage 
from pages.login_advance_filters_applicant_page.dash_board_page import DashboardPage
from pages.login_advance_filters_applicant_page.jobs_list_page import JobsPage 
from pages.login_advance_filters_applicant_page.view_applicant_page_details import ViewJob 
from pages.login_advance_filters_applicant_page.all_applicant_advance_filters_page import Allapplicant 

# login  -> select random job -> if any exists applicant delete all ->import resumes around 20 -> apply advance filters ->if multiple applicants found select particular applicant then open -> first send mail -> schedule ai prescreening->and schedule Ai interview -> ai code assessment->ai code assessment ->click on resume to download ->then schedule manual interview -> download applicant card->share applicant ->provide feedback ->check reviewr back is saved

def test_login_to_applicant_page(page):
    login = LoginPage(page)
    login.open()
    login.login_with_credentials("liliya.moka@symphonize.com", "Aikam@123") 

    dashboard=DashboardPage(page)
    dashboard.job_icon()

    jobs_page=JobsPage(page)
    '''jobs_page.verify_job_title("Job Title","Python developer","Sym0071")
    jobs_page.verify_job_Client("Client","symphonize","Sym0754")
    jobs_page.verify_job_location("Location","vijayawada","Sym0755")
    jobs_page.verify_job_posted_on("Posted on","09 jan 2026")
    jobs_page.verify_job_Target_deadline("Target Deadline","31 Mar 2026")'''
    jobs_page.verify_job_id("Sym0071","Python developer")


    view_btn=ViewJob(page)
    #view_btn.import_resumes()
    view_btn.view_job() 

    all_applicant=Allapplicant(page)
    all_applicant.import_resumes()

    all_applicant.advance_filters("Google Ads","Meta Ads","Retargeting Strategies","mekalarakesh26102000@gmail.com","9515798304","Hyderabad","Bengaluru","25")

    all_applicant.verify_applicant_filtered("Rakesh Mekala")

    all_applicant.verify_advance_filters_mails_sent_list("Senior Software Developer","MGS Technologies Pvt Ltd")
    all_applicant.verify_advance_filters_given_mails_list("B.Tech","Srinivasa Engineering College","Computer Science & Information Technology")
    

    all_applicant.verify_advance_filter_applicant("bhargav.tumati@gmail.com","Technical round","Face to Face","Chennai","Zoom","9765545567","20-02-2026","10:00","12:00","It is purelyy for full stack developers employees with min 5 years of experience")
    all_applicant.un_viewed_applicants("Male")
    all_applicant.advance_filters_exclude_keywords('("Tag Manager" or "Performance Marketing")',"Meta Ads","SURESH PAGAR")


    




