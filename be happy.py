from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

a = input("Enter:")

driver.get("https://aslteachingresources.com/dictionary/{}/".format(a))


try:
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@name="fitvid0"]'))
    )

    src = iframe.get_attribute('src')

    videoidstart = src.find('/embed/') + len('/embed/')
    videoidend = src.find('?', videoidstart)
    videoid = src[videoidstart:videoidend]

    new_src = f"https://www.youtube.com/embed/{videoid}?start=4&end=3"
    
    print(new_src)

except NoSuchElementException:
    print("Not Available")

finally:
    driver.quit()
