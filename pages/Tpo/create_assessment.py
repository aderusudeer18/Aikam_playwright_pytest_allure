from playwright.sync_api import sync_playwright, expect
import allure
import pytest

class CreateAssessment:
    def __init__(self, page):
        self.page = page
        
    def test_create_assessment(self, timeout=15000):
        with allure.step("click on create assessment"):
            try:
                create_assessment = self.page.locator("//button[contains(text(),'Create Assessment')]")
                expect(create_assessment).to_be_visible(timeout=timeout)
                create_assessment.click()
                allure.attach(
                    "Test case passed successfully:Create Assessment icon is clicked ",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as e:
                pytest.fail(f"Failed to click Create Assessment icon: {e}")

    def test_step1_select_skill(self, skill_name="Python", timeout=5000):
        with allure.step(f"Step 1: Select skill '{skill_name}'"):
            try:
                # Type into search box
                search_input = self.page.locator('input[placeholder="Search skill..."]')
                expect(search_input).to_be_visible(timeout=timeout)
                search_input.fill(skill_name)
                self.page.wait_for_timeout(1000) # Wait for suggestions to load
                
                # Select the suggestion
                suggestion = self.page.locator(f'button:has-text("{skill_name}")').first
                expect(suggestion).to_be_visible(timeout=timeout)
                suggestion.click()
                
                # Click Next
                next_btn = self.page.locator('button:has-text("Next")')
                expect(next_btn).to_be_enabled(timeout=timeout)
                next_btn.click()
                
                allure.attach(
                    f"Test case passed successfully: Selected skill {skill_name} and clicked Next",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as e:
                pytest.fail(f"Failed to select skill {skill_name} in Step 1: {e}")

    def test_step2_fill_details_and_publish(self, assessment_title="Python Entry Level Test", timeout=10000):
        with allure.step(f"Step 2: Enter title '{assessment_title}' and publish"):
            try:
                # The page might take a moment to transition to step 2
                title_input = self.page.locator('input[placeholder="Title that describes the role"]')
                expect(title_input).to_be_visible(timeout=timeout)
                title_input.fill(assessment_title)
                
                # Click Publish
                publish_btn = self.page.locator('button:has-text("Publish")')
                expect(publish_btn).to_be_visible(timeout=timeout)
                publish_btn.click()
                
                # Wait for the success toast or redirection to Jobs page
                self.page.wait_for_url("**/jobs**", timeout=15000)
                
                allure.attach(
                    f"Test case passed successfully: Assessment '{assessment_title}' created",
                    name="Success",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as e:
                pytest.fail(f"Failed to publish assessment in Step 2: {e}")