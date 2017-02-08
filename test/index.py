from common.selenium_driver import Driver
from func_module.SOP.CEL.search_CEL import Search_CEL
from test.issues.alm_operation import Operation

if __name__ == "__main__":
    # browser_driver = Driver().get_firefox_driver()
    #
    # test_search_cel = Search_CEL(browser_driver, "http://irisqa2.oocl.com/wls_prs_doc/secured/blSop/searchBlSop/display")
    # test_search_cel.search_by_id(75081)
    # browser_driver.quit()

    Operation().create_story('this is a test')
