# 导包
from selenium import webdriver
import time
# 创建浏览器对象
driver = webdriver.Chrome()
# 打开百度首页
driver.get("https://www.baidu.com")
# 使用绝对路径定位
driver.find_element_by_css_selector("#kw").send_keys("seleniuaaum")
time.sleep(5)
driver.find_element_by_css_selector("#kw").clear()
time.sleep(5)
driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input[@id='su']").click()
time.sleep(5)
driver.quit()