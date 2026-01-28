from playwright.sync_api import expect, TimeoutError
import pytest
import allure
from datetime import datetime


class CreateJobPage:
    def __init__(self, page):
        self.page = page
        
    # job title
    def select_job_title(self, title:str,timeout=3000):
        with allure.step("Input has passed to Job title"):
            job_title_input = self.page.locator('//input[@role="combobox"]')
            expect(job_title_input).to_be_visible(timeout=1500)
            expect(job_title_input).to_be_enabled()
            job_title_input.click()
            job_title_input.fill("")
            job_title_input.fill(title) 

            options = self.page.locator('[role="option"]')
            matched = False

            
            try:
                options.first.wait_for(state="visible", timeout=2000)

                texts = options.all_inner_texts()
                for i, text in enumerate(texts):
                    if text.strip().lower() == title.strip().lower():  
                        options.nth(i).click()
                        matched = True
                        allure.attach(
                            f"Job title '{title}' selected successfully",
                            name="Test_Success_Message",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        break

            except TimeoutError:
                pass

            
            if not matched:
                pytest.fail(
                    f"Invalid job title '{title}'. Exact match not found in dropdown options: {texts}")
                

                
            ''' job_title_input = self.page.locator('//input[@role="combobox"]')
            expect(job_title_input).to_be_visible(timeout=1500)
            expect(job_title_input).to_be_enabled()
            job_title_input.click()
            job_title_input.fill("")
            self.page.keyboard.type(title, delay=100)
            options = self.page.locator('[role="option"]')
            matched = False
            try:
                options.first.wait_for(state="visible", timeout=1000)
                texts = options.all_inner_texts()
                for i, text in enumerate(texts):
                    if text.strip().lower() == title.strip().lower():
                        options.nth(i).click()
                        matched = True
                        allure.attach(
                    "Test case passed successfully:given input job title is valid and selected",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
                        break

            except TimeoutError:
                pass
        with allure.step("Give job title is Invalid ,please check"):
            if not matched:
                self.page.keyboard.press("Enter")'''
    #job_type

    def select_job_type(self,value : str,timeout=5000):
        with allure.step("Given input is matched with job_type options and selected"):
            job_type_select = self.page.locator('//button[@role="combobox"]').nth(0)
            job_type_select.click()

            option = self.page.get_by_role("option", name=value, exact=True)

            if option.count() == 0:
                pytest.fail(f"Invalid job type '{value}'. Please provide valid input.")

            option.click()

            allure.attach(
                f"Job type '{value}' selected successfully",
                name="Success",
                attachment_type=allure.attachment_type.TEXT
            )
                
    #worktype
    def select_worktype(self, value: str):
        with allure.step(f"Select worktype: {value}"):

            workplace_type = self.page.locator('//button[@type="button"]').nth(2)
            workplace_type.click()

            option = self.page.get_by_role("option", name=value, exact=True)

            if option.count() == 0:
                pytest.fail(f"Invalid job type '{value}'. Please provide valid input.")

            option.click()

            allure.attach(
                f"Job type '{value}' selected successfully",
                name="Success",
                attachment_type=allure.attachment_type.TEXT
            )
            



    #location

    def select_location(self, location:str,timeout=3000):

        with allure.step("Select location"):
            location_container = self.page.locator("//label[normalize-space()='Job Location']/following-sibling::*[1]")
            expect(location_container).to_be_visible(timeout=3000)
            location_container.click(force=True)

            location_input = self.page.locator("input[type='text']:not([disabled])").last
            expect(location_input).to_be_visible(timeout=timeout)

            #location_input.fill("")
            location_input.fill(location)

            option = self.page.locator(
                f"//div[@role='option'][translate(normalize-space(text()),"
                f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')="
                f"'{location.lower()}']")

            if option.count() == 0:
                pytest.fail(f"Invalid location '{location}'. Please provide valid location.")

            option.first.scroll_into_view_if_needed()
            option.first.click()

            selected_location = self.page.locator(f"//*[normalize-space()='{location}']")
            

            allure.attach(
                f"Location '{location}' selected successfully",
                name="Location Selected",
                attachment_type=allure.attachment_type.TEXT)



        ''' location_container = self.page.locator("//label[normalize-space()='Job Location']/following-sibling::*[1]")
            expect(location_container).to_be_visible(timeout=timeout)
            location_container.click(force=True)
            location_input = self.page.locator("input[type='text']:not([disabled])").last
            expect(location_input).to_be_visible(timeout=timeout)
            location_input.fill("")
            location_input.type(location, delay=100)
            dropdown_feedback = self.page.locator("text=/no location|no results|not found/i")
            allure.attach(
                    "Test case passed successfully:Given location is matched and selected",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            if dropdown_feedback.is_visible():
                pytest.fail(f"No location  found'{location}'")
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(300)
            selected_value = location_input.input_value().strip().lower()'''
            



        

            
        


    # project_team_size
    def select_project_team_size(self, value: str,timeout=5000):
        with allure.step("Selected valid option in project team size:{team_size}"):
        
        
            dropdown = self.page.locator("//button[@type='button']").nth(4)
            dropdown.click()

            option = self.page.get_by_role("option", name=value, exact=True)

            if option.count() == 0:
                pytest.fail(f"Invalid job type '{value}'. Please provide valid input.")

            option.click()

            allure.attach(
                f"Job type '{value}' selected successfully",
                name="Success",
                attachment_type=allure.attachment_type.TEXT)
    

        
        

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

    def select_target_deadline(self,target:str,timeout=5000):
       
        with allure.step("Select date according to input"):
            target = datetime.strptime(target, "%d-%m-%Y")

       
            self.page.locator("//label[text()='Target Deadline']/following::button[1]").click()

            calendar = self.page.locator("//div[@role='dialog']")
            expect(calendar).to_be_visible(timeout=timeout)

            # 👉 Month-Year header (generic & reliable)
            month_year = calendar.locator(
                "//div[@aria-live='polite'] | //h6 | //div[contains(@class,'Header')]"
            )
            expect(month_year.first).to_be_visible(timeout=timeout)

            # 👉 Navigation arrows (first = prev, second = next)
            nav_buttons = calendar.locator("//button")
            prev_btn = nav_buttons.nth(0)
            next_btn = nav_buttons.nth(1)

            expect(next_btn).to_be_visible(timeout=timeout)

            # Read current month/year
            current = datetime.strptime(
                month_year.first.inner_text().strip(),
                "%B %Y"
            )

            # Navigate only if needed
            while (current.year, current.month) != (target.year, target.month):

                if (current.year, current.month) < (target.year, target.month):
                    next_btn.click()
                else:
                    prev_btn.click()

                self.page.wait_for_timeout(300)

                current = datetime.strptime(
                    month_year.first.inner_text().strip(),
                    "%B %Y"
                )

            # 👉 Select day
            day_btn = calendar.locator(
                f"//button[not(@disabled) and normalize-space()='{target.day}']"
            )

            if day_btn.count() == 0:
                pytest.fail(f"Day {target.day} not found in calendar")

            day_btn.first.click()

            allure.attach(
                f"Date {target} selected successfully",
                name="Date Selected",
                attachment_type=allure.attachment_type.TEXT
            )


        ''' with allure.step("Given deadline is valid and selected"):
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
            date_button.click()''' 

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
        allure.attach(
                    "Test case passed successfully:Clicked on Ai button to generate Ai description ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

    def select_Ai_description(self,message,timeout=12000):
        prompt =self.page.locator("//textarea[@placeholder='Enter your prompt']").fill(str(message))
        generate_Ai=self.page.locator("//button[contains(text(),'Generate with AI')]").click()
        allure.attach(
                    "Test case passed successfully:input is passed to Ai Description",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

    def select_next_btn2(self,timeout=18000):
        next_btn = self.page.get_by_role("button", name="Next")
        expect(next_btn).to_be_visible(timeout=5000)
        expect(next_btn).to_be_enabled()
        next_btn.click()
        