from pages.login_advance_filters_applicant_page.login_page import LoginPage 
from pages.login_advance_filters_applicant_page.dash_board_page import DashboardPage
from pages.login_advance_filters_applicant_page.jobs_list_page import JobsPage 
from pages.login_advance_filters_applicant_page.view_applicant_page_details import ViewJob 
from pages.login_advance_filters_applicant_page.all_applicant_advance_filters_page import Allapplicant 

# login  -> select random job -> if any exists applicant delete all ->import resumes around 20 -> apply advance filters ->if multiple applicants found select particular applicant then open -> first send mail -> schedule ai prescreening->and schedule Ai interview -> ai code assessment->ai code assessment ->click on resume to download ->then schedule manual interview -> download applicant card->share applicant ->provide feedback ->check reviewr back is saved

def test_login_to_applicant_page(page):
    login = LoginPage(page)
    login.open()
    login.test_login_email_password("himakar.vempati@tekworks.in", "Admin!@3") 

    #dashboard=DashboardPage(page)
    #dashboard.job_icon()

    jobs_page=JobsPage(page)
    jobs_page.wait_until_jobs_page("Tek0078","Python Developer")


    view_btn=ViewJob(page)
    view_btn.view_job() 

    all_applicant=Allapplicant(page)
    all_applicant.import_resumes()

    all_applicant.advance_filters("Google Ads","Meta Ads","Retargeting Strategies","mekalarakesh26102000@gmail.com","9515798304","Hyderabad","Bengaluru","25")

    all_applicant.test_verify_applicant_filtered("Rakesh Mekala")

    all_applicant.test_advance_filters_mails_sent_list("Senior Software Developer","MGS Technologies Pvt Ltd")
    all_applicant.test_advance_filters_given_mails_list("B.Tech","Srinivasa Engineering College","Computer Science & Information Technology")
    

    all_applicant.test_advance_filter_applicant("bhargav.tumati@gmail.com","Technical round","Bengaluru","Face to Face","25-02-2026","10:00 AM","12:00 PM","It is purelyy for full stack developers employees with min 5 years of experience")

    all_applicant.un_viewed_applicants()
    all_applicant.advance_filters_exclude_keywords("Email Marketing","RAHUL KUMAR")


    




