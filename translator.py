from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

web = webdriver.Chrome(options=options)
web.get('https://papago.naver.com/')

time.sleep(2) #give time for browser to load

def translate(text):
    text_content = text
    text_area = web.find_element_by_xpath('//*[@id="txtSource"]')
    text_area.send_keys(text_content)
    time.sleep(2)
    translated = web.find_element_by_xpath('//*[@id="txtTarget"]/span')
    return translated.text