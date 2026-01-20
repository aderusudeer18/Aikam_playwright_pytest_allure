from playwright.sync_api import sync_playwright 
import allure 
import pytest 



class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://aikam-app-qa-793571778940.asia-south1.run.app/")

    def login(self, email, password):
        with allure.step("login with valid creditionals"):
            self.page.wait_for_selector('//input[@type="email"]').type(email)
            self.page.wait_for_selector('//input[@type="password"]').type(password)
            self.page.wait_for_selector('//div[text()="Login"]').click()

    
  