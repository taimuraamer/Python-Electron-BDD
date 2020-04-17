from behave import given, when, then
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from keyboard import press


@given("I open traffic UI")
def setup(self):
    chromedriver_path = r'/home/taimur/Downloads/chromedriver'
    electron_path = r"/home/taimur/Downloads/traffic-carmaker-00012-ddd3569-linux.AppImage"

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

@then('I should see an image')
def test_login(self):
    time.sleep(2)
    print(self.driver.find_element_by_xpath("//*[@id='AaiSelectProjectPath']/div[1]/p[1]").text)
    self.driver.find_element_by_xpath("//*[@id='AaiSelectProjectPath']/div[2]/div[2]/button/span").click()
    time.sleep(2)
    press('enter')
    time.sleep(2)
    self.driver.find_element_by_xpath("//*[@id='AaiSelectProjectPath']/div[3]/button").click()
    self.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div/div[1]/span/aside/div[1]/div/div[4]/div/div[2]/a[1]").is_displayed()
    self.driver.quit()


@given("scenario 2 given statement")
def in_sub_dir(context):
    pass


@given("scenario 2 given statement")
def negative(context):
    pass
