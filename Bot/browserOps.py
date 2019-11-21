from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
WINDOW_SIZE = "1920,1080"
options = Options()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
#options.add_argument("--headless")
options.add_argument("--window-size=%s" % WINDOW_SIZE)
driver = webdriver.Chrome(options=options)

def process_cart_adidas(url):
    # Boot up webdriver; process adidas url
    driver.get(url)
    # If bot is in a queue, sleep until we reach processing page and can
    # actually add to cart.
    #while driver.title != 'adidas YEEZY BOOST 350 V2 STATIC NON-REFLECTIVE - STATIC | adidas US':
    time.sleep(2)
    # Get initial amount of items in bag
    items_in_bag = driver.find_element_by_class_name('glass_cart_count___1UWuC').text
    # If bag is empty, replace str with valid int value
    if items_in_bag == '':
        items_in_bag = 0
    # Cast temp, initialize constant
    items_in_bag = int(items_in_bag)
    UPDATED = items_in_bag + 1
    # Grab CSS to "Add to Bag" button
    btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag')
    # While bag has not updated, add to bag
    while items_in_bag != UPDATED:
        btn.click()
        time.sleep(0.5)
        items_in_bag = driver.find_element_by_css_selector('.glass_cart_count___1UWuC').text
        if items_in_bag == '':
            items_in_bag = 0
        items_in_bag = int(items_in_bag)
    # Allocate time to process item bagging (avoid unexpected error pg.)
    #time.sleep(2)
    # Navigate to Checkout page
    driver.get('https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/CODelivery-Start')


def autofill_shipping_adidas():
    # Read client info from file.
    with open('ClientInfo.txt', 'r') as file:
        # Autofill information

        driver.find_element_by_id("dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName").send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName').send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_city').send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip').send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1').send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_houseNumber').send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_apartmentNumber').send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone').send_keys(file.readline())
        driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress').send_keys(file.readline())

    driver.find_element_by_xpath('//*[@id="dwfrm_delivery"]/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/span').click()
    time.sleep(0.5)
    # Send to payment screen.
    driver.find_elements_by_xpath('//*[@id="dwfrm_delivery_savedelivery"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="dwfrm_delivery_savedelivery"]')

def autofill_card_adidas():
    # Read in card information from file.
    with open('CardInfo.txt', 'r') as card:
        # Autofill form.
        driver.find_element_by_id('dwfrm_payment_creditCard_number').send_keys(card.readline())
        driver.find_element_by_id('dwfrm_payment_creditCard_cvn').send_keys(card.readline())
        m = (card.readline()).replace('\n', '')
        y = (card.readline()).replace('\n', '')
    # Open dropdown menus; get months & years
    driver.find_element_by_id('dwfrm_payment_creditCard_month_display_field').click()
    driver.find_element_by_id('dwfrm_payment_creditCard_year_display_field').click()
    list = driver.find_elements_by_class_name('materialize-select-list')
    months = list[0].find_elements_by_css_selector('*')
    years = list[1].find_elements_by_css_selector('*')
    # Select month
    for month in months:
        if month.text == m:
            month.click()
    # Select year
    for year in years:
        if year.text == y:
            year.click()
