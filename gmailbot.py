from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
password = 'enter your email password'
PATH = "C:\Program Files (x86)\chromedriver.exe"
print('opening browser...')
driver = webdriver.Chrome(PATH)

driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
print(driver.title)
search = driver.find_element_by_name('identifier')
search.send_keys(input())
search.send_keys(Keys.RETURN)
time.sleep(5)
search = driver.find_element_by_name('password')
search.send_keys(password)
search.send_keys(Keys.RETURN)


#driver.quit()