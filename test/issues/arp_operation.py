import time

import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_driver import Driver
from common.xlsx_util import Xlsx_Util


class Arp_Operation:
    def __init__(self):
        self._default_link = 'http://zha-mvp-021-w10:8080/'

    def open_page(self, browser_driver, link=''):
        link = link or self._default_link
        browser_driver.get(link)

    def log_in_jenkins(self):
        title_array = ['Record Time', 'Debt', 'Bugs', 'Duplication', 'Coverage', 'Unit Tests', 'Code Smells', 'Remark']
        data_array = [time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]

        browser_driver = Driver().get_firefox_driver()
        self.open_page(browser_driver)

        browser_driver.switch_to.window(browser_driver.window_handles[0])
        locator = (By.XPATH, "//input[@name='j_username']")
        WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find user input field.')
        user_input_field = browser_driver.find_element_by_xpath(locator[1])
        user_input_field.click()
        user_input_field.send_keys("Jenkins")

        locator = (By.XPATH, "//input[@name='j_password']")
        WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find password input field.')
        pwd_input_field = browser_driver.find_element_by_xpath(locator[1])
        pwd_input_field.click()
        pwd_input_field.send_keys("Password1")

        locator = (By.XPATH, "//button[contains(text(),'log in')]")
        log_in_button = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find login button.')
        log_in_button.click()

        locator = (By.XPATH, "//a[@href='job/IRIS4_ARP_SONAR_JAVA/']")
        arp_link = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find arp link.')
        arp_link.click()

        locator = (By.XPATH, "//a[text()='SonarQube']")
        sonar_qube_link = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator),message='can\'t find sonar qube link.')
        sonar_qube_link.click()

        locator = (By.XPATH, "//div[text()='Debt']/preceding-sibling::div[1]")
        debt_area = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find debt area.')
        data_array.append(re.findall('^\d+', debt_area.text)[0])

        locator = (By.XPATH, "//div[text()='Duplications']/preceding-sibling::div[1]")
        duplications_area = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find duplications area.')
        data_array.append(duplications_area.text)

        locator = (By.XPATH, "//div[text()='Unit Tests']/preceding-sibling::div[1]")
        unit_test_area = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find unit test area.')
        data_array.append(unit_test_area.text)

        locator = (By.XPATH, "//div[text()='Coverage']/preceding-sibling::div[1]")
        coverage_area = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find coverage area.')
        data_array.append(coverage_area.text)

        locator = (By.XPATH, "//a[text()='Issues']")
        issues_tab = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find issues tab.')
        issues_tab.click()

        locator = (By.XPATH, "//div[@class='issues-page-actions']/span[1]/strong[1]")
        value_area = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find value area.')

        locator = (By.XPATH, "//a[@data-value='BUG']")
        bug_section = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find bug option.')
        bug_section.click()
        time.sleep(1)
        data_array.insert(2, value_area.text.split('/')[1])
        bug_section.click()

        locator = (By.XPATH, "//a[@data-value='CODE_SMELL']")
        code_smell_section = WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find code smell option.')
        code_smell_section.click()
        time.sleep(1)
        data_array.append(value_area.text.split('/')[1])
        code_smell_section.click()

        Xlsx_Util('D:/arp_sonar_qube_report.xlsx').write(title_array, data_array)
        browser_driver.quit()
        print('success')