import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pymysql
import zipfile
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import pandas as pd

val = 0
def create_session(page):
    global val
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    data = 24
    driver = webdriver.Chrome(options=options)
    url = f'https://www.carrefour.es/search-api/query/v1/search?query=bebidas+alcoholicas&scope=desktop&lang=es&session=c12ddee4-2cd6-4026-b677-bde867f778fb&rows={data}&start={val}&origin=linked&f.op=OR'
    print(url)
    driver.get(url)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    val += 24

    return driver

lis = []

for i in range(0, 25):
    driver1 = create_session(i)
    j = driver1.find_element(By.XPATH, '//pre').text
    json_data = json.loads(j)
    for j in json_data['content']['docs']:
        lis.append(f'https://www.carrefour.es{j["url"]}')
    driver1.close()
    print('\n')

print(lis)

df = pd.DataFrame(lis)

df.to_excel('www_carrefour_es.xlsx')






