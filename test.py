from selenium import webdriver
import time
driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
driver.get('https://www.facebook.com')
driver.find_element_by_id('email').send_keys('143asd')
driver.find_element_by_id('pass').send_keys('chinnu143')
driver.find_element_by_id('loginbutton').click()