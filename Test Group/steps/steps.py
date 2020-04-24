from behave import given, when, then
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


@given("I open traffic UI")
def setup(self):
    # windows path
    # chromedriver_path = r'C:\Users\taimur\Downloads\chromedriver_win32\chromedriver.exe'
    # electron_path = r"C:\Program Files\Traffic UI\Traffic UI.exe"

    # ubuntu path
    chromedriver_path = r'/home/taimur/Downloads/chromedriver'
    electron_path = r"/home/taimur/Downloads/traffic-carmaker-00017-d46c3c0-linux.AppImage"

    opts = Options()
    opts.add_argument("--remote-debugging-port=9222")
    # opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--start-maximized")
    opts.binary_location = electron_path
    self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
    self.driver.implicitly_wait(15)


# wait for application to start

@when('I select the project folder and click start')
def test_login(self):
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")


@then('I should see configurations being imported correctly')
def test_login(self):
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()
    self.driver.quit()


@when('I select the project folder and clear the field')
def test_login(self):
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    elem.clear()


@when('I click start configurations')
def test_login(self):
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()


@then('I should see configurations error and path not selected')
def test_login(self):
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()
    path = self.driver.find_element_by_css_selector(
        'div.layout.project-path-content.py-3.padding-left.pr-3.column > span.note.text-truncate')
    assert path.text == ''
    self.driver.quit()
