from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class Search_CEL():
    def __init__(self, browser_driver, search_link):
        self._driver = browser_driver
        self._link = search_link

    def search_by_id(self, id):
        if (id):
            self._driver.get(self._link)
            locator = (By.NAME, 'com.oocl.ir4.blsop.form.customization.criteria.textfield.optId')
            WebDriverWait(self._driver, 20, 1).until(method=visibility_of_element_located(locator),  message='out of time 1')
            self._driver.find_element_by_name('com.oocl.ir4.blsop.form.customization.criteria.textfield.optId').send_keys(str(id))
            self._driver.find_element_by_id('com.oocl.ir4.blsop.form.customization.criteria.button.find').click()