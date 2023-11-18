from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

a = input("Enter:")

driver.get("https://aslteachingresources.com/dictionary/{}/".format(a))

try:
    iframe = driver.find_element(By.XPATH, '//iframe[@name="fitvid0"]')
    
    src = iframe.get_attribute('src')

    print(src)

except:
    print("Not Available")

time.sleep(100)


#https://www.youtube.com/embed/yGKy5DJhE3U?start=3&end=7

#https://www.youtube.com/watch?v=yGKy5DJhE3U&ab_channel=Signs

#class : "fluid-width-video-wrappers"
#<iframe src="https://www.youtube.com/embed/QqeOLt4Kg1U?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen="" name="fitvid0" data-gtm-yt-inspected-9="true"></iframe>
