from flask import Flask, request, jsonify
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

app = Flask(__name__)

@app.route('/get_youtube_src', methods=['GET'])
def get_youtube_src():
    a = request.args.get('a')

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://aslteachingresources.com/dictionary/{}/".format(a))

        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[@name="fitvid0"]'))
        )

        src = iframe.get_attribute('src')

        videoidstart = src.find('/embed/') + len('/embed/')
        videoidend = src.find('?', videoidstart)
        videoid = src[videoidstart:videoidend]

        new_src = f"https://www.youtube.com/embed/{videoid}?start=4&end=3"
        return jsonify({'result': new_src})

    except NoSuchElementException:
        return jsonify({'result': 'Not Available'})

    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
