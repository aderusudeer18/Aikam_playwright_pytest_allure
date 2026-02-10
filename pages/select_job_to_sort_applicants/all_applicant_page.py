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
            search_name=self.page.locator('//input[@type="text"]')
            search_name.fill(applicant_name)
            result = self.page.locator(f"text={applicant_name}")
            if result.count() > 0:
                result.first
                allure.attach(
                    "Test case passed successfully:Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Applicant not found: {applicant_name}")

           
   
    def all_applicant_page(self, applicant_name):
        with allure.step(f"Select applicant: {applicant_name}"):
            
            row = self.page.locator('//input[@type="checkbox"]').nth(1)
            row.click(force=True)
            applicant = self.page.get_by_text(applicant_name, exact=True)
            expect(applicant).to_be_visible(timeout=20000)
            

        
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


    def all_applicant_pre_screened(self, applicant_name):
        with allure.step(f"Select applicant: {applicant_name}"):
            row = self.page.locator('//input[@type="checkbox"]').nth(1)
            row.click(force=True)
            applicant = self.page.get_by_text(applicant_name, exact=True)
            expect(applicant).to_be_visible(timeout=20000)


    def move_to_applicant_pre_screened(self,timeout=3000):
        with allure.step("Verify move to button is visible "):
            move_to_btn = self.page.locator('//button[@role="combobox"]').nth(0)
            move_to_btn.click()

            self.page.get_by_role("option", name="Pre-Screened").click()
            self.page.locator('//button[contains(text(),"Skip")]').click()

            toast = self.page.get_by_text("applicant is already in the stage-Pre-Screened")

            if toast.is_visible(timeout=2000):
                pytest.fail("Applicant already exists in Selected stage")

            

            allure.attach(
                    "Test case passed successfully:Applicant is moved to stage",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            

   

    def search_by_name(self,applicant_name1):
        with allure.step("search by name or email,Phone number"):
            self.page.reload()
            self.page.locator("div.cursor-pointer svg.lucide-search").click()
            self.page.wait_for_timeout(1000)
            search_name=self.page.locator('//input[@type="text"]')
            search_name.fill(applicant_name1)
            result = self.page.locator(f"text={applicant_name1}")
            if result.count() > 0:
                result.first
                allure.attach(
                    "Test case passed successfully:Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Applicant not found: {applicant_name1}")
            

    def all_applicant_shortlisted(self, applicant_name1):
        with allure.step(f"Select applicant: {applicant_name1}"):
            row = self.page.locator('//input[@type="checkbox"]').nth(1)
            row.click(force=True)
            applicant = self.page.get_by_text(applicant_name1, exact=True)
            expect(applicant).to_be_visible(timeout=20000)
            
    def move_to_applicant_shortlisted(self,timeout=3000):
        with allure.step("Verify move to button is visible "):
            
            move_to_btn = self.page.locator('//button[@role="combobox"]').nth(0)
            move_to_btn.click()

            shortlisted = self.page.get_by_role("option", name="Shortlisted")
            shortlisted.click()
            skip = self.page.locator('//button[contains(text(),"Skip")]')
            skip.click()
            allure.attach(
                    "Test case passed successfully:Applicant is moved to stage",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
        
    def search_by_name(self,applicant_name2):
        with allure.step("search by name or email,Phone number"):
            self.page.reload()
            self.page.locator("div.cursor-pointer svg.lucide-search").click()
            self.page.wait_for_timeout(1000)
            search_name=self.page.locator('//input[@type="text"]')
            search_name.fill(applicant_name2)
            result = self.page.locator(f"text={applicant_name2}")
            if result.count() > 0:
                result.first
                allure.attach(
                    "Test case passed successfully:Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Applicant not found: {applicant_name2}")
            

    def all_applicant_interviewing(self, applicant_name2):
        with allure.step(f"Select applicant: {applicant_name2}"):
            row = self.page.locator('//input[@type="checkbox"]').nth(1)
            row.click(force=True)
            applicant = self.page.get_by_text(applicant_name2, exact=True)
            expect(applicant).to_be_visible(timeout=20000)
    
    def move_to_applicant_interviewing(self,timeout=3000):
        with allure.step("Verify move to button is visible "):
            move_to_btn = self.page.locator('//button[@role="combobox"]').nth(0)
            move_to_btn.click()

            interviewing = self.page.get_by_role("option", name="Interviewing")
            interviewing.click()

            skip = self.page.locator('//button[contains(text(),"Skip")]')
            skip.click()
            allure.attach(
                    "Test case passed successfully:Applicant is moved to stage",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            


    def search_by_name(self,applicant_name3):
        with allure.step("search by name or email,Phone number"):
            self.page.reload()
            self.page.locator("div.cursor-pointer svg.lucide-search").click()
            self.page.wait_for_timeout(1000)
            search_name=self.page.locator('//input[@type="text"]')
            search_name.fill(applicant_name3)
            result = self.page.locator(f"text={applicant_name3}")
            if result.count() > 0:
                result.first
                allure.attach(
                    "Test case passed successfully:Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Applicant not found: {applicant_name3}")
            
    def all_applicant_selected(self, applicant_name3):
        with allure.step(f"Select applicant: {applicant_name3}"):
            row = self.page.locator('//input[@type="checkbox"]').nth(1)
            row.click(force=True)
            result = self.page.locator(f"text={applicant_name3}")
            if result.count() > 0:
                result.first
                allure.attach(
                    "Test case passed successfully:Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Applicant not found: {applicant_name3}")

                
            
    def move_to_applicant_selected(self,timeout=3000):
        with allure.step("Verify move to button is visible "):
            move_to_btn = self.page.locator('//button[@role="combobox"]').nth(0)
            move_to_btn.click()

            self.page.get_by_role("option", name="Selected").click()

            toast = self.page.get_by_text("already")

            if toast.is_visible(timeout=2000):
                pytest.fail("Applicant already exists in Selected stage")

            self.page.locator('//button[contains(text(),"Skip")]').click()


            allure.attach(
                "Test case passed successfully: Applicant is moved to Selected stage",
                name="Test_Success_Message",
                attachment_type=allure.attachment_type.TEXT
)

           
            
    def search_by_name(self,applicant_name4):
        with allure.step("search by name or email,Phone number"):
            self.page.reload()
            self.page.locator("div.cursor-pointer svg.lucide-search").click()
            self.page.wait_for_timeout(1000)
            search_name=self.page.locator('//input[@type="text"]')
            search_name.fill(applicant_name4)
            result = self.page.locator(f"text={applicant_name4}")
            if result.count() > 0:
                result.first
                allure.attach(
                    "Test case passed successfully:Applicant name visible in the applicant page",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            else:
                raise AssertionError(f" Applicant not found: {applicant_name4}")
            
    def all_applicant_rejected(self, applicant_name4):
        with allure.step(f"Select applicant: {applicant_name4}"):

            row = self.page.locator('//input[@type="checkbox"]').nth(1)
            row.click(force=True)
            applicant = self.page.get_by_text(applicant_name4, exact=True)
            expect(applicant).to_be_visible(timeout=20000)
            

    def move_to_applicant_rejected(self,timeout=3000):
        with allure.step("Verify move to button is visible "):
            move_to_btn=self.page.locator('//button[@role="combobox"]').nth(0)
            move_to_btn.click()
            pre_screen=self.page.get_by_role("option",name="Rejected")
            pre_screen.click()
            skip=self.page.locator('//button[contains(text(),"Skip")]')
            skip.click() 
            allure.attach(
                    "Test case passed successfully:Applicant is moved to stage",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT)
            
    


    def sort_applicant(self,timeout=2000):
        with allure.step("Click on all applicants ribbon"):
            self.page.reload()
            self.page.locator('//button[contains(text(),"All Applicants")]').click()
            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()

            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Name").click()
            self.page.get_by_text("A → Z", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Name").click()
            self.page.get_by_text("Z → A", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("ATS Score").click()
            self.page.get_by_text("Lowest First", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("ATS Score").click()
            self.page.get_by_text("Highest First", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Date & Time").click()
            self.page.get_by_text("Oldest First", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Date & Time").click()
            self.page.get_by_text("Newest First", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Work Experience").click()
            self.page.get_by_text("Lowest First", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Work Experience").click()
            self.page.get_by_text("Highest First", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Notice Period").click()
            self.page.get_by_text("Lowest First", exact=True).click()
            self.page.wait_for_timeout(1000)

            self.page.locator("button:has(svg.lucide-arrow-down-wide-narrow)").click()
            self.page.wait_for_selector('//div[@role="menuitem"]').click()
            self.page.get_by_text("Work Experience").click()
            self.page.get_by_text("Highest First", exact=True).click()



            self.page.reload()
            allure.attach(
                    "Test case passed successfully:sort applicants is applied to all applicants successfully",
                    name="Test_Success_Message",
                    attachment_type=allure.attachment_type.TEXT) 
            

    

   





    





    


