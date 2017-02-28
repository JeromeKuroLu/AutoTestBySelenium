from common.selenium_driver import Driver
from func_module.SOP.CEL.search_CEL import Search_CEL
from test.issues.alm_operation import Operation
from pylab import *

if __name__ == "__main__":
    # browser_driver = Driver().get_firefox_driver()
    #
    # test_search_cel = Search_CEL(browser_driver, "http://irisqa2.oocl.com/wls_prs_doc/secured/blSop/searchBlSop/display")
    # test_search_cel.search_by_id(75081)
    # browser_driver.quit()

    Operation().copy_tasks_from_st('ST120556', '1231', [])


    # x, y = mgrid[-300:300, -300:300]
    # circle = Circle((0, 0), 1, alpha=0)
    # gca().add_patch(circle)
    # imshow(arctan2(x, y), cmap='hsv', extent=[-1, 1, -1, 1]).set_clip_path(circle)
    # show()