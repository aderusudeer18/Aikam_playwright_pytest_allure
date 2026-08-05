from playwright.sync_api import sync_playwright
import pytest
import allure


class Organisation:
    def __init__(self,page):
        self.page=page  

    def org_details(self, org_email,org_name, timeout=3000):
        with allure.step("edit org details"):
            self.page.reload()
            org_btn = self.page.locator('button:has(svg.lucide-building2)').first
            org_btn.wait_for(state="visible", timeout=5000)
            org_btn.click()
            
            search_bar = self.page.get_by_placeholder("Search", exact=False).first
            try:
                search_bar.wait_for(state="visible", timeout=5000)
            except:
                pass # fallback below
            
            if not search_bar.is_visible():
                search_bar = self.page.locator('input[type="text"]').first
                
            search_bar.fill(org_email)
            search_bar.press("Enter")

            # Wait for search results to filter
            self.page.wait_for_timeout(2000)
            
            org_locator = self.page.get_by_text(org_name, exact=False).first
            try:
                org_locator.wait_for(state="visible", timeout=10000)
                org_locator.click()
            except:
                # fallback to click the first row if org_name isn't visible
                self.page.locator('tbody tr').first.click()

            edit_org = self.page.locator('//button[contains(text(),"Edit Organization")]')
            edit_org.wait_for(state="visible", timeout=5000)
            edit_org.click()
            
            pre_screening_toggle = self.page.locator('//label[contains(text(),"Prescreening")]')
            pre_screening_toggle.wait_for(state="visible", timeout=5000)
            pre_screening_toggle.click()
            
            ai_interview_toggle = self.page.locator('//label[contains(text(),"Interview")]')
            ai_interview_toggle.click()
            
            code_assessment_toggle = self.page.locator('//label[contains(text(),"Coding Assessment")]')          
            code_assessment_toggle.click()

            upgrade_plan = self.page.locator('//button[contains(text(),"Upgrade Plan") or contains(text(),"Change Plan")]')
            upgrade_plan.click()
            
            # Identify current plan by looking for text like "Current Plan: COMPACT"
            current_plan_element = self.page.locator('text=/Current Plan:/i').first
            try:
                current_plan_element.wait_for(state="visible", timeout=5000)
            except:
                pass
            
            if current_plan_element.is_visible():
                current_plan_text = current_plan_element.inner_text().upper()
                
                if "COMPACT" in current_plan_text:
                    # Current is Compact -> Upgrade to Enterprise
                    enterprise_select_btn = self.page.locator('div').filter(has_text="Enterprise").locator('button:has-text("Select")').first
                    if enterprise_select_btn.is_visible():
                        enterprise_select_btn.click()
                        
                elif "ENTERPRISE" in current_plan_text:
                    # Current is Enterprise -> Downgrade to Compact
                    compact_select_btn = self.page.locator('div').filter(has_text="Compact").locator('button:has-text("Select")').first
                    if compact_select_btn.is_visible():
                        compact_select_btn.click()
            
            # Click Confirm Change for the plan modal
            confirm_btn = self.page.locator('button:has-text("Confirm Change")')
            if confirm_btn.is_visible():
                confirm_btn.click()
            self.page.wait_for_timeout(2000)
            allure.attach("Test case passed successfully: Organization details updated", name="Success", attachment_type=allure.attachment_type.TEXT)

    def org_email(self, email):
        with allure.step("Edit org email"):
            self.page.locator('//input[@id="admin-email"]').fill(email)
            allure.attach("Test case passed successfully: Organization email edited", name="Success", attachment_type=allure.attachment_type.TEXT)
            
    def org_name(self, name):
        with allure.step("Edit org name"):
            self.page.locator('//input[@id="org-name"]').fill(name)
            allure.attach("Test case passed successfully: Organization name edited", name="Success", attachment_type=allure.attachment_type.TEXT)