from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

links = [
    "https://aslteachingresources.com/dictionary/hello/",
    "https://aslteachingresources.com/dictionary/goodbye/",
    "https://aslteachingresources.com/dictionary/thank-you/",
    "https://aslteachingresources.com/dictionary/please/",
    "https://aslteachingresources.com/dictionary/sorry/",
    "https://aslteachingresources.com/dictionary/excuse-me/",
    "https://aslteachingresources.com/dictionary/yes/",
    "https://aslteachingresources.com/dictionary/no/",
    "https://aslteachingresources.com/dictionary/love/",
    "https://aslteachingresources.com/dictionary/friend/",
    "https://aslteachingresources.com/dictionary/family/",
    "https://aslteachingresources.com/dictionary/home/",
    "https://aslteachingresources.com/dictionary/school/",
    "https://aslteachingresources.com/dictionary/work/",
    "https://aslteachingresources.com/dictionary/play/",
    "https://aslteachingresources.com/dictionary/eat/",
    "https://aslteachingresources.com/dictionary/drink/",
    "https://aslteachingresources.com/dictionary/sleep/",
    "https://aslteachingresources.com/dictionary/bathroom/",
    "https://aslteachingresources.com/dictionary/help/",
    "https://aslteachingresources.com/dictionary/understand/",
    "https://aslteachingresources.com/dictionary/learn/",
    "https://aslteachingresources.com/dictionary/teach/",
    "https://aslteachingresources.com/dictionary/want/",
    "https://aslteachingresources.com/dictionary/need/",
    "https://aslteachingresources.com/dictionary/like/",
    "https://aslteachingresources.com/dictionary/dislike/",
    "https://aslteachingresources.com/dictionary/happy/",
    "https://aslteachingresources.com/dictionary/sad/",
    "https://aslteachingresources.com/dictionary/angry/",
    "https://aslteachingresources.com/dictionary/laugh/",
    "https://aslteachingresources.com/dictionary/cry/",
    "https://aslteachingresources.com/dictionary/beautiful/",
    "https://aslteachingresources.com/dictionary/ugly/",
    "https://aslteachingresources.com/dictionary/hot/",
    "https://aslteachingresources.com/dictionary/cold/",
    "https://aslteachingresources.com/dictionary/more/",
    "https://aslteachingresources.com/dictionary/less/",
    "https://aslteachingresources.com/dictionary/finish/",
    "https://aslteachingresources.com/dictionary/start/",
    "https://aslteachingresources.com/dictionary/time/",
    "https://aslteachingresources.com/dictionary/money/",
    "https://aslteachingresources.com/dictionary/busy/",
    "https://aslteachingresources.com/dictionary/relax/",
    "https://aslteachingresources.com/dictionary/wait/",
    "https://aslteachingresources.com/dictionary/watch/",
    "https://aslteachingresources.com/dictionary/listen/",
    "https://aslteachingresources.com/dictionary/read/",
    "https://aslteachingresources.com/dictionary/write/",
    "https://aslteachingresources.com/dictionary/sign/"
]


youtube_links = [] 

for i in links:
    driver.get(i)


    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[@name="fitvid0"]'))
        )

        src = iframe.get_attribute('src')

        videoidstart = src.find('/embed/') + len('/embed/')
        videoidend = src.find('?', videoidstart)
        videoid = src[videoidstart:videoidend]

        new_src = f"https://www.youtube.com/embed/{videoid}?start=4&end=3"
        
        youtube_links.append(new_src)


    except Exception as e:
        continue



with open('youtube_links.txt', 'w') as file:
    for j in youtube_links:
        file.write(j + '\n')
