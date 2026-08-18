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
            import_btn = self.page.locator("//button[.//span[normalize-space()='Import Resumes']] | //button[contains(., 'Import Resumes')]").first
            import_btn.wait_for(state="visible", timeout=timeout)
            import_btn.scroll_into_view_if_needed()
            
            try:
                import_btn.click(force=True, timeout=5000)
            except Exception as e:
                allure.attach(f"Standard click failed: {str(e)}", name="Debug Info", attachment_type=allure.attachment_type.TEXT)
                self.page.evaluate("el => el.click()", import_btn.element_handle())
            upload = self.page.locator("input[type='file']")
            upload.wait_for(state="attached", timeout=60000)
            
            self.page.set_input_files('input[type="file"]', [
                r"c:\Users\Sudeer\Downloads\Aikam_K_ASHOK_KUMAR_Resume.pdf",
                r"c:\Users\Sudeer\Downloads\Aikam_Babu_Rao_.K_Resume.pdf",
                r"c:\Users\Sudeer\Downloads\Aikam_T._KIRAN_Resume.pdf",
                r"c:\Users\Sudeer\Downloads\Aikam_A.Balaji_Resume.pdf"
            ])
            

            # The button text in the modal might have changed (e.g., to 'Upload' or have different spacing).
            # This robust locator looks for Import or Upload and picks the last one (the modal button).
            modal_import_btn = self.page.locator("button:has-text('Import'), button:has-text('Upload')").last
            modal_import_btn.wait_for(state="visible", timeout=10000)
            modal_import_btn.click()

            # Wait for either the success or error toast using XPath OR
            toast = self.page.locator("//p[contains(text(),'resumes have been successfully imported')] | //h3[contains(text(),'Resume Upload Failed')]").first
            
            success_toast = self.page.locator("//p[contains(text(),'resumes have been successfully imported')]").first
            error_toast = self.page.locator("//h3[contains(text(),'Resume Upload Failed')]").first
            max_time = 180 
            start = time.time()
            while time.time() - start < max_time:            
                if error_toast.count() > 0 and error_toast.is_visible():
                    allure.attach(
                        f"Resume Upload Toast shown: {error_toast.inner_text()}. Proceeding since resumes may already be imported.",
                        name="Upload Info",
                        attachment_type=allure.attachment_type.TEXT)
                    
                    screenshot_bytes = self.page.screenshot()
                    allure.attach(screenshot_bytes, name="Resume_Upload_Error_Screenshot", attachment_type=allure.attachment_type.PNG)

                    self.page.reload()
                    return

                if success_toast.count() > 0 and success_toast.is_visible():
                    allure.attach(
                        success_toast.inner_text(),
                        name="Upload Success",
                        attachment_type=allure.attachment_type.TEXT)
                    self.page.wait_for_timeout(3000)
                    self.page.reload()
                    return  
            self.page.reload()

    def export_excel_btn(self,timeout=5000):
        with allure.step("Clicking on Export excel button"):
            all_applicant_checkbox=self.page.locator('//input[@type="checkbox"]').first
            all_applicant_checkbox.check()

            excel_sheet_btn=self.page.locator('//img[@alt="excel"]').first
            expect(excel_sheet_btn).to_be_visible(timeout=timeout)
            excel_sheet_btn.click()
            
            try:
                export_btn = self.page.locator("//button[contains(text(),'Export')]").first
                export_btn.wait_for(state="visible", timeout=3000)
                with self.page.expect_download(timeout=5000) as d:
                    export_btn.click()
                download = d.value
                save_path = os.path.join(os.path.expanduser("~"), "Downloads", download.suggested_filename)
                download.save_as(save_path)
                allure.attach(
                    "Test case passed successfully: Excel exported and downloaded",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(f"Excel export click/download did not complete: {str(e)}", name="Debug Info", attachment_type=allure.attachment_type.TEXT)
                # Take screenshot manually
                screenshot_bytes = self.page.screenshot()
                allure.attach(screenshot_bytes, name="Export_Excel_Failure_Screenshot", attachment_type=allure.attachment_type.PNG)
                pytest.fail(f"Excel export failed: {str(e)}")
            

     
   

    def advance_filters(self,skill_1,skill_2,skill_3,email_id,number,can_loc_1,can_loc_2,timeout=3000):
        with allure.step("Applying advance filters to applicants"):
            # Ensure at least one applicant is loaded/visible before opening filters
            self.page.locator("div.flex.items-center.gap-2").first.wait_for(state="visible", timeout=20000)
            
            advance=self.page.locator('button.border-gray-300.rounded-lg.shadow-sm').filter(has=self.page.locator('svg.lucide-sliders-horizontal')).first
            advance.click()
            self.page.wait_for_timeout(5000)
            keyword = self.page.get_by_placeholder("Add keywords...")
            keyword.click()
            self.page.keyboard.type(skill_1)
            self.page.keyboard.press("Enter")
            self.page.keyboard.type(skill_2)
            self.page.keyboard.press("Enter")
            self.page.keyboard.type(skill_3)
            self.page.keyboard.press("Enter")

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

            apply_btn=self.page.locator("//button[contains(text(),'Apply')]").last
            apply_btn.wait_for(state="visible", timeout=5000)
            try:
                apply_btn.click(timeout=5000)
            except Exception:
                self.page.evaluate("el => el.click()", apply_btn.element_handle())
            self.page.locator("div.flex.items-center.gap-2").first.wait_for(state="visible", timeout=20000)
            allure.attach(
                "Test case passed successfully: Advance filters applied",
                name="Test_Success_Message",
                attachment_type=allure.attachment_type.TEXT)


    def verify_applicant_filtered(self, applicant_name, timeout=20000):
            with allure.step(f"verify applicants has been filtered based on advance filters for {applicant_name}"):
                self.page.wait_for_timeout(2000)
                applicant_card = self.page.locator("h3", has_text=applicant_name).first
                try:
                    applicant_card.wait_for(state="visible", timeout=timeout)
                except Exception as e:
                    # Debugging: Print all applicant names currently on the screen
                    all_names = self.page.locator("h3").all_text_contents()
                    
                    raise AssertionError(f"Could not find applicant '{applicant_name}'. Found these instead: {all_names}") from e
                
                applicant_card.click()

                # AI Prescreening
                ai_pre_screening = self.page.locator("//button[.//span[text()='Prescreening']]")
                ai_pre_screening.click()
                request_ai_pre_screening = self.page.locator("//button[contains(text(),'Request Prescreening')]")
                self.page.wait_for_timeout(2000)
                if request_ai_pre_screening.is_visible():
                    request_ai_pre_screening.click()

                    Next = self.page.locator("//button[contains(text(),'Next')]")
                    Next.wait_for(state="visible")
                    Next.scroll_into_view_if_needed()
                    self.page.wait_for_timeout(2000)
                    Next.click(force=True)

                    self.page.wait_for_timeout(2000)
                    schedule = self.page.get_by_role("button", name="Schedule", exact=True)
                    if not schedule.is_visible():
                        Next.wait_for(state="visible")
                        Next.scroll_into_view_if_needed()
                        self.page.wait_for_timeout(2000)
                        Next.click(force=True)

                    schedule.wait_for(state="visible")
                    schedule.scroll_into_view_if_needed()
                    schedule.click()

                # Interview
                interview_tab = self.page.locator("//button[.//span[text()='Interview']]")
                interview_tab.wait_for(state="visible")
                interview_tab.click()
                request_ai_interview = self.page.locator("//button[contains(text(),'Request') and contains(text(),'Interview')]")
                self.page.wait_for_timeout(2000)
                if request_ai_interview.is_visible():
                    request_ai_interview.click()

                    Next = self.page.locator("//button[contains(text(),'Next')]")
                    Next.wait_for(state="visible")
                    Next.scroll_into_view_if_needed()
                    self.page.wait_for_timeout(2000)
                    Next.click(force=True)

                    self.page.wait_for_timeout(2000)
                    schedule = self.page.get_by_role("button", name="Schedule", exact=True)
                    if not schedule.is_visible():
                        Next.wait_for(state="visible")
                        Next.scroll_into_view_if_needed()
                        self.page.wait_for_timeout(2000)
                        Next.click(force=True)

                    schedule.wait_for(state="visible")
                    schedule.scroll_into_view_if_needed()
                    schedule.click()

                # Coding Assessment
                ai_code_assessment = self.page.locator("//button[.//span[text()='Coding Assessment']]")
                ai_code_assessment.click()
                request_ai_code_assessment = self.page.locator("//button[contains(text(),'Request Coding Assessment')]")
                self.page.wait_for_timeout(2000)
                if request_ai_code_assessment.is_visible():
                    request_ai_code_assessment.click()

                    Next = self.page.locator("//button[contains(text(),'Next')]").click()
                    Next_btn=self.page.locator('//button[contains(text(),"Next")]').click()
                    schedule = self.page.get_by_role("button", name="Schedule", exact=True)
                    
            

                    schedule.wait_for(state="visible")
                    schedule.scroll_into_view_if_needed()
                    schedule.click() 

                allure.attach(
                    "Test case passed successfully: AI Prescreening, Interview, and Coding Assessment requested",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)

                resume = self.page.locator("//button[.//span[text()='Resume']]")
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
            reset_btn=self.page.locator('//span[contains(text(),"Reset Filters")]')
            if reset_btn.is_visible():
                reset_btn.click()
            
            advance=self.page.locator('button.border-gray-300.rounded-lg.shadow-sm').filter(has=self.page.locator('svg.lucide-sliders-horizontal')).first
            advance.wait_for(state="visible", timeout=10000)
            advance.click()
            # wrong_btn=self.page.locator('//button[@type="button"]').nth(4)
            # wrong_btn.click()

            # reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
            # reset_btn.click()

            designation_role=self.page.locator('//input[@placeholder="Search designation..."]')
            designation_role.click()
            self.page.keyboard.type(designation, delay=50)
            self.page.wait_for_timeout(6000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(2000)
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(2000)

            company_name=self.page.locator('//input[@placeholder="Search company..."]')
            company_name.click()
            self.page.keyboard.type(company, delay=50)
            self.page.wait_for_timeout(6000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(2000)
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(2000)

            ai_pre_screen_sent=self.page.locator('//label[contains(text(),"AI Pre Screening Sent")]')
            ai_pre_screen_sent.click()
            ai_interview_sent=self.page.locator('//label[contains(text(),"AI Interview Sent")]')
            ai_interview_sent.click()
            ai_code_assessment_sent=self.page.locator('//label[contains(text(),"AI Coding Assessment Sent")]')
            ai_code_assessment_sent.click()


            un_view_btn=self.page.locator('//input[@value="Viewed"]')
            un_view_btn.check()
            self.page.wait_for_timeout(3000)
            apply_btn=self.page.locator("//button[contains(text(),'Apply')]").last
            apply_btn.wait_for(state="visible", timeout=5000)
            try:
                apply_btn.click(timeout=5000)
            except Exception:
                self.page.evaluate("el => el.click()", apply_btn.element_handle())
            self.page.wait_for_timeout(3000)
            allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 


    def verify_advance_filters_given_mails_list(self,ug,institute_name,course_name,timeout=3000):
        with allure.step("verify interviews toggles given list"):
            
            try:
                self.page.locator('//a[contains(text(),"All Applicants")]').first.click(timeout=3000)
            except Exception:
                pass
            self.page.wait_for_timeout(2000)
            advance=self.page.locator('button.border-gray-300.rounded-lg.shadow-sm').filter(has=self.page.locator('svg.lucide-sliders-horizontal')).first
            advance.click()
            wrong_btn_dsg=self.page.locator('//button[@type="button"]').nth(8)
            wrong_btn_dsg.click()
            wrong_btn_company=self.page.locator('//button[@type="button"]').nth(6)
            wrong_btn_company.click()

            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
            reset_btn.click()
            

            ug_qualification=self.page.locator('//input[@placeholder="Search UG qualification..."]')
            ug_qualification.click()
            self.page.keyboard.type(ug, delay=50)
            self.page.wait_for_timeout(6000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(500)
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(1000)

            institute=self.page.locator('//input[@placeholder="Search institute..."]')
            institute.click()
            self.page.keyboard.type(institute_name, delay=100)
            self.page.wait_for_timeout(6000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(2000)
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(2000)

            course=self.page.locator('//input[@placeholder="Search course..."]')
            course.click()
            self.page.keyboard.type(course_name, delay=50)
            self.page.wait_for_timeout(6000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(500)
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(1000)

            ai_pre_screen_given=self.page.locator('//label[contains(text(),"AI Pre Screening Given")]')
            ai_pre_screen_given.check()
            ai_interview_given=self.page.locator('//label[contains(text(),"AI Interview Given")]')
            ai_interview_given.check()
            ai_code_assessment_given=self.page.locator('//label[contains(text(),"AI Coding Assessment Given")]')
            ai_code_assessment_given.check() 
            apply_btn=self.page.locator("//button[contains(text(),'Apply')]").last
            apply_btn.wait_for(state="visible", timeout=5000)
            try:
                apply_btn.click(timeout=5000)
            except Exception:
                self.page.evaluate("el => el.click()", apply_btn.element_handle())

            
            self.page.wait_for_timeout(3000)
            allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)  
            

    def verify_advance_filter_applicant(self,cc_mail:str,interview_sub,interview_type:str,zoom_value:str,location:str,mobile_number,target,time_from,time_to,mail_description,timeout=3000):
        with allure.step("verify applicants has been filtered based on advance filters"):
            filtered_applicant=self.page.locator("h3.font-semibold.text-gray-900.text-primary.truncate").first
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
            

            share_applicant=self.page.locator('button:has(svg.lucide-send), div:has(svg.lucide-send)').first
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
            

            send_mail=self.page.locator('button:has(svg.lucide-mail), div:has(svg.lucide-mail)').first
            send_mail.click()
            offer_mail=self.page.locator('//button[contains(text(),"Offer")]')
            offer_mail.click()
            send_btn=self.page.locator("//button[contains(text(),'Send Email')]")
            expect(send_btn).to_be_visible(timeout=3000)   
            send_btn.click()
            allure.attach(
                    "Test case passed successfully: Email sent successfully",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            


    def un_viewed_applicants(self,select_option,timeout=3000):
        with allure.step("verify unviewed applicants are visible"):
            all_applicant_page=self.page.locator('//a[contains(text(),"All Applicants")]')
            all_applicant_page.click()

            advance=self.page.locator('button.border-gray-300.rounded-lg.shadow-sm').filter(has=self.page.locator('svg.lucide-sliders-horizontal')).first
            advance.click()

            gender=self.page.locator('//button[@role="combobox"]')
            gender.click()
            select_gender=self.page.get_by_role("option",name=select_option,exact=True)
            select_gender.click()

            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]')
            reset_btn.click()
            unviewed_btn=self.page.locator('//label[contains(text(),"Unviewed")]')
            unviewed_btn.check()
            # Wait for the DOM to settle after input changes
            self.page.wait_for_timeout(1500)
            apply_btn=self.page.locator("//button[contains(text(),'Apply')]").last
            
            # Wait for apply button to be visible and click with force
            apply_btn.wait_for(state="visible", timeout=5000)
            try:
                apply_btn.click(timeout=5000)
            except Exception:
                self.page.evaluate("el => el.click()", apply_btn.element_handle())
            
            allure.attach(
                    "Test case passed successfully:Unviewed applicants are visible ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            


    def advance_filters_exclude_keywords(self,skill_1,skill_2,applicant_name,timeout=3000):
        with allure.step("Applying advance filters to exclude keywords to applicants"):
                advance=self.page.locator('button.border-gray-300.rounded-lg.shadow-sm').filter(has=self.page.locator('svg.lucide-sliders-horizontal')).first
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
                

                # Wait for the DOM to settle after input changes
                self.page.wait_for_timeout(1500)
                apply_btn=self.page.locator("//button[contains(text(),'Apply')]").last
                expect(apply_btn).to_be_visible(timeout=5000)
                try:
                    apply_btn.click()
                except Exception:
                    self.page.evaluate("el => el.click()", apply_btn.element_handle())

                container = self.page.locator("div",has=self.page.get_by_text(applicant_name, exact=False)).first

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




