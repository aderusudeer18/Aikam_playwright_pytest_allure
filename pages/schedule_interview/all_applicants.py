from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 
 

class AllApplicant:
    def __init__(self,page):
        self.page=page 

    def all_applicant(self):
        with allure.step("selected Applicant in the all applicants page"):
            card = self.page.get_by_text("SARVANI GANGARAJU")
            self.page.wait_for_timeout(2000)
            card_box = card.bounding_box()
            checkboxes = self.page.locator("input[type='checkbox']")
            count = checkboxes.count()
            closest_index = 0
            closest_distance = float("inf")
            for i in range(count):
                box = checkboxes.nth(i).bounding_box()
                if box:
                    distance = abs(box["y"] - card_box["y"])
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_index = i
            checkboxes.nth(closest_index).click() 

    def schedule_interview(self):
        with allure.step("clicked on schedule interview button"):
            self.page.on("dialog",lambda dialog:dialog.accept())
            self.page.locator('//button[contains(text(),"Schedule AI Interview")]').click()
            self.page.wait_for_selector('//label[contains(text(),"Video Interview")]').click()
    
            self.page.wait_for_selector('//label[contains(text(),"Coding Assessment")]').click()
        
            
            self.page.locator("//button[contains(text(),'Next')]").click()
            
            self.page.get_by_role("button", name="Next").click()
            self.page.get_by_role("button", name="Next").click()
            self.page.get_by_role("button", name="Schedule", exact=True).click()
