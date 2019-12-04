f = open('proxies.txt', 'r', encoding='utf-8')
list = f.readlines()
proxy = list[0]
print(proxy)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
proxy = '--proxy-server=' + proxy
options.add_argument(proxy)
options.add_argument('--lang=ru_RU')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920,1080")
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get('http://2ip.ru')