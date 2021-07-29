from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost")

# open new tabs
driver.execute_script("window.open('https://twitter.com/i/flow/signup', '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes')")
driver.execute_script("window.open('https://facebook.com')")
driver.execute_script("window.open('https://gmail.com')")


driver.switch_to.window(driver.window_handles[-2])
driver.find_element_by_id('email').send_keys("my ninja")

time.sleep(4)

driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_name('name').send_keys("my ninja")

print(driver.window_handles)
print(driver.current_window_handle)
