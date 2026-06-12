from playwright.sync_api import expect, TimeoutError
import pytest
import allure
from datetime import datetime


class CreateJobPage:
    def __init__(self, page):
        self.page=page



    def create_job(self,timeout):
        create_job_btn = self.page.locator('//button[contains(text(),"Create Job")]')
        create_job_btn.wait_for(state="visible", timeout=timeout)
        create_job_btn.click()
        allure.attach(
            f"Create job button clicked successfully",
            name="Success",
            attachment_type=allure.attachment_type.TEXT)

    

    def verify_job_description(self,description,timeout=5000):
        textarea = self.page.locator("//textarea[@placeholder='Example: We are hiring a frontend developer with 3+ years experience in React who can build scalable SaaS applications']")
        textarea.wait_for(state="visible", timeout=5000)
        textarea.fill(description)  
        create_ai = self.page.locator("//button[contains(text(),'Create with AI')]")
        create_ai.wait_for(state="visible", timeout=timeout)
        create_ai.click()

        
    # job title
    def select_job_title(self, title:str,timeout=3000):
        with allure.step("Input has passed to Job title"):
            job_title_input = self.page.locator('//input[@placeholder="Title that describes the role"]')
            job_title_input.wait_for(state="visible", timeout=timeout)
            current_value = job_title_input.input_value()
            if current_value.strip() and not any(p in current_value.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                allure.attach(
                    f"Job title is already filled with '{current_value}'. Skipping fill with '{title}'.",
                    name="Skip_Fill",
                    attachment_type=allure.attachment_type.TEXT
                )
                return
            job_title_input.click()
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
                            f"Job title '{title}' selected from dropdown",
                            name="Dropdown_Select",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        break

            except TimeoutError:
                pass   # No dropdown shown -> allowed

            if not matched:
                allure.attach(
                    f"Job title '{title}' kept as manual input",
                    name="Manual_Input",
                    attachment_type=allure.attachment_type.TEXT
                )

            
    #job_type

    def select_job_type(self,value : str,timeout=5000):
        with allure.step("Given input is matched with job_type options and selected"):
            job_type_select = self.page.locator('//button[@role="combobox"]').nth(0)
            job_type_select.wait_for(state="visible", timeout=timeout)
            current_text = job_type_select.text_content() or ""
            if current_text.strip() and not any(p in current_text.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                allure.attach(
                    f"Job type is already filled with '{current_text.strip()}'. Skipping fill with '{value}'.",
                    name="Skip_Fill",
                    attachment_type=allure.attachment_type.TEXT
                )
                return
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
            workplace_type.wait_for(state="visible", timeout=5000)
            current_text = workplace_type.text_content() or ""
            if current_text.strip() and not any(p in current_text.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                allure.attach(
                    f"Worktype is already filled with '{current_text.strip()}'. Skipping fill with '{value}'.",
                    name="Skip_Fill",
                    attachment_type=allure.attachment_type.TEXT
                )
                return
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
            current_text = location_container.text_content() or ""
            if current_text.strip() and not any(p in current_text.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                allure.attach(
                    f"Location is already filled with '{current_text.strip()}'. Skipping fill with '{location}'.",
                    name="Skip_Fill",
                    attachment_type=allure.attachment_type.TEXT
                )
                return
            location_container.click(force=True)

            location_input = self.page.locator("input[type='text']:not([disabled])").last
            expect(location_input).to_be_visible(timeout=timeout)

           
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
            

    # project_team_size
    def select_project_team_size(self, value: str,timeout=5000):
        with allure.step("Selected valid option in project team size:{team_size}"):
        
        
            dropdown = self.page.locator("//button[@type='button']").nth(4)
            dropdown.wait_for(state="visible", timeout=timeout)
            current_text = dropdown.text_content() or ""
            if current_text.strip() and not any(p in current_text.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                allure.attach(
                    f"Project team size is already filled with '{current_text.strip()}'. Skipping fill with '{value}'.",
                    name="Skip_Fill",
                    attachment_type=allure.attachment_type.TEXT
                )
                return
            dropdown.click()

            option = self.page.get_by_role("option", name=value, exact=True)

            if option.count() == 0:
                pytest.fail(f"Invalid date and month '{value}'. Please provide valid input.")

            option.click()

            allure.attach(
                f"Job type '{value}' selected successfully",
                name="Success",
                attachment_type=allure.attachment_type.TEXT)
    

        
        

    def select_work_experience(self, exp_1, exp_2,timeout=5000):
        with allure.step(f"Select work experience: {exp_1} - {exp_2}"):
            try:
                min_exp_input = self.page.locator('//input[@placeholder="Min"]')
                max_exp_input = self.page.locator('//input[@placeholder="Max"]')
                min_exp_input.wait_for(state="visible", timeout=timeout)
                
                current_min = min_exp_input.input_value()
                current_max = max_exp_input.input_value()

                min_exp = float(exp_1)
                max_exp = float(exp_2)
                if min_exp > max_exp:
                    pytest.fail(f"Invalid Experience Range: Min ({exp_1}) cannot be greater than Max ({exp_2})")

                if current_min.strip() and not any(p in current_min.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                    allure.attach(f"Min experience is already filled with {current_min}. Skipping.", name="Skip_Fill_Min", attachment_type=allure.attachment_type.TEXT)
                else:
                    min_exp_input.fill(str(exp_1))

                if current_max.strip() and not any(p in current_max.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                    allure.attach(f"Max experience is already filled with {current_max}. Skipping.", name="Skip_Fill_Max", attachment_type=allure.attachment_type.TEXT)
                else:
                    max_exp_input.fill(str(exp_2))
                
                allure.attach(f"Work experience action processed", name="Success", attachment_type=allure.attachment_type.TEXT)
            except ValueError:
                 pytest.fail(f"Invalid Experience values: {exp_1}, {exp_2}. Must be numbers.")
            except Exception as e:
                pytest.fail(f"Failed to enter work experience: {e}")

    def salary_range(self, min_sal, max_sal,timeout=5000):
        with allure.step(f"Select salary range: {min_sal} - {max_sal}"):
            try:
                min_salary = self.page.locator('//input[@name="minsalary"]')
                max_salary = self.page.locator('//input[@name="maxsalary"]')
                min_salary.wait_for(state="visible", timeout=timeout)
                
                current_min = min_salary.input_value()
                current_max = max_salary.input_value()

                min_s = float(min_sal)
                max_s = float(max_sal)
                if min_s > max_s:
                    pytest.fail(f"Invalid Salary Range: Min ({min_sal}) cannot be greater than Max ({max_sal})")

                if current_min.strip() and not any(p in current_min.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                    allure.attach(f"Min salary is already filled with {current_min}. Skipping.", name="Skip_Fill_Min_Sal", attachment_type=allure.attachment_type.TEXT)
                else:
                    min_salary.fill(str(min_sal))

                if current_max.strip() and not any(p in current_max.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                    allure.attach(f"Max salary is already filled with {current_max}. Skipping.", name="Skip_Fill_Max_Sal", attachment_type=allure.attachment_type.TEXT)
                else:
                    max_salary.fill(str(max_sal))
                
                allure.attach(f"Salary range action processed", name="Success", attachment_type=allure.attachment_type.TEXT)
            except ValueError:
                pytest.fail(f"Invalid Salary values: {min_sal}, {max_sal}. Must be numbers.")
            except Exception as e:
                pytest.fail(f"Failed to enter salary range: {e}")

    def select_target_deadline(self,target:str,timeout=5000):
       
        with allure.step("Select date according to input"):
            date_button = self.page.locator("//label[text()='Target Deadline']/following::button[1]")
            date_button.wait_for(state="visible", timeout=timeout)
            current_text = date_button.text_content() or ""
            if current_text.strip() and not any(p in current_text.lower() for p in ["select", "search", "choose", "enter", "pick", "placeholder"]):
                allure.attach(
                    f"Target deadline is already filled with '{current_text.strip()}'. Skipping fill with '{target}'.",
                    name="Skip_Fill",
                    attachment_type=allure.attachment_type.TEXT
                )
                return

            target = datetime.strptime(target, "%d-%m-%Y")

       
            date_button.click()

            calendar = self.page.locator("//div[@role='dialog']")
            expect(calendar).to_be_visible(timeout=timeout)

        
            month_year = calendar.locator("//div[@aria-live='polite'] | //h6 | //div[contains(@class,'Header')]")
            expect(month_year.first).to_be_visible(timeout=timeout)

          
            nav_buttons = calendar.locator("//button")
            prev_btn = nav_buttons.nth(0)
            next_btn = nav_buttons.nth(1)

            expect(next_btn).to_be_visible(timeout=timeout)
            current = datetime.strptime(
                month_year.first.inner_text().strip(),"%B %Y")

            while (current.year, current.month) != (target.year, target.month):

                if (current.year, current.month) < (target.year, target.month):
                    next_btn.click()
                else:
                    prev_btn.click()

                self.page.wait_for_timeout(300)

                current = datetime.strptime(month_year.first.inner_text().strip(),"%B %Y")


            day_btn = calendar.locator(f"//button[not(@disabled) and normalize-space()='{target.day}']")
            if day_btn.count() == 0:
                pytest.fail(f"Day {target.day} not found in calendar")

            day_btn.first.click()

            allure.attach(
                f"Date {target} selected successfully",
                name="Date Selected",
                attachment_type=allure.attachment_type.TEXT)

    


    def publish_btn(self,timeout=2000):

        with allure.step("Publish Job"):
            publish_btn=self.page.locator("//button[contains(text(),'Publish')]")
            publish_btn.wait_for(state="visible", timeout=timeout)
            publish_btn.click()
            allure.attach(
                f"Job is published successfully",
                name="Test_Success_Message",
                attachment_type=allure.attachment_type.TEXT)
        



    

   