from selenium.webdriver import FirefoxProfile
from selenium import webdriver
from common.config import *
from func_module.SOP.CEL.search_CEL import Search_CEL

if __name__ == "__main__":
    config = GlobalConfig()
    config.load()

    profile_dir = config.profile_dir
    firefoxProfile = FirefoxProfile(profile_dir)
    browser_driver = webdriver.Firefox(firefoxProfile)

    test_search_cel = Search_CEL(browser_driver, "http://irisqa2.oocl.com/wls_prs_doc/secured/blSop/searchBlSop/display")
    test_search_cel.search_by_id(75081)

    browser_driver.quit()