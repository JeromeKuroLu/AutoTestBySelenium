from selenium.webdriver import FirefoxProfile
from selenium import webdriver
from common.config import *

class Driver():

    def get_firefox_driver(self):
        config = GlobalConfig()
        config.load()

        profile_dir = config.profile_dir
        firefoxProfile = FirefoxProfile(profile_dir)
        browser_driver = webdriver.Firefox(firefoxProfile)
        return  browser_driver