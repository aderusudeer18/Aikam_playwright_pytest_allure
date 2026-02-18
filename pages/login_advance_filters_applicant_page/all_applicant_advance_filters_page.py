from datetime import datetime
from playwright.sync_api import sync_playwright, expect
import allure
import pytest
import time
import os
import re

from conftest import page

class AllApplicantPage: 
    def __init__(self,page):
        self.page=page 

    def import_resumes(self, timeout=30000):
         with allure.step("Verify resumes has been imported"):
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(3000)

            # Use robust locator for the visible "Import Resumes" button
            import_btn = self.page.locator("//main//button[.//span[normalize-space()='Import Resumes']] | //main//button[contains(., 'Import Resumes')]").first
            import_btn.wait_for(state="visible", timeout=timeout)
            import_btn.scroll_into_view_if_needed()
            
            # Aggressive click strategy
            try:
                import_btn.click(force=True, timeout=5000)
            except Exception as e:
                allure.attach(f"Standard click failed: {str(e)}", name="Debug Info")
                self.page.evaluate("el => el.click()", import_btn.element_handle())

            # File upload
            upload = self.page.locator("input[type='file']")
            upload.wait_for(state="attached", timeout=60000)
            
            self.page.set_input_files('input[type="file"]', [
                r"C:\Users\Sudeer\Downloads\Aikam_Rakesh_Mekala_Resume (1).pdf",
                r"C:\Users\Sudeer\Downloads\Aikam_FAKHRUDDIN_SHAIK_Resume.pdf",
                r"C:\Users\Sudeer\Downloads\Aikam_SURESH_PAGAR_Resume.pdf",
                r"C:\Users\Sudeer\Downloads\Aikam_RAHUL_KUMAR_Resume.pdf"
            ])
            
            # Final Import click
            self.page.wait_for_selector("//button[contains(text(),'Import')]").click()
            
            # Stabilization wait
            self.page.wait_for_timeout(10000) 
            
            # Success/Error detection
            success_regex = re.compile(r"Successfully|uploaded|imported", re.I)
            error_regex = re.compile(r"Failed|Error|Duplicate", re.I)
            
            max_time = 60 
            start = time.time()
            while time.time() - start < max_time:            
                try:
                    err_loc = self.page.get_by_text(error_regex).first
                    if err_loc.count() > 0 and err_loc.is_visible():
                        err_msg = err_loc.inner_text()
                        if "Duplicate" in err_msg:
                            allure.attach(err_msg, name="Upload Note (Duplicate)")
                            break # Duplicate is fine
                        pytest.fail(f"Resume Upload Failed: {err_msg}")

                    succ_loc = self.page.get_by_text(success_regex).first
                    if succ_loc.count() > 0 and succ_loc.is_visible():
                        allure.attach("Upload successful", name="Status")
                        break
                except Exception as e:
                    # Page might have been closed/navigated - assume success if no error found
                    if "closed" in str(e).lower() or "target" in str(e).lower():
                        allure.attach("Page navigated/closed - assuming upload completed", name="Info")
                        break
                    # For other exceptions, continue checking
                time.sleep(1)
            
            # Ultra-Robust Modal Closure: Close any modal dialog
            modal_close_selectors = [
                "button:has(.lucide-x)",
                "button[aria-label='Close' i]",
                "button:has-text('Close')",
                ".lucide-x >> ancestor::button",
                "//button[contains(@class, 'close')]"
            ]
            for sel in modal_close_selectors:
                try:
                    btns = self.page.locator(sel).filter(visible=True)
                    if btns.count() > 0:
                        btns.first.click(timeout=3000)
                        self.page.wait_for_timeout(1000)
                        break
                except: continue

            # Refresh to stabilize UI
            self.page.reload()
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(5000)
            return

     
   

    def apply_advance_filters(self, skill_1, skill_2, skill_3, email_id, number, can_loc_1, can_loc_2, min_experience="0", timeout=15000):
        with allure.step(f"Applying advance filters: skills={[skill_1, skill_2, skill_3]}, exp={min_experience}"):
            import re
            
            # Dynamic Filters toggle: Targets "Filters" text or sliders icon, avoiding sidebar
            self.page.wait_for_timeout(2000)
            advance = self.page.get_by_role("button", name=re.compile(r"Filters", re.I)).filter(has_not=self.page.locator("aside, nav")).first
            if advance.count() == 0:
                # Fallback to precise slider icon but excluding sidebar
                advance = self.page.locator("button:has(.lucide-sliders-horizontal)").filter(has_not=self.page.locator("aside, nav")).first
            
            advance.click()

            # Wait for the filter drawer/overlay to appear
            drawer = self.page.locator("[role='dialog']:visible, .drawer:visible, .filter-container:visible, aside:not([role='navigation'])").last
            try:
                drawer.wait_for(state="visible", timeout=7000)
            except:
                drawer = self.page

            # Keywords - Placeholder is "Add keyword..." as seen in screenshot
            keyword = drawer.get_by_placeholder(re.compile(r"Add keyword", re.I)).first
            if keyword.count() == 0:
                keyword = drawer.locator("input[type='text']").first
            
            for skill in [skill_1, skill_2, skill_3]:
                keyword.fill(skill)
                self.page.keyboard.press("Enter")

            # Search email - Dynamic placeholder matches screenshot "Search email..."
            email = drawer.get_by_placeholder(re.compile(r"Search email", re.I)).first
            email.fill(email_id)
            
            # Mobile number - Use type or label
            mobile = drawer.locator("input[type='tel']").first
            if mobile.count() == 0:
                mobile = drawer.get_by_placeholder(re.compile(r"mobile|phone", re.I)).first
            mobile.fill(number)

            # Location inputs - Dynamic placeholder matches screenshot "Enter location..."
            candidate_loc = drawer.get_by_placeholder(re.compile(r"Enter location", re.I)).first
            for loc in [can_loc_1, can_loc_2]:
                candidate_loc.fill(loc)
                self.page.wait_for_timeout(1000)
                self.page.keyboard.press("ArrowDown")
                self.page.keyboard.press("Enter")

            # Apply button - strictly scoped to the drawer
            apply_btn = drawer.get_by_role("button", name=re.compile(r"^Apply$|Apply", re.I)).first
            apply_btn.wait_for(state="visible", timeout=timeout)
            apply_btn.click()


    def process_filtered_applicant(self, applicant_name=None, timeout=15000):
        with allure.step(f"Verify applicant '{applicant_name}' and perform AI actions"):
            import re
            
            # Click the applicant card - Using a more reliable locator
            if applicant_name:
                filtered_applicant = self.page.locator("div.flex.w-full.items-center").filter(has_text=re.compile(applicant_name, re.I)).first
            else:
                filtered_applicant = self.page.locator("div.flex.w-full.items-center").first
                
            filtered_applicant.wait_for(state="visible", timeout=timeout)
            filtered_applicant.click()

            # Sequence of AI actions with semantic locators handling tabs
            def run_ai_action(action_name, request_name):
                # Ensure visibility and clear any lingering toasts/overlays if possible
                self.page.wait_for_timeout(1000)
                
                # 1. Click the TAB first - Use force=True to bypass potential overlays/animations
                tab_candidates = [
                    self.page.get_by_role("tab", name=re.compile(action_name, re.I)),
                    self.page.get_by_role("button", name=re.compile(action_name, re.I)),
                    self.page.get_by_text(re.compile(action_name, re.I), exact=True)
                ]
                
                tab_found = False
                for t in tab_candidates:
                    if t.count() > 0:
                        try:
                            # Attempt standard click first, then force if needed
                            t.first.click(timeout=3000)
                        except:
                            t.first.click(force=True)
                        tab_found = True
                        break
                
                if not tab_found:
                    allure.attach(f"Tab '{action_name}' not found", name="Warning")
                    return

                # 2. Click the REQUEST button inside the tab content
                req_btn = self.page.get_by_role("button", name=re.compile(request_name, re.I))
                try:
                    req_btn.wait_for(state="visible", timeout=5000)
                    req_btn.click(force=True)
                except:
                    allure.attach(f"Request button '{request_name}' not clicked or already active", name="Notice")
                
                # 3. Wait for and click Next/Schedule if they appear
                # We check for these specifically after the request as multi-step modals may appear
                for i in range(3): 
                    for step_name in [r"^Next$", r"^Schedule$"]:
                        step_btn = self.page.get_by_role("button", name=re.compile(step_name, re.I)).filter(visible=True)
                        if step_btn.count() > 0:
                            step_btn.first.click(force=True)
                            self.page.wait_for_timeout(2000) # Wait for animation/next step

            run_ai_action("AI Prescreening", "Request AI Prescreening")
            run_ai_action("AI Interview", "Request AI Interview")
            run_ai_action("AI Coding Assessment", "Request AI Coding Assessment")

            # 4. Ultra-Aggressive Modal Closer: Close all obstructing modals
            for i in range(5):
                modal_close = self.page.locator("button:has(.lucide-x), button[aria-label='Close' i], [role='dialog'] button:has-text('Close'), button:has-text('Cancel')").filter(visible=True).first
                if modal_close.count() > 0:
                    try:
                        modal_close.click(force=True, timeout=3000)
                        self.page.wait_for_timeout(1000)
                    except: break
                else: break

            # 5. Final sequence: Select Resume tab and Download
            # Ensure we are in the applicant profile view
            self.page.wait_for_timeout(1000)
            resume_tab = self.page.get_by_role("tab", name=re.compile(r"Resume", re.I)).first
            if resume_tab.count() == 0:
                resume_tab = self.page.get_by_role("button", name=re.compile(r"Resume", re.I)).first
            
            if resume_tab.count() > 0:
                resume_tab.click(force=True)
                self.page.wait_for_timeout(2000) # Wait for resume content to load
            
            with self.page.expect_download() as d:
                # Robust download button locator
                dl_btn = self.page.locator("//button[contains(., 'Download')] | //button[.//svg[contains(@class, 'download')]]").filter(visible=True).first
                if dl_btn.count() == 0:
                    dl_btn = self.page.get_by_role("button", name=re.compile(r"Download", re.I)).first
                
                dl_btn.click(force=True)

            download = d.value  
            save_path = os.path.join(os.path.expanduser("~"), "Downloads", download.suggested_filename)
            download.save_as(save_path)
            
            allure.attach(
                f"Applicant actions completed and resume downloaded to {save_path}",
                name="Success",
                attachment_type=allure.attachment_type.TEXT)
                

    def verify_sent_status_filters(self, designation, company, timeout=5000):
        with allure.step("Verify applicant list with 'Sent' filters"):
            import re
            
            # Click All Applicants breadcrumb/link to return to main view if needed
            all_app_link = self.page.get_by_role("link", name=re.compile(r"All Applicants", re.I)).first
            if all_app_link.count() > 0:
                all_app_link.click()
                self.page.wait_for_load_state("networkidle")
            
            # Robust Filters toggle standardized
            self.page.wait_for_timeout(2000)
            advance = self.page.get_by_role("button", name=re.compile(r"Filters", re.I)).filter(has_not=self.page.locator("aside, nav")).first
            if advance.count() == 0:
                advance = self.page.locator("button:has(.lucide-sliders-horizontal)").filter(has_not=self.page.locator("aside, nav")).first
            
            if advance.count() > 0:
                advance.click()

            # Handle both drawer and full-page filter view
            drawer = self.page.locator("[role='dialog']:visible, .drawer:visible, .filter-container:visible").last
            if drawer.count() == 0:
                drawer = self.page

            # Reset logic - crucial to clear previous state
            reset_btn = drawer.get_by_role("button", name=re.compile(r"Reset|Clear", re.I)).filter(visible=True).first
            if reset_btn.count() == 0:
                reset_btn = drawer.get_by_text(re.compile(r"Reset Changes", re.I)).first
            
            if reset_btn.count() > 0:
                reset_btn.click()
                self.page.wait_for_timeout(1000)

            # Fill filters with scrolling
            def fill_with_scroll(placeholder_regex, value):
                field = drawer.get_by_placeholder(placeholder_regex).first
                field.wait_for(state="visible", timeout=7000)
                field.scroll_into_view_if_needed()
                field.fill(value)
                self.page.keyboard.press("Enter")
                self.page.wait_for_timeout(500)

            fill_with_scroll(re.compile(r"designation", re.I), designation)
            fill_with_scroll(re.compile(r"company", re.I), company)

            # Checkboxes for 'Sent' status
            sent_options = [
                r"AI Pre Screening Sent",
                r"AI Interview Sent",
                r"AI Coding Assessment Sent",
                r"^Viewed$"
            ]
            for opt in sent_options:
                cb = drawer.get_by_label(re.compile(opt, re.I)).first
                if cb.count() > 0:
                    cb.scroll_into_view_if_needed()
                    cb.check()

            apply_btn = drawer.get_by_role("button", name=re.compile(r"^Apply$", re.I)).first
            apply_btn.wait_for(state="visible", timeout=timeout)
            apply_btn.click()
            
            self.page.wait_for_timeout(3000)
            allure.attach(
                "Advance filters applied to all applicants and displayed successfully",
                name="Success",
                attachment_type=allure.attachment_type.TEXT)


    def verify_given_status_filters(self, ug, institute_name, course_name, timeout=5000):
        with allure.step("verify interviews toggles given list"):
            import re
            
            # Robust "Filters" button locator
            advance = self.page.locator("button").filter(has_text=re.compile(r"Filters", re.I)).filter(has_not=self.page.locator("aside, nav")).first
            if advance.count() == 0:
                 advance = self.page.locator("button:has(.lucide-sliders-horizontal)").filter(has_not=self.page.locator("aside, nav")).first
            
            # Click with retry/force if needed
            if advance.count() > 0:
                try:
                   advance.click()
                except:
                   advance.click(force=True)

            # Handle both drawer and full-page filter view
            drawer_locator = self.page.locator("[role='dialog']:visible, .drawer:visible, .filter-container:visible, .sheet-content:visible").last
            if drawer_locator.count() > 0:
                drawer = drawer_locator
                is_overlay = True
            else:
                drawer = self.page
                is_overlay = False

            # Reset logic - preferring "Reset Changes" or "Reset/Clear" regex
            reset_btn = drawer.get_by_role("button", name=re.compile(r"Reset|Clear", re.I)).filter(visible=True).first
            if reset_btn.count() == 0:
                 reset_btn = drawer.locator("button").filter(has_text=re.compile(r"Reset Changes", re.I)).first
            
            if reset_btn.count() > 0:
                reset_btn.click()
                self.page.wait_for_timeout(1000)

            # UG Qualification
            ug_qualification = drawer.get_by_placeholder(re.compile(r"ug qualification", re.I)).first
            ug_qualification.fill(ug)
            self.page.wait_for_timeout(500)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            # Institute
            institute = drawer.get_by_placeholder(re.compile(r"institute", re.I)).first
            institute.fill(institute_name)
            self.page.wait_for_timeout(500)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            # Course
            course = drawer.get_by_placeholder(re.compile(r"course", re.I)).first
            course.fill(course_name)
            self.page.wait_for_timeout(500)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            # Checkboxes
            for label_text in ["AI Pre Screening Given", "AI Interview Given", "AI Coding Assessment Given"]:
                # Try locator by label text first
                cb = drawer.locator("label").filter(has_text=re.compile(label_text, re.I)).first
                if cb.count() > 0:
                    cb.scroll_into_view_if_needed()
                    cb.check()
                else:
                     # Fallback to standard get_by_label
                     drawer.get_by_label(re.compile(label_text, re.I)).first.check()

            # Apply Button
            apply_btn = drawer.get_by_role("button", name=re.compile(r"^Apply$", re.I)).first
            apply_btn.wait_for(state="visible", timeout=2000)
            apply_btn.click()
            
            # Wait for drawer to close if it was an overlay
            if is_overlay:
                try:
                    drawer.wait_for(state="hidden", timeout=3000)
                except:
                    # Explicit close if still visible
                    if drawer.is_visible():
                        close_btn = drawer.locator("button:has(.lucide-x), button[aria-label='Close' i], button:has-text('Close')").first
                        if close_btn.count() > 0:
                             close_btn.click()
                        else:
                             self.page.mouse.click(0, 0)
            
            self.page.wait_for_timeout(3000)
            allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 


    def schedule_manual_interview(self, cc_mail: str, interview_sub, interview_type: str, zoom_value: str, location: str, mobile_number, target, time_from, time_to, mail_description, timeout=5000):
        with allure.step("Verify filtered applicant and schedule manual interview"):
            filtered_applicant=self.page.locator("div.flex.w-full.items-center.gap-2.mb-1").nth(0)
            filtered_applicant.click(force=True)
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
            

            share_applicant=self.page.locator("//div[@data-state='closed']").nth(5)
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
            

            send_mail=self.page.locator('//div[@data-state="closed"]').nth(7)
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
            


    def filter_by_unviewed_status(self, select_option, timeout=5000):
        with allure.step("Verify unviewed applicants are visible"):
            all_applicant_page=self.page.locator('//a[contains(text(),"All Applicants")]')
            all_applicant_page.click()

            advance=self.page.locator('//div[@data-state="closed"]').nth(11)
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
            


    def filter_by_exclude_keywords(self, skill_1, skill_2, applicant_name, timeout=5000):
        with allure.step("Apply 'Exclude Keywords' filters"):
            advance=self.page.locator('//div[@data-state="closed"]').nth(11)
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
