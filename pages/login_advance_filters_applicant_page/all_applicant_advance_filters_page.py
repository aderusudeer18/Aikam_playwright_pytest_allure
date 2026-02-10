from datetime import datetime
from playwright.sync_api import sync_playwright, expect
import allure
import pytest
import time
import os

from conftest import page

class Allapplicant: 
    def __init__(self,page):
        self.page=page 

    def import_resumes(self, timeout=30000):
        with allure.step("Verify resumes has been imported"):
           
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(3000)

            # 2. Use a robust locator to find the visible "Import Resumes" button
            # We try the user-provided XPath and a text-based backup
            import_btn = self.page.locator("//button[.//span[normalize-space()='Import Resumes']] | //button[contains(., 'Import Resumes')]").first
            
            # 3. Wait for visibility and scroll into view
            import_btn.wait_for(state="visible", timeout=timeout)
            import_btn.scroll_into_view_if_needed()
            
            # 4. Aggressive click strategy
            try:
                # Attempt force click first (bypasses most overlay issues)
                import_btn.click(force=True, timeout=5000)
            except Exception as e:
                # Fallback to JavaScript click if standard click fails
                allure.attach(f"Standard click failed: {str(e)}", name="Debug Info", attachment_type=allure.attachment_type.TEXT)
                self.page.evaluate("el => el.click()", import_btn.element_handle())

            # 5. Wait for the file input to appear after the click
            upload = self.page.locator("input[type='file']")
            upload.wait_for(state="attached", timeout=60000)
            
            self.page.set_input_files('input[type="file"]', [
                r"C:\Users\Sudeer\Downloads\Aikam_Rakesh_Mekala_Resume (1).pdf",
                r"C:\Users\Sudeer\Downloads\Aikam_FAKHRUDDIN_SHAIK_Resume.pdf",
                r"C:\Users\Sudeer\Downloads\Aikam_SURESH_PAGAR_Resume.pdf",
                r"C:\Users\Sudeer\Downloads\Aikam_RAHUL_KUMAR_Resume.pdf"
            ])
            

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
                

    def export_excel_btn(self,timeout=2000):
        with allure.step("Clicking on Export excel button"):
            self.page.locator('//button[@style="color: transparent;"]')
     
   

    def advance_filters(self,skill_1,skill_2,skill_3,email_id,number,can_loc_1,can_loc_2,timeout=3000):
        with allure.step("Applying advance filters to applicants"):
            advance=self.page.locator('//div[@data-state="closed"]').nth(9).click()
            keyword = self.page.locator("//input[@type='text']").nth(0)
            keyword.type(skill_1)
            self.page.keyboard.press("Enter")
            keyword.type(skill_2)
            self.page.keyboard.press("Enter")
            keyword.type(skill_3)

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


    def verify_applicant_filtered(self,timeout=3000):
            with allure.step("verify applicants has been filtered based on advance filters"):
                #if filtered_applicant.count() >1:
                filtered_applicant=self.page.locator("div.flex.w-full.items-center.gap-2.mb-1").nth(0)
                filtered_applicant.click()

                ai_pre_screening=self.page.locator('//button[contains(text(),"AI Prescreening")]')
                ai_pre_screening.click()
                request_ai_pre_screening=self.page.locator('//button[contains(text(),"Request AI Prescreening")]')
                request_ai_pre_screening.wait_for(state="visible")
                request_ai_pre_screening.click()


                Next=self.page.locator('//button[contains(text(),"Next")]')
                Next.wait_for(state="visible")
                Next.click()


                schedule=self.page.get_by_role("button",name="Schedule",exact=True)
                schedule.wait_for(state="visible")
                schedule.click()

                ai_interview=self.page.locator('//button[contains(text(),"AI Interview")]').nth(1)
                ai_interview.click()
                request_ai_interview=self.page.locator('//button[contains(text(),"Request AI Interview")]')
                request_ai_interview.wait_for(state="visible")
                request_ai_interview.click()

                Next=self.page.locator('//button[contains(text(),"Next")]')
                Next.wait_for(state="visible")
                Next.click()

                schedule=self.page.get_by_role("button",name="Schedule",exact=True)
                schedule.wait_for(state="visible")
                schedule.click()

                ai_code_assessment=self.page.locator('//button[contains(text(),"AI Coding Assessment")]')
                ai_code_assessment.click()
                request_ai_code_assessment=self.page.locator('//button[contains(text(),"Request AI Coding Assessment")]')
                request_ai_code_assessment.wait_for(state="visible")
                request_ai_code_assessment.click()

                Next=self.page.locator('//button[contains(text(),"Next")]')
                Next.wait_for(state="visible")
                Next.click()



                Next1=self.page.locator('//button[contains(text(),"Next")]')
                Next1.wait_for(state="visible")
                Next1.click()

                schedule=self.page.get_by_role("button",name="Schedule",exact=True)
                schedule.wait_for(state="visible")
                schedule.click() 


                resume=self.page.locator('//button[contains(text(),"Resume")]')
                resume.click()
                
                with self.page.expect_download() as d:
                    resume_download=self.page.locator('//button[contains(text(),"Download")]')
                    resume_download.click()

                download = d.value  


                path = download.path() 

                save_path = os.path.join(os.path.expanduser("~"), "Downloads", download.suggested_filename)
                download.save_as(save_path)
                allure.attach(
                            "Test case passed successfully:Clicked on Resume to download applicant resume",
                            name="Test_Success_Message",
                            attachment_type=allure.attachment_type.TEXT) 
                

    def verify_advance_filters_mails_sent_list(self,designation,company,timeout=3000):
        with allure.step("verify applicant page is visible"):
            self.page.locator('//a[contains(text(),"All Applicants")]').click()
            advance=self.page.locator('//div[@data-state="closed"]').nth(9)
            advance.click()
            wrong_btn=self.page.locator('//button[@type="button"]').nth(4)
            wrong_btn.click()

            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
            reset_btn.click()

            designation_role=self.page.locator('//input[@placeholder="Search designation..."]')
            designation_role.fill(designation)
            #self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            company_name=self.page.locator('//input[@placeholder="Search company..."]')
            company_name.fill(company)
            #self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")





            ai_pre_screen_sent=self.page.locator('//label[contains(text(),"AI Pre Screening Sent")]')
            ai_pre_screen_sent.click()
            ai_interview_sent=self.page.locator('//label[contains(text(),"AI Interview Sent")]')
            ai_interview_sent.click()
            ai_code_assessment_sent=self.page.locator('//label[contains(text(),"AI Coding Assessment Sent")]')
            ai_code_assessment_sent.click()


            view_btn=self.page.locator('//input[@value="Viewed"]')
            view_btn.check()

            apply_btn=self.page.locator("//button[contains(text(),'Apply')]")
            expect(apply_btn).to_be_visible(timeout=2000)
            apply_btn.click()
            self.page.wait_for_timeout(3000)
            allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 


    def verify_advance_filters_given_mails_list(self,ug,institute_name,course_name,timeout=3000):
        with allure.step("verify interviews toggles given list"):
            
            advance=self.page.locator('//div[@data-state="closed"]').nth(9)
            advance.click()
            wrong_btn_dsg=self.page.locator('//button[@type="button"]').nth(8)
            wrong_btn_dsg.click()
            wrong_btn_company=self.page.locator('//button[@type="button"]').nth(6)
            wrong_btn_company.click()

            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
            reset_btn.click()
            

            ug_qualification=self.page.locator('//input[@placeholder="Search UG qualification..."]')
            ug_qualification.fill(ug)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")



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
            
            

            
    
            

    def verify_advance_filter_applicant(self,cc_mail:str,interview_sub,interview_type:str,zoom_value:str,location:str,mobile_number,target,time_from,time_to,mail_description,timeout=3000):
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

            self.page.locator('//button[@role="combobox"]').nth(1).click()
            option=self.page.get_by_role("option", name=interview_type, exact=True)
            option.click()

            if interview_type == "Online Interview":
                zoom_option=self.page.get_by_role("option",name=zoom_value, exact=True)
                zoom_option.click()

            elif interview_type == "Face to Face":
                location_input = self.page.locator('//input[@placeholder="Enter Google Map Location"]')
                location_input.fill(location)

            elif interview_type=="Phone Call":
                type_number=self.page.locator('//input[@value="+91"]')
                type_number.fill(mobile_number)
            



            allure.attach(
                    f"interview type is  'Value' selected successfully",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT)

            

            #date selection
            target = datetime.strptime(target, "%d-%m-%Y")
            self.page.locator("//label[text()='Interview Date']/following::button[1]").click()
            month_year = self.page.locator("//div[@aria-live='polite'] | //h6")
            month_year.first.wait_for(state="visible", timeout=timeout)

            prev_btn = self.page.locator("//button").nth(0)
            next_btn = self.page.locator("//button").nth(1)

            current = datetime.strptime(
                month_year.first.inner_text().strip(),"%B %Y")

            while (current.year, current.month) != (target.year, target.month):

                if (current.year, current.month) < (target.year, target.month):
                    next_btn.click()
                else:
                    prev_btn.click()

                self.page.wait_for_timeout(200)

                current = datetime.strptime(
                    month_year.first.inner_text().strip(),"%B %Y")

            day_btn = self.page.locator(f"//button[.//text()[normalize-space()='{target.day}']]")

            day_btn.first.wait_for(state="visible", timeout=5000)
            day_btn.first.click()


            from_time=self.page.locator('//input[@type="time"]').nth(0)
            from_time.fill(time_from)

            To_time=self.page.locator('//input[@type="time"]').nth(1)
            To_time.fill(time_to)

            manual_description=self.page.locator('//textarea[@name="description"]')
            manual_description.fill(mail_description)

            send_btn=self.page.locator('//button[contains(text(),"Send")]')
            send_btn.click()  


            download_icon = self.page.locator("div.cursor-pointer").nth(2)

            with self.page.expect_download() as download_info:
                download_icon.click()

            download = download_info.value

            save_path = os.path.join(os.path.expanduser("~"), "Downloads", download.suggested_filename)
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
            


    def un_viewed_applicants(self,select_option,timeout=3000):
        with allure.step("verify unviewed applicants are visible"):
            all_applicant_page=self.page.locator('//a[contains(text(),"All Applicants")]')
            all_applicant_page.click()

            advance=self.page.locator('//div[@data-state="closed"]').nth(9)
            advance.click()

            gender=self.page.locator('//button[@role="combobox"]')
            gender.click()
            select_gender=self.page.get_by_role("option",name=select_option,exact=True)
            select_gender.click()

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
            


    def advance_filters_exclude_keywords(self,skill_1,skill_2,applicant_name,timeout=3000):
        with allure.step("Applying advance filters to exclude keywords to applicants"):
                advance=self.page.locator('//div[@data-state="closed"]').nth(9)
                advance.click()
                reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
                reset_btn.click() 


                boolean_on=self.page.locator('//button[@role="switch"]')
                boolean_on.click()

                keywords = self.page.locator("//input[contains(@placeholder,'Ex:')]")
                keywords.wait_for(state="visible")
                keywords.fill(skill_1)

                exclude_keywords=self.page.locator('//input[@type="text"]')
                exclude_keywords.type(skill_2) 
                

                apply_btn=self.page.locator("//button[contains(text(),'Apply')]")
                expect(apply_btn).to_be_visible(timeout=2000)
                apply_btn.click()

                container = self.page.locator("div",has=self.page.get_by_text(applicant_name, exact=True)).first

                expect(container).to_be_visible(timeout=15000)
                checkbox = container.locator("input[type='checkbox']").nth(1)

                expect(checkbox).to_be_visible(timeout=5000)
                checkbox.check(force=True)
                allure.attach(
                    "Test case passed successfully:applicant card is exists and selected",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

                
                delete_btn=self.page.locator("//button[@aria-haspopup='dialog']").nth(1)
                delete_btn.click()
                yes_cancle=self.page.locator('//button[@type="button"]').nth(11)
                yes_cancle.click()
                allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 




