import pytest
import allure
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=700)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when in ("call", "setup"):
        page = item.funcargs.get("page")

        if page:
            try:
                status = "FAILED" if rep.failed else "PASSED"

                allure.attach(
                    page.screenshot(full_page=True),
                    name=f"{item.name} - {rep.when} - {status}",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as e:
                print("Screenshot capture failed:", e)




def pytest_sessionstart(session):
    os.makedirs("allure-results", exist_ok=True)

    with open("allure-results/environment.properties", "w") as f:
        f.write(
            "Browser=Chromium\n"
            "Framework=Playwright + Pytest\n"
            "Report=Allure\n"
            "OS=Windows\n"
            "Environment=QA\n"
            "Developed=AIKAM\n"
        )

