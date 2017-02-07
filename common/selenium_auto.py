from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

# browser.get('http://www.baidu.com')
# assert 'Yahoo' in browser.title

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

# print(find_connectable_ip('localhost', '1111'))
# browser.get('http://luje4:Tuesday2@ssoidpqa.oocl.com')

# browser.add_cookie({'SSO_USER_PROVIDER_COOKIE': 'OOCLDM', 'SSO_IRIS4_USERID_COOKIE_QA2': 'LUJE4'})

firefoxProfile = FirefoxProfile('''C:/Users/LUJE4/AppData/Roaming/Mozilla/Firefox/Profiles/utuezw01.default/''')
# 为完成NTLM验证，使用firefox AutoAuth插件
# firefoxProfile.add_extension('C:/Users/LUJE4/AppData/Roaming/Mozilla/Firefox/Profiles/utuezw01.default/extensions/autoauth@efinke.com.xpi')
browser_driver = webdriver.Firefox(firefoxProfile)
browser_driver.get('http://irisqa2.oocl.com/wls_prs_doc/secured/blSop/searchBlSop/display')

# 隐性等待
browser_driver.implicitly_wait(10)
# 显性等待
locator = (By.NAME, 'com.oocl.ir4.blsop.form.customization.criteria.textfield.optId')
WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='out of time 1')
browser_driver.find_element_by_name('com.oocl.ir4.blsop.form.customization.criteria.textfield.optId').send_keys('75081')
browser_driver.find_element_by_id('com.oocl.ir4.blsop.form.customization.criteria.button.find').click()

locator = (By.XPATH, "//div[@id='fdoc.blsop.search.searchCusSop.grid.searchResults']//*[contains(text(), 'Philips Consumer Electronics - BG Hent (funloc 451501 Hent) (6648687000)')]")
WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='out of time 2')
result = browser_driver.find_element_by_xpath(xpath="//div[@id='fdoc.blsop.search.searchCusSop.grid.searchResults']//*[contains(text(), 'Philips Consumer Electronics - BG Hent (funloc 451501 Hent) (6648687000)')]")
ActionChains(browser_driver).double_click(result).perform()
print(browser_driver.current_url)
new_window_handle = browser_driver.window_handles[len(browser_driver.window_handles) - 1]
browser_driver.switch_to.window(new_window_handle)
print(browser_driver.current_url)

locator = (By.XPATH, "//div[@id='fdoc.blSop.maintain.grid.blRelGrid']//button[contains(text(), 'Add')]")
WebDriverWait(browser_driver, 20, 1).until(method=visibility_of_element_located(locator), message='can\'t find the add button')
browser_driver.find_element_by_xpath("//div[@id='fdoc.blSop.maintain.grid.blRelGrid']//button[contains(text(), 'Add')]").click()

input_field = browser_driver.find_element_by_xpath("//div[@id='fdoc.blSop.maintain.grid.blRelGrid']//input[1]")
ActionChains(browser_driver).send_keys_to_element(input_field, 'B/L Release'+Keys.TAB).perform()
locator = (By.XPATH, "//div[@id='fdoc.blsop.window.BlReleaseWindow']")
try:
    bl_window = WebDriverWait(browser_driver, 10, 1).until(method=visibility_of_element_located(locator), message='Can\'t not find the B/L Release window')
    if (bl_window):
        print('Success')
except(Exception):
    print('There is some error')

browser_driver.quit()