import pytest
from selenium import webdriver
from datetime import datetime

link = "http://localhost:3000/"

@pytest.fixture(scope="function")
def browser(request):
    test_name = request.node.nodeid
    print("\nstart browser for test", test_name, "..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    try:
        browser.get(link)
        yield browser
        take_screenshot(browser, test_name)
    finally:
        print("\nquit browser for test", test_name, "..")
        browser.quit()
        
def take_screenshot(browser, test_name):
    file_name = test_name.replace("::", "__") + " " + datetime.now().strftime("%Y-%m-%d_%H%M") + ".png"
    print("\ntake screenshot", file_name, "..")
    browser.save_screenshot(file_name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        browser = item.funcargs['browser']
        screenshot = browser.get_screenshot_as_base64()
        extra.append(pytest_html.extras.image(screenshot, ''))
    report.extra = extra