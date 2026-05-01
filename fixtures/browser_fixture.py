
import pytest
from utilities.logging import logger
from configurationData.config import headless as HEADLESS, BASE_URL

@pytest.fixture(scope="session")
def browser(playwright_instance):
    logger.info("Launching browser (session)")
    browser = playwright_instance.chromium.launch(headless=HEADLESS)
    yield browser
    logger.info("Closing browser (session)")
    browser.close()

@pytest.fixture(scope="function")
def context(browser, request):
    """
    Fresh context per test = isolation (parallel-safe)
    Enable tracing, video, screenshots
    """
    test_name = request.node.name

    ctx = browser.new_context(
        base_url=BASE_URL,
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=True,
        record_video_dir="reports/videos",
    )

    # Start tracing
    ctx.tracing.start(
        name=test_name,
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield ctx

    # Stop tracing (save per-test)
    trace_path = f"traces/{test_name}.zip"
    ctx.tracing.stop(path=trace_path)

    ctx.close()