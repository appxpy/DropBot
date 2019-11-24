from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random_proxy import RandomProxy
from timer import checktime
import time
from now import now
print('----------------------------------LOG FILE----------------------------------')
f = open('config.txt', 'r')
cfgline = f.readlines()
options = Options()
if '1' in cfgline[0]:
    print(now() ,'-', 'Using proxy')
    PROXY = str(RandomProxy())
    options.add_argument('--proxy-server=http://%s' % PROXY)
options.add_argument('--lang=ru_RU')

options.add_argument("--window-size=1920,1080")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
actions = ActionChains(driver)
print(now() ,'-', 'Webdriver in headless mode launched succesefully')
