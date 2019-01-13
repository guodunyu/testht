from time import sleep

from selenium import webdriver


class Testcase():

    def setup(self):
        self.driver = webdriver.Firefox()

        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(5)


    def test001(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("你好")

    def teardown(self):

        self.driver.quit()



