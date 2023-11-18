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


signvideo=driver.find_elements(By.CSS_SELECTOR, '')


time.sleep(100)