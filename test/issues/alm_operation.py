from common.selenium_driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, presence_of_element_located

class Alm_Operation():
    def __init__(self):
        self._default_link = 'http://alm.oocl.com/?workspaceId=WS100102&scopeId=PJ100468'

    def open_page(self, browser_driver, link=''):
        link = link or self._default_link
        browser_driver.get(link)
        try:
            alert = browser_driver.switch_to_alert()
            alert.accept()
        except:
            print('There is some error')

    def create_story(self, title, description="", ):
        browser_driver = Driver().get_firefox_driver()
        self.open_page(browser_driver)

        browser_driver.switch_to.window(browser_driver.window_handles[0])
        locator = (By.XPATH, "//md-icon[text()='equalizer']/parent::button")
        WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find the story tab button.')
        browser_driver.find_element_by_xpath("//md-icon[text()='equalizer']/parent::button").click()
        locator = (By.XPATH, "//span[text()='User Stories']")
        WebDriverWait(browser_driver, 5, 1).until(method=visibility_of_element_located(locator), message='can\'t find the user story tab.')
        browser_driver.find_element_by_xpath("//span[text()='User Stories']").click()
        locator = (By.XPATH, "//md-icon[text()='add']/parent::button[child::span]")
        WebDriverWait(browser_driver, 5, 1).until(method=visibility_of_element_located(locator), message='can\'t find the add story button.')
        browser_driver.find_element_by_xpath("//md-icon[text()='add']/parent::button[child::span]").click()
        locator = (By.XPATH, "//input[@placeholder='STORY NAME']")
        WebDriverWait(browser_driver, 5, 1).until(method=visibility_of_element_located(locator), message='can\'t find the story name field.')
        browser_driver.find_element_by_xpath("//input[@placeholder='STORY NAME']").send_keys(title)
        describe_area = browser_driver.find_element_by_xpath("//b[text()='DESCRIPTION']/parent::div/parent::section[@id='textAngularContainerA']/div[2]/div[2]/div[3]")
        describe_area.click()
        describe_area.send_keys(description)
        browser_driver.find_element_by_xpath("//span[text()='Create']/parent::button[@ng-click='onCreateClick()']").click()

        browser_driver.close()

    def copy_tasks_from_st(self, to_stnum, from_stnum, except_tasks):
        browser_driver = Driver().get_firefox_driver()
        link = 'http://alm.oocl.com/stories/detail?scopeId=PJ100468&workspaceId=WS100102&storyId=<ST>&defaultTab=0'
        link.replace('\<ST\>', str(to_stnum))
        print(link)
        self.open_page(browser_driver, link)

        # browser_driver.switch_to.window(browser_driver.window_handles[0])
        # locator = (By.XPATH, "//md-icon[text()='search']/parent::button")
        # WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find the story search button.')
        # browser_driver.find_element_by_xpath("//md-icon[text()='search']/parent::button").click()
        # locator = (By.XPATH, "//input[@id='searchInput']")
        # WebDriverWait(browser_driver, 5, 1).until(method=visibility_of_element_located(locator), message='can\'t find the story search field.')
        # browser_driver.find_element_by_xpath("//input[@id='searchInput']").send_keys('ST120927' + Keys.ENTER)
        #
        #
        # open_new_window_js = 'window.open();'
        # browser_driver.execute_script(open_new_window_js)
        # browser_driver.switch_to.window(browser_driver.window_handles[1])
        # self.open_page(browser_driver)
        #
        # locator = (By.XPATH, "//md-icon[text()='search']/parent::button")
        # WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find the story search button.')
        # browser_driver.find_element_by_xpath("//md-icon[text()='search']/parent::button").click()
        # locator = (By.XPATH, "//input[@id='searchInput']")
        # WebDriverWait(browser_driver, 5, 1).until(method=visibility_of_element_located(locator), message='can\'t find the story search field.')
        # browser_driver.find_element_by_xpath("//input[@id='searchInput']").send_keys('ST120556' + Keys.ENTER)
        #
        # browser_driver.close()
        # browser_driver.switch_to.window(browser_driver.window_handles[0])
        # browser_driver.close()

        browser_driver.close()