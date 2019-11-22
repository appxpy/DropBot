from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from now import now
options = Options()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
print(now() ,'-', 'Webdriver started succesefully')
def process_cart_adidas(url):
    # Boot up webdriver; process adidas url
    driver.get(url)
    try:
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "glass_cart_count___1UWuC"))
    )
    except:
        print(now() ,'-', 'Timeout error occured')
    finally:
        items_in_bag = driver.find_element_by_class_name('glass_cart_count___1UWuC').text
    # If bag is empty, replace str with valid int value
    if items_in_bag == '':
        items_in_bag = 0
    # Cast temp, initialize constant
    items_in_bag = int(items_in_bag)
    UPDATED = items_in_bag + 1
    # Grab CSS to "Add to Bag" button
    try:
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag"))
    )
    except:
        print(now() ,'-', 'Timeout error occured')
    finally:
        btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag').click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "gl-cta.gl-cta--secondary.gl-cta--full-width"))
    )
    finally:
        BuyButton = driver.find_element_by_class_name(
                "gl-cta.gl-cta--secondary.gl-cta--full-width")
        BuyButton.click()
        print('Clicked')
    # Navigate to Checkout page
    #driver.get('https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/CODelivery-Start')


def autofill_shipping_adidas():
    # Read client info from file.
    with open('ClientInfo.txt', 'r') as file:
        # Autofill information
        try:
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName"))
            )
        finally:
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
    driver.find_elements_by_css_selector('#dwfrm_delivery_savedelivery')
    driver.get('https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/COSummary2-Start')
def autofill_card_adidas():
    # Read in card information from file.
    with open('CardInfo.txt', 'r') as card:
        driver.find_element_by_id('dwfrm_adyenencrypted_number').send_keys(card.readline())
        driver.find_element_by_id('dwfrm_adyenencrypted_cvc').send_keys(card.readline())
        m = (card.readline()).replace('\n', '')
        y = (card.readline()).replace('\n', '')
    # Open dropdown menus; get months & years
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "month", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ffSelectButton", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "month", " " ))]//span').click()
    list = driver.find_elements_by_xpath('//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div')
    months = list[0].find_elements_by_class_name('selectoption')
    print(months)
    for month in months:
        if month.text == m:
            month.click()
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "nobr", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ffSelectButton", " " ))]').click()
    list = driver.find_elements_by_xpath('//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[3]/div/div/div/div/div[2]/div')
    
    years = list[0].find_elements_by_css_selector('selectoption')
    # Select month
    
    # Select year
    for year in years:
        if year.text == y:
            year.click()
