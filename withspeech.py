import time
import speech_recognition as sr
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source, timeout=5)  
        print("Got it! Now recognizing...")

    a = recognizer.recognize_google(audio)
    print("You said: " + a)

    driver.get("https://asl-lex.org/visualization/index.html?sign={}".format(a))

    time.sleep(50)

except sr.UnknownValueError:
    print("Sorry, couldn't understand what you said.")

except sr.RequestError as e:
    print(f"Couldn't request results from Google Speech Recognition service; {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
