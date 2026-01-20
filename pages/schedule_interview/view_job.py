from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 


class ViewJob:
    def __init__(self,page):
        self.page=page 
    
    def view_job(self):
        with allure.step("View Applicant button is visible"):
            self.page.wait_for_selector("//p[contains(text(),'View Applicants')]").click()