from playwright.sync_api import expect
import allure
import pytest

from constants.messages import AllureMessages, ErrorLogMessages
from constants.locators import DashboardLocators

class DashboardPage:
    def __init__(self, page):
        self.page = page

    def job_icon(self,timeout=10000):
        with allure.step(AllureMessages.CLICK_ON_JOBS_ICON_STEP):
            try:
                icon=self.page.locator(DashboardLocators.JOBS_ICON)
                expect(icon).to_be_visible(timeout=timeout)
                icon.click()
                allure.attach(
                        AllureMessages.JOBS_ICON_CLICKED_SUCCESS,
                        name="Success",
                        attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                pytest.fail(f"{ErrorLogMessages.FAILED_TO_CLICK_JOBS_ICON}{e}")

    def test_create_job(self,timeout=15000):
        with allure.step(AllureMessages.CLICKED_ON_CREATE_JOB_STEP):
            try:
                create_job = self.page.locator(DashboardLocators.CREATE_JOB_BTN)
                expect(create_job).to_be_visible(timeout=timeout)
                create_job.click()
                allure.attach(AllureMessages.CLICKED_CREATE_JOB_SUCCESS, name="Success", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                 pytest.fail(f"{ErrorLogMessages.FAILED_TO_CLICK_CREATE_JOB}{e}")
