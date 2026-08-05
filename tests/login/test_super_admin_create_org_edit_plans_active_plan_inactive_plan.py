from pages.super_admin.login import LoginSuperadminPage 
from pages.super_admin.dashboard import DashboardPage
from pages.super_admin.organisations import Organisation
import allure 

def test_super_admin(page):
    login_page=LoginSuperadminPage(page)
    login_page.open()
    login_page.login_super_admin("aikam@symphonize.com","Symphonize8*")

    org=DashboardPage(page)
    org.create_organization_btn()
    org.org_details("ENG","sam curren","ppfylvcxys@olipii.com","Service based","97056531736")

    search_org=Organisation(page)
    search_org.org_details("olipii", "ENG")
