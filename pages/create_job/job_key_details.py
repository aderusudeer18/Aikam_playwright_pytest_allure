from playwright.sync_api import expect, TimeoutError
import pytest
import allure


class CreateJobPage:
    def __init__(self, page):
        self.page = page
        
    # job title
    def select_job_title(self, title:str,timeout=5000):
        with allure.step("Input has passed to Job title"):
            job_title_input = self.page.locator('//input[@role="combobox"]')
            expect(job_title_input).to_be_visible(timeout=15000)
            expect(job_title_input).to_be_enabled()
            job_title_input.click()
            job_title_input.fill("")
            self.page.keyboard.type(title, delay=120)
            options = self.page.locator('[role="option"]')
            matched = False
            try:
                options.first.wait_for(state="visible", timeout=4000)
                texts = options.all_inner_texts()
                for i, text in enumerate(texts):
                    if text.strip().lower() == title.strip().lower():
                        options.nth(i).click()
                        matched = True
                        break
            except TimeoutError:
                pass
        with allure.step("Give job title is Invalid ,please check"):
            if not matched:
                self.page.keyboard.press("Enter")
    #job_type

    def select_job_type(self,value : str,timeout=5000):
        with allure.step("Given input is matched with job_type options and selected"):
            job_type_select = self.page.locator('//button[@role="combobox"]').nth(0)
            job_type_select.click()
        with allure.step("Given input is not Matched with Job_type options,please provide Valid Input"):
            if value not in value:
                pytest.fail(f"Invalid job type '{value}'. Available options: {value}")
            self.page.get_by_role("option", name=value).click()
    
                
    #worktype
    def select_worktype(self, value: str):
        with allure.step(f"Select worktype: {value}"):
            workplace_type = self.page.locator('//button[@type="button"]').nth(2)
            workplace_type.click()
            if value not in value:
                pytest.fail(f"Invalid worktype '{value}'. Available options: {value}")
            self.page.get_by_role("option", name=value).click()

            option = self.page.locator(f"//div[normalize-space(text())='{value}']")
            



    #location

    def select_location(self, location: str,timeout=5000):
        with allure.step("Select location"):
            
            location_details = self.page.locator('//button[@type="button"]').nth(3)
            expect(location_details).to_be_visible(timeout=timeout)
            location_details.click()

            enter_location = self.page.locator('//input[@type="text"]').nth(3)
            expect(enter_location).to_be_visible(timeout=timeout)

            enter_location.fill("")
            enter_location.type(location, delay=150)

            options = self.page.locator(
                "//div[contains(@class,'option') or contains(@class,'item') or contains(@class,'list')]"
            )
            options.first.wait_for(timeout=timeout)

            matched = False

            for i in range(options.count()):
                option_text = options.nth(i).inner_text().strip().lower()
                print("Location option:", option_text)

                if location.lower() in option_text:
                    options.nth(i).click()
                    matched = True
                    break

            if not matched:
                pytest.fail(f"Location '{location}' not found")



    # project_team_size
    def select_project_team_size(self, team_size: str,timeout=5000):
        with allure.step("Selected valid option in project team size:{team_size}"):
            dropdown = self.page.locator("//button[@type='button']").nth(4)
            dropdown.click()
            options = self.page.locator('//div[@role="group"]//div')
            options.first.wait_for(state="visible", timeout=5000)

            texts = options.all_inner_texts()

            for i, text in enumerate(texts):
                if text.strip() == team_size:
                    options.nth(i).click()
                    return

            raise AssertionError(
                f"Team size '{team_size}' not found. Available options: {texts}")
        
    '''def select_project_team_size(self, timeout=15000):
        with allure.step("Select project team size"):
            
            dropdown = self.page.locator("//div[contains(@class,'team-size')]")
            dropdown.click()

            options = self.page.locator("//div[@role='group']//div[@role='option']")

            expect(options.first).to_be_visible(timeout=timeout)

            options.first.click()'''

            

        

    def select_work_experience(self, exp_1, exp_2,timeout=5000):
        with allure.step("Given min and max experience is valid inputs"):
            self.page.locator('//input[@placeholder="Min"]').fill(str(exp_1))
            self.page.locator('//input[@placeholder="Max"]').fill(str(exp_2))
        with allure.step("Given inputs are Invalid,please check the min exp is always less than max exp"):
            if exp_1 >= exp_2:
                expect(self.page.get_by_text("Minimum experience cannot be greater than maximum experience")).to_be_visible()

    def salary_range(self, min_sal, max_sal,timeout=5000):
        with allure.step("Given salary range is valid inputs"):
            min_salary = self.page.locator('//input[@name="minsalary"]')
            max_salary = self.page.locator('//input[@name="maxsalary"]')
            min_salary.fill(str(min_sal))
            max_salary.fill(str(max_sal))
        with allure.step("Given salary range is Invalid,please provide valid inputs the MIN salary is always less than MAX salary range"):
            if min_sal >= max_sal:
                expect(self.page.get_by_text("Minimum salary cannot be greater to maximum salary")).to_be_visible()

    def select_target_deadline(self,value,timeout=5000):
        with allure.step("Given deadline is valid and selected"):
            self.page.locator("//label[text()='Target Deadline']/following::button[1]").click() 
            self.page.wait_for_selector("//div[@role='dialog' and @data-state='open']") 
            target_month = "January" 
            while True: 
                current_month = self.page.locator("//div[@role='dialog']//*[contains(text(),'2026')]").inner_text() 
                if target_month in current_month: 
                    break 
                else: 
                    wrong_date=self.page.locator("//button[contains(@aria-label,'Next')]") 
                    wrong_date.click() 
            date_button = self.page.locator("//div[@role='dialog']//button[normalize-space(text())='30' and not(@disabled)]") 
            date_button.scroll_into_view_if_needed() 
        with allure.step("Given deadline is Invalid,select the date from Tommorrow"):
            expect(date_button,"input is valid and selected").to_be_visible(timeout=2000) 
            date_button.click() 

    def select_next_btn1(self,timeout=5000):
        with allure.step("Selected all mandatory fields in the job key details page and clicked on next button"):
            next1=self.page.locator('//button[@type="button"]').nth(7) 
            expect(next1).to_be_visible(timeout=5000)
            expect(next1).to_be_enabled()
            next1.click() 

    def write_with_Ai(self):
        ai_btn = self.page.locator("//button[contains(.,'Write with AI')]")
        expect(ai_btn).to_be_visible(timeout=5000)
        expect(ai_btn).to_be_enabled()
        ai_btn.click()

    def select_Ai_description(self,message,timeout=12000):
        prompt =self.page.locator("//textarea[@placeholder='Enter your prompt']").fill(str(message))
        generate_Ai=self.page.locator("//button[contains(text(),'Generate with AI')]").click()

    def select_next_btn2(self,timeout=18000):
        next_btn = self.page.get_by_role("button", name="Next")
        expect(next_btn).to_be_visible(timeout=5000)
        expect(next_btn).to_be_enabled()
        next_btn.click()