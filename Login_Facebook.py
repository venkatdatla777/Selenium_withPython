from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("D:\Python_Facebook\chromedriver83.exe",chrome_options=chrome_options)


# driver = webdriver.Chrome("D:\Python_Facebook\chromedriver83.exe")
driver.maximize_window()


driver.get("http://www.facebook.com")
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit   = driver.find_element_by_id("loginbutton")
username.send_keys("pavanvarmadatla444@gmail.com")
password.send_keys("pavanbabu7")
submit.click()


homePageTitle = driver.find_element_by_xpath("//span[contains(text(),'Pavan')]").text
print(homePageTitle)
print("login Success")
time.sleep(10)


driver.find_element_by_xpath("//div[@id='logoutMenu']").click()
time.sleep(10)
driver.find_element_by_xpath("//span[contains(text(),'Log Out')]").click()
print("log outed")


driver.close()
print("Browser Closed")

