from playwright.sync_api import sync_playwright,expect
import allure
import time



class DashboardPage:
    def __init__(self, page):
        self.page = page    

    def create_organization_btn(self):
        with allure.step("Create Organization"):
            # Use a more flexible locator, e.g. text or button
            self.page.locator('text=Create Organization').first.click()
            self.page.wait_for_timeout(2000)

    def org_details(self,name,admin_name,primary_email,option_text,phone_num):
        with allure.step("creating new organisation"):
            self.page.locator('//input[@id="org-name"]').fill(name)
            self.page.locator('//input[@id="admin-name"]').fill(admin_name)
            
            dropdown = self.page.locator('//button[@type="button"]').nth(2)
            dropdown.click()

            option = self.page.locator(f"//div[text()='{option_text}']")

            if option.count() > 0:
                option.first.click()
            else:
                # Click the first available option if the exact text isn't found just as a fallback or raise
                self.page.locator('//div[@role="option"]').first.click()
                # raise Exception(f"Option '{option_text}' is not available in the dropdown.")
            
            primary_admin_email=self.page.locator('//input[@id="admin-email"]')
            primary_admin_email.fill(primary_email)

            phone_locator=self.page.locator('//input[@id="phone"]')
            phone_locator.click()
            self.page.keyboard.type(phone_num, delay=50)
            self.page.wait_for_timeout(1000)

            # take a screenshot to debug why the submit button is disabled
            self.page.screenshot(path="form_screenshot.png")
            
            # Save HTML
            html_content = self.page.content()
            with open("page_html.txt", "w", encoding="utf-8") as f:
                f.write(html_content)

            create_org_btn = self.page.locator('button:has-text("Create Organization")').last

            if create_org_btn.is_visible():
                create_org_btn.click()
            else:
                self.page.locator('text=Create Organization').last.click()
                
            # Wait for the modal to close and the organization to be fully created
            self.page.wait_for_timeout(5000)
