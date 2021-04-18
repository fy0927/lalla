# 导包
# 创建浏览器对象
# 获取url地址
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

# 通过ID来定位文本框和百度一下
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)
driver.find_element_by_id("su").click()

time.sleep(2)

driver.quit()




