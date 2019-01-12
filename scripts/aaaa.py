from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(10)
sleep(5)
driver.quit()