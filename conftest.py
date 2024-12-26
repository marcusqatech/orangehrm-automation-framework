import pytest
from playwright.sync_api import sync_playwright
from utils.logger import getLogger

# Get the logger
logger = getLogger()

# Fixture to launch browser
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        # Launch the browser (Chromium in this case)
        logger.info("Launching Chromium browser...")
        browser = p.chromium.launch(headless=False)  # Set headless=True to run in the background
        yield browser
        logger.info("Closing Chromium browser...")
        browser.close()

# Capture screenshot on failure and log error
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        page = item.funcargs.get('page', None)
        if page:
            screenshot_path = f"reports/{item.nodeid}_failure.png"
            page.screenshot(path=screenshot_path)
            logger.error(f"Test failed: {item.nodeid}. Screenshot saved at {screenshot_path}")
    else:
        logger.info(f"Test passed: {item.nodeid}")

# Capture console logs (optional)
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.on("console", lambda msg: logger.info(f"Console message: {msg.text}"))
    yield page
    page.close()
