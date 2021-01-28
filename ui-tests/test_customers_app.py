import pytest
from selenium import webdriver


@pytest.mark.bug_1
def test_welcome_screen_layout(browser):
    assert "Customers App" == browser.title, "Wrong Page Title, expected: Customers App"


@pytest.mark.bug_2
def test_customer_list_screen_data(browser):
    name_input = browser.find_element_by_id("name")
    name_input.send_keys("Chema del Barco")
    browser.find_element_by_css_selector("input[type='button'][value='Submit']").click()
    row = browser.find_element_by_xpath("//a[text()='Caribian Airlnis']/../..").text
    assert "Caribian Airlnis 1000 Medium" == row, "Wrong company Size, expected: Medium"


@pytest.mark.bug_3
def test_contacts_detail_screen_united_brands(browser):
    name_input = browser.find_element_by_id("name")
    name_input.send_keys("Chema del Barco")
    browser.find_element_by_css_selector("input[type='button'][value='Submit']").click()
    browser.find_element_by_xpath(".//a[text()='United Brands']").click()
    name_text = browser.find_element_by_xpath("//b[text()='Name:']/..").text
    assert "Name: United Brands" == name_text, "Incorrect company name, expected: Name: United Brands"
    size = browser.find_element_by_xpath("//b[text()='Size:']/..").text
    assert "Size: Medium" == size, "Incorrect company name, expected: Medium"
