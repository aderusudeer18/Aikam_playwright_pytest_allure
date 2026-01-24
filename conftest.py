import pytest
import os
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(request, browser_context):
    page = browser_context.new_page()
    yield page

    # Attach screenshot ONLY if test failed
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/{request.node.name}.png"

        page.screenshot(path=screenshot_path, full_page=True)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep



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
