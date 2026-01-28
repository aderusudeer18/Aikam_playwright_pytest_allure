from playwright.sync_api import sync_playwright,expect 
import allure 
import pytest 
 

class AllApplicant:
    def __init__(self,page):
        self.page=page 

    
    def search_by_name(self,applicant_name):
        with allure.step("search by name or email,Phone number"):
            self.page.locator("div.cursor-pointer svg.lucide-search").click()
            self.page.wait_for_timeout(1000)
            search_name=self.page.locator('//input[@type="text"]').nth(1)
            search_name.type(applicant_name)
            result = self.page.locator(f"text={applicant_name}")
            if result.count() > 0:
                result.first
                allure.attach(
                    "Test case passed successfully:Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Applicant not found: {applicant_name}")

           
            

   
    def all_applicant(self, applicant_name):
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

        
    def download_excel_btn(self):
        with allure.step("verify the applicant is selected and able to click on Excel button"): 
            excel_sheet=self.page.wait_for_selector('//img[@alt="excel"]').click()
    
        with self.page.expect_download() as d:
            self.page.locator("//button[contains(text(),'Export')]").click()

        download = d.value  


        path = download.path() 

        save_path = fr"C:\Users\Sudeer\Downloads\{download.suggested_filename}"
        download.save_as(save_path)
        allure.attach(
                    "Test case passed successfully:Clicked on Export excel to download applicant details",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 


    def all_applicant(self, applicant_name):
        with allure.step(f"Select applicant: {applicant_name}"):

            found = False
            max_pages = 10

            for _ in range(max_pages):

                self.page.wait_for_load_state("networkidle")
                self.page.wait_for_timeout(2000)

                applicant = self.page.get_by_text(applicant_name, exact=True)

                if applicant.count() > 0:
                    applicant.first.scroll_into_view_if_needed()

                    app_box = applicant.first.bounding_box()
                    checkboxes = self.page.locator("input[type='checkbox']")

                    closest_checkbox = None
                    closest_distance = float("inf")

                    for i in range(checkboxes.count()):
                        box = checkboxes.nth(i).bounding_box()
                        if box:
                            distance = abs(box["y"] - app_box["y"])
                            if distance < closest_distance:
                                closest_distance = distance
                                closest_checkbox = checkboxes.nth(i)

                    if closest_checkbox:
                        closest_checkbox.scroll_into_view_if_needed()
                        closest_checkbox.click(force=True)
                        found = True
                        break

                # Handle Next button
                next_btn = self.page.get_by_text("Next")

                if next_btn.count() == 0:
                    break

                if not next_btn.is_enabled():
                    allure.attach(
                        self.page.screenshot(),
                        name="Next_Disabled_Applicant_Not_Found",
                        attachment_type=allure.attachment_type.PNG
                    )
                    assert False, f"Applicant '{applicant_name}' not found and Next is disabled"

                next_btn.scroll_into_view_if_needed()
                next_btn.click()
                self.page.wait_for_load_state("networkidle")

            
                assert False, f"Applicant '{applicant_name}' not found"


    def move_to_applicant_btn(self,applicant_name,timeout=3000):
        with allure.step("Verify move to button is visible "):
            move_to_btn=self.page.locator('//button[@role="combobox"]').nth(0)
            move_to_btn.click()
            pre_screen=self.page.get_by_role("option",name="Selected").click()
            skip=self.page.locator('//button[contains(text(),"Skip")]').click() 
            self.page.locator('//button[contains(text(),"Selected")]').click()
            selected_applicant = self.page.get_by_text(applicant_name)
            expect(selected_applicant.first).to_be_visible(timeout=1000) 
            self.page.reload()
            allure.attach(
                    "Test case passed successfully:Applicant is moved to stage",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)


    def sort_applicant(self,timeout=2000):
        with allure.step("Click on all applicants ribbon"):
            self.page.locator('//button[contains(text(),"All Applicants")]').click()
            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Name").click()
            self.page.get_by_text("A → Z", exact=True).click()
            self.page.reload()
            allure.attach(
                    "Test case passed successfully:sort applicants is applied to all applicants successfully",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 
            

    def advance_filters(self,skill_1,skill_2,skill_3,email_id,timeout=3000):
        with allure.step("Applying advance filters to applicants"):
            advance=self.page.locator('//div[@data-state="closed"]').nth(11).click()
            keyword = self.page.locator("//input[@type='text']").nth(1)
            keyword.type(skill_1)
            self.page.keyboard.press("Enter")
            keyword.type(skill_2)
            self.page.keyboard.press("Enter")
            keyword.type(skill_3)
            email=self.page.locator('//input[@placeholder="Search email..."]')
            email.type(email_id)

            apply=self.page.wait_for_selector("//button[contains(text(),'Apply')]").click()
            self.page.reload()
        
            allure.attach(
                    "Test case passed successfully:Advance filters has applied to all applicants and displayed ",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)  

    def re_set_changes(self,timeout=3000):
        with allure.step("reset your changes in the  advance filters "):
            advance=self.page.locator('//div[@data-state="closed"]').nth(11).click()
            reset_btn=self.page.locator('//button[contains(text(),"Reset Changes")]').click()
            apply=self.page.wait_for_selector("//button[contains(text(),'Apply')]").click() 
            self.page.reload()


            

    def search_by_name_to_delete(self,applicant_name,timeout=3000):
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
            )
            

           
            

   
    def applicant_to_delete(self, applicant_name):
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
            yes_cancle=self.page.locator('//button[@type="button"]').nth(8).click()

   





    





    


