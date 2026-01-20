from playwright.sync_api import sync_playwright,expect 
import pytest 
import allure 

class jobsPage:
    def __init__(self,page):
        self.page=page

    def jobs_page(self,timeout=3000):
        with allure.step("Entered valid creditionals and jobs page is visible"):
            self.page.get_by_role("row", name="Tek0034 Software Engineer").get_by_role("link").click()

