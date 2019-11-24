from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from timer import checktime
import time
from now import now
import requests
import json
import threading
import time
from UserAgentRandom import LoadHeader
from concurrent.futures import ThreadPoolExecutor as Pool
import re
from random_proxy import RandomProxy
from now import now
thread = 1
#model = str(input('Model: '))
model = "FW4843"
print(now() ,'-', 'Use selected model:', model)
size = "2.5"
print(now() ,'-', 'Use selected size:', size)
#size = str(input('Shoe size: '))
open('timerfile.txt', 'w').close()
f = open("timerfile.txt","a+")
f.write(now())
f.write('*')
f.close()
thread_count = 8
print(now() ,'-', 'Bot started')
def url_gen(model,size):
    BaseSize = 580
    ShoeSize = float(size) - 6
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    url = 'https://www.adidas.ru/yeezy/' + model + '.html?forceSelSize=' + model + '_' + str(int(RawSize))
    print(now() ,'-', 'Url created')
    return url
url = url_gen(model,size)
# :param model specific model of sneaker
# :return size_lookup dictionary of sizes/availability

# Sets up bot environment to automate purchase sneaker if available.
# :param size specific size for purchase
def sneaker_bot(model,size):
    print(now() ,'-', 'Your size is found, start the purchase phase')
    process_cart_adidas(url)
    autofill_shipping_adidas()
    autofill_card_adidas()

# Allows for multitreading in order to purchase all sizes
# specified in size list)
#browserOps.driver.quit()
options = Options()
PROXY = str(RandomProxy()) # IP:PORT or HOST:PORT
options.add_argument('--proxy-server=http://%s' % PROXY)
options.add_argument('--lang=ru_RU') 
options.add_argument('--no-proxy-server')
options.add_argument("--window-size=1920,1080")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
actions = ActionChains(driver)
print('----------------------------------LOG FILE----------------------------------')
print(now() ,'-', 'Webdriver in headless mode launched succesefully')
def process_cart_adidas(url):
    # Boot up webdriver; process adidas url
    driver.get(url)
    print(now() ,'-', 'Transfer on item page')
    # Grab CSS to "Add to Bag" button
    try:
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]'))
    )
    except:
        print(now() ,'-', 'You now in virtual queue, repeating attempt.')
        process_cart_adidas(url)
    finally:
        btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]')
        btn.click()
    sizes = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/ul')
    sizeObj = sizes.find_elements_by_tag_name('li')
    for obj in sizeObj:
        if str(str(size) + ' UK') in obj.text:
            obj.click()
    print(now() ,'-', 'Processing cart')
    Add_To_Cart = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/button')
    Add_To_Cart.click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="dialogcontainer"]/div/a[1]'))
    )
    finally:
        GeoCheck = driver.find_element_by_xpath(
                '//*[@id="dialogcontainer"]/div/a[1]')
        GeoCheck.click()
    print(now() ,'-', 'Processing forward on shipping page')
    # Navigate to Checkout page
    driver.get('https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/CODelivery-Start')


def autofill_shipping_adidas():
    # Read client info from file.
    print(now() ,'-', 'Begin autofill')
    with open('ClientInfo.txt', 'r') as file:
        # Autofill information
        try:
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName"))
            )
        finally:
            print(now() ,'-', 'Autofilling firstname field')
            driver.find_element_by_id("dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName").send_keys(file.readline())
            print(now() ,'-', 'Autofilling lastname field')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName').send_keys(file.readline())
            print(now() ,'-', 'Autofilling adress field')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_city').send_keys(file.readline())
            print(now() ,'-', 'Autofilling zipcode field')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip').send_keys(file.readline())
            print(now() ,'-', 'Autofilling street field')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1').send_keys(file.readline())
            print(now() ,'-', 'Autofilling house number field')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_houseNumber').send_keys(file.readline())
            print(now() ,'-', 'Autofilling apartament number field')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_apartmentNumber').send_keys(file.readline())
            print(now() ,'-', 'Autofilling phone form')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone').send_keys(file.readline())
            print(now() ,'-', 'Autofilling email form')
            driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress').send_keys(file.readline())
    print(now() ,'-', 'Accepting privacy policy')
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="dwfrm_delivery"]/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/span').click()
    print(now() ,'-', 'Processing forward on billing page')
    #driver.find_elements_by_css_selector('#dwfrm_delivery_savedelivery')
    driver.get('https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/COSummary2-Start')
def autofill_card_adidas():
    # Read in card information from file.
    print(now() ,'-', 'Autofilling billing information')
    with open('CardInfo.txt', 'r') as card:
        try:
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "dwfrm_adyenencrypted_number"))
            )
        finally:
            print(now() ,'-', 'Autofilling card number begin')
            driver.find_element_by_id('dwfrm_adyenencrypted_number').send_keys(card.readline())
            print(now() ,'-', 'Autofilling card cvc begin')
            driver.find_element_by_id('dwfrm_adyenencrypted_cvc').send_keys(card.readline())
        m = (card.readline()).replace('\n', '')
        y = (card.readline()).replace('\n', '')
    print(now() ,'-', 'Autofilling mounth/year')
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "month", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ffSelectButton", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "month", " " ))]//span').click()
    listx = driver.find_elements_by_xpath('//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div')
    months = listx[0].find_elements_by_class_name('selectoption')
    for month in months:
        if month.text == m:
            month.click()

    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "nobr", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ffSelectButton", " " ))]').click()
    listy = driver.find_elements_by_xpath('//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[3]/div/div/div/div/div[2]/div')
    years = listy[0].find_elements_by_class_name('selectoption')
    for year in years:
        if year.text == y:
            year.click()
    print(now() ,'-', 'Autofilling billing information success!')
    finalbutton = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[5]/div/button')
    for btn in finalbutton:
        btn.click()
    print(now() ,'-', 'Closing webdriver')
    driver.quit()
    f = open('timerfile.txt', 'a+')
    f.write(now())
    f.close()
    print(now() ,'-', 'Bot work finished in', checktime(), 'seconds')
sneaker_bot(model,size)