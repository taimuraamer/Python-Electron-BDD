from lib2to3.pgen2 import driver

from behave import given, when, then
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.command import Command


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


@when('I enter valid input values for physical property of maximum speed and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        287)
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter valid input values for physical property of brake maximum deceleration and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        21)
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter valid input values for physical property of height and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '2.4')
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter valid input values for physical property of cdA and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '1.2')
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter valid input values for physical property of width and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '2.27')
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter valid input values for physical property of engine maximum acceleration and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '2.27')
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter valid input values for physical property of mass and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '2000')
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter valid input values for physical property of length and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '8.84')
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add profile']").click()


@when('I enter empty input values for physical property of maximum speed and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    time.sleep(1)


@when('I enter empty input values for physical property of brake maximum deceleration speed and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    time.sleep(1)


@when('I enter empty input values for physical property of height and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    time.sleep(1)


@when('I enter empty input values for physical property of cdA and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)


@when('I enter empty input values for physical property of width and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)


@when('I enter empty input values for physical property of engine max. acceleration and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)


@when('I enter empty input values for physical property of mass and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)


@when('I enter empty input values for physical property of length and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)


@when('I enter invalid input values for physical property of maximum speed and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div.flex.mt-4.xs12 > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        -287)
    time.sleep(1)


@when('I enter invalid input values for physical property of break maximum deceleration and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(3) > div > div > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        8)
    time.sleep(1)



@when('I enter invalid input values for physical property of height and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(5) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '-88')
    time.sleep(1)



@when('I enter invalid input values for physical property of cdA and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(4) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '-9')
    time.sleep(1)



@when('I enter invalid input values for physical property of width and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(3) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '-2')
    time.sleep(1)



@when('I enter invalid input values for physical property of engine maximum acceleration and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '-8')
    time.sleep(1)



@when('I enter invalid input values for physical property of mass and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(2) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '-2000')
    time.sleep(1)



@when('I enter invalid input values for physical property of length and click add profile')
def test_login(self):
    # loading configurations
    time.sleep(2)
    elem = self.driver.find_element_by_id('input-48')
    elem.send_keys("/home/taimur/Downloads/Empty Project/")
    self.driver.find_element_by_xpath("//*[text()='Required']").click()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").is_enabled()
    self.driver.find_element_by_css_selector("#AaiSelectProjectPath div.row.mt-12.justify-center  button").click()
    self.driver.find_element_by_css_selector(
        "div.layout.project-path-content.py-3.padding-left.pr-3.column  div  button  span").is_displayed()

    # adding vehicle profile  with valid maximum speed
    time.sleep(2)
    vehicle_profile = self.driver.find_element_by_xpath("//*[text()='Vehicle and Driver Profiles']")
    vehicle_profile.is_enabled()
    vehicle_profile.is_displayed()
    vehicle_profile.click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='add vehicle profile']").click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_css_selector(
        '#CRUDVehicleProfile > form > div.row.mt-12.physical-properties > div.flex.xs6 > div > div:nth-child(1) > div > div > div > div > div.v-input__slot > div > input[type=text]').send_keys(
        '-8.84')
    time.sleep(1)


@then('I should see vehicle profile being added and visible in profile table')
def test_login(self):
    path = self.driver.find_element_by_css_selector(
        'div.row.mt-3 > div > div > table > tbody > tr > td:nth-child(1)')
    assert path.text == 'Vehicle-0'
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        'tbody > tr > td:nth-child(3) > div > button:nth-child(2) > span > i').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.layout.pt-3 > button:nth-child(3) > span').click()
    time.sleep(1)
    self.driver.quit()


@then('I should see an error being shown and vehicle profile not being added')
def test_login(self):
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='Required']")
    self.driver.quit()


@then('I should see an error for value greater than zero')
def test_login(self):
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='Should be greater than zero']")
    self.driver.quit()


@then('I should see an error for value less than zero')
def test_login(self):
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='Should be smaller than zero']")
    self.driver.quit()


@then('I should see an error for value greater than or equals to 90')
def test_login(self):
    time.sleep(1)
    self.driver.find_element_by_xpath("//*[text()='Should be greater than or equals to 90']")
    self.driver.quit()
