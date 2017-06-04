#! python3
#seleniumPrac.py - selenium practice

import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')

browser = webdriver.Firefox(firefox_binary=binary)

browser.get('http://gmail.com')


emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('iggs.piggy@gmail.com')

buttonElem = browser.find_element_by_id('next')
buttonElem.click()

time.sleep(1.5)

passElem = browser.find_element_by_id('Passwd')
passElem.click()
passElem.send_keys('Pass')

signIn = browser.find_element_by_id('signIn')
signIn.click()





#firefox_capabilities['marionette'] = True
#firefox_capabilities['binary'] = "C:\\Users\\Igor\\Desktop\\firefox-47.0.win64.sdk\\firefox-sdk\\bin\\firefox.exe"
#browser = webdriver.Firefox(capabilities=firefox_capabilities)
#the_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
#ffpath = "C:\\Users\\Igor\\Desktop\\firefox-47.0.win64.sdk\\firefox-sdk\\bin\\firefox.exe"
#browser = webdriver.Firefox(executable_path=ffpath)
#browser = webdriver.Firefox()
#time.sleep(5)


