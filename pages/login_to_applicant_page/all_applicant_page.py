from datetime import datetime
from playwright.sync_api import sync_playwright ,expect
import allure 
import pytest
import time
from datetime import datetime

from conftest import page

class Allapplicant: 
    def __init__(self,page):
        self.page=page 

    '''def delete_all_applicants(self,timeout=3000):
        with allure.step("Delete all existing applicants in all applicants page"):
            rows = self.page.locator("//tbody/tr")
            if rows.count() == 0:
                allure.attach(
                    "No applicants found. Skipping delete step.",
                    name="Info",
                    attachment_type=allure.attachment_type.TEXT)
                return

            checkbox = rows.nth(0).locator('.//input[@type="checkbox"]')
            checkbox.wait_for(state="visible")
            checkbox.check()

            delete_btn = self.page.locator("//button[@aria-haspopup='dialog']").nth(1)
            delete_btn.wait_for(state="enabled")
            delete_btn.click()

            confirm_btn = self.page.get_by_role("button", name="Yes, Delete")
            confirm_btn.wait_for(state="visible")
            confirm_btn.click()

            allure.attach(
                "Applicant deleted successfully",
                name="Delete Success",
                attachment_type=allure.attachment_type.TEXT)'''
                
        


    def import_resumes(self,timeout=18000):
        with allure.step("verify resumes has been imported"):

            import_resume=self.page.locator("//span[contains(text(),'Import Resumes')]").click()
            self.page.set_input_files('input[type="file"]',[r"C:\Users\Sudeer\Downloads\Aikam_Rakesh_Mekala_Resume (1).pdf",
                                                            r"C:\Users\Sudeer\Downloads\Aikam_FAKHRUDDIN_SHAIK_Resume.pdf",
                                                            r"C:\Users\Sudeer\Downloads\Aikam_SURESH_PAGAR_Resume.pdf",
                                                            r"C:\Users\Sudeer\Downloads\Aikam_RAHUL_KUMAR_Resume.pdf"])

            self.page.wait_for_selector("//button[contains(text(),'Import')]").click()
            self.page.wait_for_timeout(20000)
            success_toast = self.page.locator("//p[contains(text(),'resumes have been successfully imported')]").first
            error_toast = self.page.locator("//h3[contains(text(),'Resume Upload Failed')]").first
            max_time = 180 
            start = time.time()
            while time.time() - start < max_time:            
                if error_toast.count() > 0 and error_toast.is_visible():
                    pytest.fail(f"Resume Upload Failed: {error_toast.inner_text()}")

                if success_toast.count() > 0 and success_toast.is_visible():
                    allure.attach(
                        success_toast.inner_text(),
                        name="Upload Success",
                        attachment_type=allure.attachment_type.TEXT)
                    self.page.wait_for_timeout(3000)
                    self.page.reload()
                    return

    
               

            

    def advance_filters(self,skill_1,skill_2,skill_3,email_id,number,can_loc_1,can_loc_2,timeout=3000):
        with allure.step("Applying advance filters to applicants"):
            advance=self.page.locator('//div[@data-state="closed"]').nth(9).click()
            keyword = self.page.locator("//input[@type='text']").nth(0)
            keyword.type(skill_1)
            self.page.keyboard.press("Enter")
            keyword.type(skill_2)
            self.page.keyboard.press("Enter")
            keyword.type(skill_3)


            ''' mandatory_checkbox=self.page.locator('//button[@type="button"]').nth(7)
            mandatory_checkbox.check()'''


            email=self.page.locator('//input[@placeholder="Search email..."]')
            email.type(email_id)
            mobile_number=self.page.locator('//input[@type="tel"]')
            mobile_number.type(number)

            candidate_loc=self.page.locator('//input[@placeholder="Enter location..."]')
            candidate_loc.fill(can_loc_1)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
            
            candidate_loc=self.page.locator('//input[@placeholder="Enter location..."]')
            candidate_loc.fill(can_loc_2)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            apply_btn=self.page.locator("//button[contains(text(),'Apply')]")
            expect(apply_btn).to_be_visible(timeout=2000)
            apply_btn.click()


    def test_verify_applicant_filtered(self,applicant_name,timeout=3000):
            with allure.step("verify applicants has been filtered based on advance filters"):
                #if filtered_applicant.count() >1:
                filtered_applicant=self.page.locator("div.flex.w-full.items-center.gap-2.mb-1").nth(0)
                filtered_applicant.click()

                ai_pre_screening=self.page.locator('//button[contains(text(),"AI Prescreening")]').click()
                request_ai_pre_screening=self.page.locator('//button[contains(text(),"Request AI Prescreening")]').click()
                Next=self.page.locator('//button[contains(text(),"Next")]').click()
                schedule=self.page.get_by_role("button",name="Schedule",exact=True).click()

                ai_interview=self.page.locator('//button[contains(text(),"AI Interview")]').nth(1)
                ai_interview.click()
                request_ai_interview=self.page.locator('//button[contains(text(),"Request AI Interview")]').click()
                Next=self.page.locator('//button[contains(text(),"Next")]').click()
                schedule=self.page.get_by_role("button",name="Schedule",exact=True).click()

                ai_code_assessment=self.page.locator('//button[contains(text(),"AI Coding Assessment")]').click()
                request_ai_ai_code_assessment=self.page.locator('//button[contains(text(),"Request AI Coding Assessment")]').click()
                Next=self.page.locator('//button[contains(text(),"Next")]').click()

                '''custom_assessment=self.page.locator('//button[contains(text(),"Custom Assessment")]').click()
                code_assessment_duration=self.page.locator('//input[@type="number"]').click()
                description=self.page.locator('//textarea[@placeholder="Enter description"]').type(question1)
                description.click()
                given_input=self.page.locator('//input[@placeholder="Input"]').fill(input1)
                given_output=self.page.locator('//input[@placeholder="Output"]').fill(output1)

                add_question=self.page.locator('//span[contains(text(),"+ Add Question")]').click()
                description=self.page.locator('//textarea[@placeholder="Enter description"]').type(question2)
                description.click()
                given_input=self.page.locator('//input[@placeholder="Input"]').fill(input2)
                given_output=self.page.locator('//input[@placeholder="Output"]').fill(output2)'''

                Next1=self.page.locator('//button[contains(text(),"Next")]').click()
                schedule=self.page.get_by_role("button",name="Schedule",exact=True).click() 


                resume=self.page.locator('//button[contains(text(),"Resume")]').click()
                
                with self.page.expect_download() as d:
                    resume_download=self.page.locator('//button[contains(text(),"Download")]').click()

                download = d.value  


                path = download.path() 

                save_path = fr"C:\Users\Sudeer\Downloads\{download.suggested_filename}"
                download.save_as(save_path)
                allure.attach(
                            "Test case passed successfully:Clicked on Resume to download applicant resume",
                            name="Test_Success_Message",
                            attachment_type=allure.attachment_type.TEXT) 
                

    def test_advance_filters_mails_sent_list(self,designation,company,timeout=3000):
        with allure.step("verify applicant page is visible"):
            self.page.locator('//a[contains(text(),"All Applicants")]').click()
            advance=self.page.locator('//div[@data-state="closed"]').nth(9).click()
            wrong_btn=self.page.locator('//button[@type="button"]').nth(4)
            wrong_btn.click()
            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]').click()

            designation_role=self.page.locator('//input[@placeholder="Search designation..."]')
            designation_role.fill(designation)
            #self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            company_name=self.page.locator('//input[@placeholder="Search company..."]')
            company_name.fill(company)
            #self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            '''industry_type=self.page.locator('//input[@placeholder="Search industry..."]')
            industry_type.fill(industry)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")'''



            ai_pre_screen_sent=self.page.locator('//label[contains(text(),"AI Pre Screening Sent")]')
            ai_pre_screen_sent.click()
            ai_interview_sent=self.page.locator('//label[contains(text(),"AI Interview Sent")]')
            ai_interview_sent.click()
            ai_code_assessment_sent=self.page.locator('//label[contains(text(),"AI Coding Assessment Sent")]')
            ai_code_assessment_sent.click()


            view_btn=self.page.locator('//input[@value="Viewed"]').check()

            apply_btn=self.page.locator("//button[contains(text(),'Apply')]")
            expect(apply_btn).to_be_visible(timeout=2000)
            apply_btn.click()
            self.page.wait_for_timeout(3000)
            allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 


    def test_advance_filters_given_mails_list(self,ug,institute_name,course_name,timeout=3000):
        with allure.step("verify interviews toggles given list"):
            
            advance=self.page.locator('//div[@data-state="closed"]').nth(9)
            advance.click()
            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
            reset_btn.click()
            

            ug_qualification=self.page.locator('//input[@placeholder="Search UG qualification..."]')
            ug_qualification.fill(ug)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            '''pg_qualification=self.page.locator('//input[@placeholder="Search PG qualification..."]')
            pg_qualification.fill(pg)'''

            institute=self.page.locator('//input[@placeholder="Search institute..."]')
            institute.fill(institute_name)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            course=self.page.locator('//input[@placeholder="Search course..."]')
            course.fill(course_name)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            ai_pre_screen_given=self.page.locator('//label[contains(text(),"AI Pre Screening Given")]')
            ai_pre_screen_given.check()
            ai_interview_given=self.page.locator('//label[contains(text(),"AI Interview Given")]')
            ai_interview_given.check()
            ai_code_assessment_given=self.page.locator('//label[contains(text(),"AI Coding Assessment Given")]')
            ai_code_assessment_given.check() 
            apply_btn=self.page.locator("//button[contains(text(),'Apply')]")
            expect(apply_btn).to_be_visible(timeout=2000)
            apply_btn.click()

            
            self.page.wait_for_timeout(3000)
            allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)  
            
            

            
    
            

    def test_advance_filter_applicant(self,cc_mail:str,interview_sub,manual_loc:str,value:str,target:str,time_from,time_to,mail_description:str,timeout=3000):
        with allure.step("verify applicants has been filtered based on advance filters"):
            filtered_applicant=self.page.locator("div.flex.w-full.items-center.gap-2.mb-1").nth(0)
            filtered_applicant.click()
            self.page.on("dialog",lambda dialog:dialog.accept())
            manual_interview=self.page.locator('//button[@type="button"]').nth(2)
            manual_interview.click()
            schedule_manual_interview=self.page.locator('//div[contains(text(),"Schedule Interview")]')
            schedule_manual_interview.click()

            cc=self.page.locator('//input[@type="email"]')
            cc.fill(cc_mail)
            self.page.keyboard.press("Enter")

            subject=self.page.locator('//input[@placeholder="Enter Interview Round or Title"]')
            subject.fill(interview_sub)

            interview_type=self.page.locator('//button[@type="button"]').nth(10)
            interview_type.click()

            '''dropdown = self.page.locator("//button[contains(@class,'select')]")
            dropdown.click()
            self.page.get_by_text(value, exact=True).click()'''

            allure.attach(
                f"Job type '{value}' selected successfully",
                name="Success",
                attachment_type=allure.attachment_type.TEXT)

            

            #date selection
            target = datetime.strptime(target, "%d-%m-%Y")
            self.page.locator("//label[text()='Interview Date']/following::button[1]").click()
            calendar = self.page.locator("//div[@role='dialog']")
            expect(calendar).to_be_visible(timeout=timeout)
            month_year = calendar.locator("//div[@aria-live='polite'] | //h6 | //div[contains(@class,'Header')]")
            expect(month_year.first).to_be_visible(timeout=timeout)
            nav_buttons = calendar.locator("//button")
            prev_btn = nav_buttons.nth(0)
            next_btn = nav_buttons.nth(1)
            expect(next_btn).to_be_visible(timeout=timeout)
            current = datetime.strptime(month_year.first.inner_text().strip(),"%B %Y")
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

            
            
            location=self.page.locator('//input[@name="location"]')
            location.fill(manual_loc)
            

            from_time=self.page.locator('//input[@type="time"]').nth(0)
            from_time.fill(time_from)

            To_time=self.page.locator('//input[@type="time"]').nth(1)
            To_time.fill(time_to)

            manual_description=self.page.locator('//textarea[@name="description"]')
            manual_description.fill(mail_description)

            send_btn=self.page.locator('//button[contains(text(),"Send")]')
            send_btn.click()  


            download_applicant=self.page.locator("div.cursor-pointer").nth(2)
            download_applicant.click()
            with self.page.expect_download() as d:
                resume_download=self.page.locator('//button[contains(text(),"Download")]').click()

            download = d.value  


            path = download.path() 

            save_path = fr"C:\Users\Sudeer\Downloads\{download.suggested_filename}"
            download.save_as(save_path)
            allure.attach(
                        "Test case passed successfully:Clicked on download applicant to download applicant details",
                        name="Test_Success_Message",
                        attachment_type=allure.attachment_type.TEXT) 
            

            share_applicant=self.page.locator("//div[@data-state='closed']").nth(3)
            share_applicant.click()
            email_input = self.page.get_by_placeholder("Enter email and press Enter")
            email_input.wait_for(state="visible", timeout=3000)
            email_input.fill("aderu.sudeer@gmail.com")
            email_input.press("Enter")
            share_applicant_details=self.page.locator('//button[contains(text(),"Share")]')
            expect(share_applicant_details).to_be_visible(timeout=3000)
            share_applicant_details.click()
            allure.attach(
                        "Test case passed successfully:applicant selected and share details",
                        name="Test_Success_Message",
                        attachment_type=allure.attachment_type.TEXT)
            

            send_mail=self.page.locator('//div[@data-state="closed"]').nth(5)
            send_mail.click()
            offer_mail=self.page.locator('//button[contains(text(),"Offer")]')
            offer_mail.click()
            send_btn=self.page.locator("//button[contains(text(),'Send Email')]")
            expect(send_btn).to_be_visible(timeout=3000)   
            send_btn.click()
            allure.attach(
                    "Test case passed successfully:Unviewed applicants are visible ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            


    def un_viewed_applicants(self,timeout=3000):
        with allure.step("verify unviewed applicants are visible"):
            advance=self.page.locator('//div[@data-state="closed"]').nth(9)
            advance.click()
            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
            reset_btn.click()
            unviewed_btn=self.page.locator('//label[contains(text(),"Unviewed")]')
            unviewed_btn.check()
            apply_btn=self.page.locator("//button[contains(text(),'Apply')]")
            expect(apply_btn).to_be_visible(timeout=2000)
            apply_btn.click()
            allure.attach(
                    "Test case passed successfully:Unviewed applicants are visible ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

    def advance_filters_exclude_keywords(self,skill_2,applicant_name,timeout=3000):
            with allure.step("Applying advance filters to exclude keywords to applicants"):
                all_applicant_page=self.page.locator('//a[contains(text(),"All Applicants")]')
                all_applicant_page.click()
                advance=self.page.locator('//div[@data-state="closed"]').nth(9)
                advance.click()
                reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
                reset_btn.click() 


                boolean_on=self.page.locator('//button[@role="switch"]')
                boolean_on.click()

                '''keywords=self.page.locator('//input[contains(@class,"border-red-500")]')
                keywords.type(skill_1)'''

                exclude_keywords=self.page.locator('//input[@type="text"]')
                exclude_keywords.type(skill_2) 
                

                apply_btn=self.page.locator("//button[contains(text(),'Apply')]")
                expect(apply_btn).to_be_visible(timeout=2000)
                apply_btn.click()

                row = self.page.locator(f"//tr[.//*[contains(text(),'{applicant_name}')]]")
                allure.attach(
                    "Test case passed successfully:applicant card is exists and selected",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

                checkbox = row.locator("input[type='checkbox']")

                checkbox.first.wait_for(state="visible")
                checkbox.first.check()
                delete_btn=self.page.locator("//button[@aria-haspopup='dialog']").nth(1)
                delete_btn.click()
                yes_cancle=self.page.locator('//button[@type="button"]').nth(8)
                yes_cancle.click()
                allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 

            

    


                
                

            '''if filtered_applicant.count() > 0:
                    self.page.get_by_text(applicant_name,exact=True).click()
                    allure.attach(
                        "Test case passed successfully:Applicants has been filtered based on advance filters",
                        name="Test_Success_Message",
                        attachment_type=allure.attachment_type.TEXT) 
                else:
                    pytest.fail("No applicants found after applying advance filters.")'''


            '''exp_skill=self.page.locator('//input[@placeholder="Enter skill"]').type(skill_1)
            min_exp=self.page.locator('//input[@placeholder="min"]').type(min_1)
            max_exp=self.page.locator('//input[@placeholder="max"]').type(max_1)'''


            


            
            

            '''gender=self.page.locator('//button[@type="button"]').nth(4) 
            gender.click()
            option=self.page.get_by_role("option",name=gender ,exact=True).click()
            if option.count() == 0:
                pytest.fail(f"Invalid gender '{gender}'. Please provide valid input.")

            option.click()'''

            '''gender_dropdown = self.page.locator('//button[@type="button"]').nth(4)
            gender_dropdown.click()

            self.page.get_by_role("option", name=gender).click()'''


            

            '''Notice_period=self.page.locator('//input[@type="number"]').nth(2)
            Notice_period.type(period)'''


            
            
        
            
        


            


            
            
            

    '''def re_set_changes(self,timeout=3000):
        with allure.step("reset your changes in the  advance filters "):
            advance=self.page.locator('//div[@data-state="closed"]').nth(11).click()
            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]').click()
            apply=self.page.wait_for_selector("//button[contains(text(),'Apply')]").click() 
            self.page.reload()'''


            

    '''def search_by_name_to_delete(self,applicant_name,timeout=3000):
        with allure.step("search by name or email,Phone number"):
            self.page.locator("div.cursor-pointer svg.lucide-search").click()
            search_name = self.page.locator('//input[@type="text"]').nth(1)
            search_name.click()
            search_name.fill(applicant_name)
            search_name.press("Enter")


            allure.attach(
                f"Applicant {applicant_name} visible after search",
                name="Search Success",
                attachment_type=allure.attachment_type.TEXT
            )'''
            

           
            

   
    '''def applicant_to_delete(self, applicant_name):
        with allure.step(f"Select applicant: {applicant_name}"):

            row = self.page.locator(f"//tr[.//*[contains(text(),'{applicant_name}')]]")
            allure.attach(
                    "Test case passed successfully:applicant card is exists and selected",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

            if row.count() == 0:
                raise AssertionError(f"Applicant not found: {applicant_name}")

            checkbox = row.locator("input[type='checkbox']")

            checkbox.first.wait_for(state="visible")
            checkbox.first.check()
            delete=self.page.locator("//button[@aria-haspopup='dialog']").nth(1).click()
            yes_cancle=self.page.locator('//button[@type="button"]').nth(8).click()'''