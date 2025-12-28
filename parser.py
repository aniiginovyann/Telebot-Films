from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time


def parse(genre):
    driver = webdriver.Chrome()
    driver.minimize_window()
    try:
        driver.get(url=f'https://www.imdb.com/chart/top/?ref_=hm_nv_menu&genres={genre}')
        time.sleep(3)
        films = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
        film_text = ''
        for i in films:
            film_text += i.text
            film_text += '\n-------------------------\n'
        return film_text
    except Exception as ex:
        return ex.__class__.__name__