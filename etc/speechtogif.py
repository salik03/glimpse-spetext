from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://aslteachingresources.com/dictionary/")

words=driver.find_elements(By.CSS_SELECTOR,"li.ln-0.paginated")


for i in words:
    anchor_tag = i.find_element(By.CSS_SELECTOR, "a")
    href_value = anchor_tag.get_attribute("href")
    print(href_value)



time.sleep(100)