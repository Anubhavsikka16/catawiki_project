import pytest
import allure
from playwright.sync_api import sync_playwright
from faker import Faker
from configurationData.config import Config

fake = Faker()

# -------------------------
# 🔹 Faker Data Fixtures
# -------------------------

@pytest.fixture
def user_data():
    return {
        "email": fake.email(),
        "password": fake.password(length=10),
        "username": fake.user_name()
    }

# -------------------------
# 🔹 Playwright Setup
# -------------------------

@pytest.fixture(scope="session") 
def playwright_instance(): # open and close Playwright once per session
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance): # open and close browser once per session
    browser = playwright_instance.chromium.launch(headless=Config.HEADLESS)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser, request):
    test_name = request.node.name

    context = browser.new_context(
        base_url=Config.BASE_URL,
        viewport=Config.VIEWPORT,
        ignore_https_errors=True,
        record_video_dir=Config.VIDEO_PATH
    )

    # Start tracing
    context.tracing.start(
        name=test_name,
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    # Stop tracing
    trace_path = f"traces/{test_name}.zip"
    context.tracing.stop(path=trace_path)

    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    page.set_default_timeout(Config.TIMEOUT)
    page.goto(Config.BASE_URL)  # Navigate to base URL
    yield page
    page.close()

# -------------------------
# 🔹 Failure Handling + Allure
# -------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            allure.attach.file(
                screenshot_path,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Attach DOM
            html = page.content()
            allure.attach(
                html,
                name="DOM Snapshot",
                attachment_type=allure.attachment_type.HTML
            )