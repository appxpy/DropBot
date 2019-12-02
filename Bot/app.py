def launch_yeezy(model, size, thread_num, proxy):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    import random
    from numpy import arange
    import requests
    import json
    import time
    import re
    import datetime
    from threading import Semaphore
    screen_lock = Semaphore(value=1)
    def now():
        now = datetime.datetime.now()
        prefix = str('[THREAD:' + str(thread_num) + '] - ')
        result = prefix + now.strftime("%X")
        return result
    def randomTime():
        timelist = list(arange(0, 1, 0.05))
        result = random.choice(timelist)
        return result
    f = open('config.txt', 'r')
    cfgline = f.readlines()
    options = Options()
    if proxy != 0:
        screen_lock.acquire()
        time.sleep(randomTime())
        print(now(), '-', 'Using proxy:', proxy, 'time:', randomTime())
        screen_lock.release()
        options.add_argument('--proxy-server=http://%s' % proxy)
    else:
        options.add_argument('--no-proxy-server')
    options.add_argument('--lang=ru_RU')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    print(now(), '-', 'Webdriver in headless mode launched succesefully')
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua
        }
    def checktime():
        f = open('timerfile.txt', 'r')
        s = f.read()
        timelist = []
        strtimelist = s.split('*')
        for date in strtimelist:
            time = datetime.datetime.strptime(date,"%H:%M:%S")
            timelist.append(time)
        delta = timelist[1] - timelist[0]
        f.close()
        open('timerfile.txt', 'w').close()
        return int(delta.total_seconds())

    def main(model, size):
        print(now(), '-', 'Use selected model:', model)
        print(now(), '-', 'Use selected size:', size)
        print(now(), '-', 'Bot started')
        # size = str(input('Shoe size: '))
        sneaker_bot(model, size)

    def url_gen(model, size):
        BaseSize = 580
        ShoeSize = float(size) - 6
        ShoeSize = ShoeSize * 20
        RawSize = ShoeSize + BaseSize
        url = 'https://www.adidas.ru/yeezy/' + model + \
            '.html?forceSelSize=' + model + '_' + str(int(RawSize))
        print(now(), '-', 'Url created')
        return url

    def check_stock(model):
        # ua = LoadHeader()
        # CheckSite = requests.get('https://adidas.ru', headers=headers)
        # print(now() ,'-', 'Recieved response from server with code', CheckSite.status_code)
        size_url = 'https://www.adidas.ru/api/products/{}/availability'.format(
            model)
        raw_sizes = requests.get(size_url, headers=headers)
        size_data = json.loads(raw_sizes.text)
        try:
             while size_data['availability_status'] == 'PREVIEW':
                 raw_sizes = requests.get(size_url, headers=headers)
                 size_data = json.loads(raw_sizes.text)
                 print(now(), '-', 'Availability status - PREVIEW. Continue sending json requests to:', size_url)
                 time.sleep(5)
        except:
            print(now(), '-', 'API error occured. Your model is not valid.')
            print(now(), '-', 'Bot stopped with exit code 1')
            exit()
        print(now(), '-', 'Recieved response from server API with code',
              raw_sizes.status_code)
        print(now(), '-', 'Availability status IN_STOCK')
        list = size_data['variation_list']
        size_dict = {}
        size_lookup = {}
        sizes_list = []
        for i in range(21):
            size_dict[i] = {list[i]['size']: list[i]['availability_status']}
        for key, value in size_dict.items():
            size_lookup.update(value)
        for key in size_lookup.keys():
            x = re.compile('\d*\.?\d\sUK')
            x1 = x.search(str(key)).group(0)
            x1 = x1.replace(' UK', '')
            # x1 = float(x1) + 0.5
            # x1 = str('{0:g}'.format(x1))
            sizes_list.append(x1)
        value_list = size_lookup.values()
        size_lookup = dict(zip(sizes_list, value_list))
        print(now(), '-', 'Created size list based on API')
        return size_lookup

    def sneaker_bot(model, size):
        sizes = check_stock(model)
        # print(sizes)
        url = url_gen(model, size)
        if str(size) in sizes:
            if str(sizes[str(size)]) == 'IN_STOCK':
                print(now(), '-', 'Your size is found, start the purchase phase')
                process_cart_adidas(url, size)
                autofill_shipping_adidas()
                autofill_card_adidas()
            else:
                print(now(), '-', 'Your size is not available')
        else:
            print(now(), '-', 'During to API error we are not able to save you a pair')

    def process_cart_adidas(url, size):
        # Boot up webdriver; process adidas url
        driver.get(url)
        try:
        	page = requests.get(url, headers=headers)
        except:
        	print(now(), '-', 'Internet or proxy error occured')
        	exit()
        print(now(), '-', 'Transfer on item page')
        # Grab CSS to "Add to Bag" button
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]'))
            )
        except:
            print(now(), '-', 'You now in virtual queue or model is not dropping')
            process_cart_adidas(url, size)

        finally:
            open('timerfile.txt', 'w').close()
            f = open("timerfile.txt", "a+")
            f.write(now())
            f.write('*')
            f.close()
            btn = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]')
            btn.click()
        sizes = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/ul')
        sizeObj = sizes.find_elements_by_tag_name('li')
        for obj in sizeObj:
            if str(str(size) + ' UK') in obj.text:
                obj.click()
        print(now(), '-', 'Processing cart')
        Add_To_Cart = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/button')
        Add_To_Cart.click()
        f = open('timerfile.txt', 'a+')
        f.write(now())
        f.close()
        print(now(), '-', 'Bot succesefully secured your item in', checktime(), 'seconds')
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="dialogcontainer"]/div/a[1]'))
            )
        except:
            print(now(), '-', 'Geo checker not founded. Continue...')
        else:
                GeoCheck = driver.find_element_by_xpath(
                    '//*[@id="dialogcontainer"]/div/a[1]')
                GeoCheck.click()
                print(now(), '-', 'Geo checker founded. Continue...')
        print(now(), '-', 'Processing forward on shipping page')
        # Navigate to Checkout page
        driver.get(
            'https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/CODelivery-Start')
        print(now(), '-', 'Bot work finished in', checktime(), 'seconds')
    def autofill_shipping_adidas():
        # Read client info from file.
        print(now(), '-', 'Begin autofill')
        with open('config.txt', 'r', encoding='utf-8') as file:
            # Autofill information
            cfgline = file.readlines()
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located(
                        (By.ID, "dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName"))
                )
            except:
                print(now(), '-', 'Adress fields could not founded. Please update your chrome to the newest one and check chromedriver in PATH')
                exit()
            finally:
                print(now(), '-', 'Autofilling firstame field')
                textfield = cfgline[3]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    "dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName").send_keys(textfield)
                print(now(), '-', 'Autofilling lastname field')
                textfield = cfgline[4]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName').send_keys(textfield)
                print(now(), '-', 'Autofilling adress field')
                textfield = cfgline[5]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_city').send_keys(textfield)
                print(now(), '-', 'Autofilling zipcode field')
                textfield = cfgline[6]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip').send_keys(textfield)
                print(now(), '-', 'Autofilling street field')
                textfield = cfgline[7]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1').send_keys(textfield)
                print(now(), '-', 'Autofilling house number field')
                textfield = cfgline[8]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_houseNumber').send_keys(textfield)
                print(now(), '-', 'Autofilling apartament number field')
                textfield = cfgline[9]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_apartmentNumber').send_keys(textfield)
                print(now(), '-', 'Autofilling phone form')
                textfield = cfgline[10]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone').send_keys(textfield)
                print(now(), '-', 'Autofilling email form')
                textfield = cfgline[11]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress').send_keys(textfield)
        print(now(), '-', 'Accepting privacy policy')
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="dwfrm_delivery"]/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/span').click()
        print(now(), '-', 'Processing forward on billing page')
        # driver.find_elements_by_css_selector('#dwfrm_delivery_savedelivery')
        driver.get(
            'https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/COSummary2-Start')

    def autofill_card_adidas():
        # Read in card information from file.
        print(now(), '-', 'Autofilling billing information')
        with open('config.txt', 'r', encoding='utf-8') as card:
            cfgline = file.readlines()
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located(
                        (By.ID, "dwfrm_adyenencrypted_number"))
                )
            finally:
                print(now(), '-', 'Autofilling holder name')
                textfield = cfgline[13]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_adyenencrypted_holderName').send_keys(textfield)
                print(now(), '-', 'Autofilling card number')
                textfield = cfgline[12]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_adyenencrypted_number').send_keys(textfield)
                print(now(), '-', 'Autofilling card cvc')
                textfield = cfgline[16]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_adyenencrypted_cvc').send_keys(textfield)
            textfield = cfgline[14]
            pattern = re.compile('".*?"')
            textfield = pattern.search(textfield).group(0)
            textfield = textfield.replace('"', '')
            m = (textfield).replace('\n', '')
            textfield = cfgline[15]
            pattern = re.compile('".*?"')
            textfield = pattern.search(textfield).group(0)
            textfield = textfield.replace('"', '')
            y = (textfield).replace('\n', '')
        print(now(), '-', 'Autofilling mounth/year')
        driver.find_element_by_xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "month", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ffSelectButton", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "month", " " ))]//span').click()
        listx = driver.find_elements_by_xpath(
            '//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div')
        months = listx[0].find_elements_by_class_name('selectoption')
        for month in months:
            if month.text == m:
                month.click()

        driver.find_element_by_xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "nobr", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "ffSelectButton", " " ))]').click()
        listy = driver.find_elements_by_xpath(
            '//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[3]/div/div/div/div/div[2]/div')
        years = listy[0].find_elements_by_class_name('selectoption')
        for year in years:
            if year.text == y:
                year.click()
        print(now(), '-', 'Autofilling billing information success!')
        finalbutton = driver.find_elements_by_xpath(
            '//*[@id="content"]/div/div[1]/div[5]/div/button')
        for btn in finalbutton:
            btn.click()
        print(now(), '-', 'Closing webdriver')
        exit()
    main(model, size)
if __name__ == '__main__':
    def now():
        now = datetime.datetime.now()
        return  now.strftime("%X")
    print( 
            '|----------------------------------LOG----------------------------------|')
    import re
    import datetime
    from multiprocessing import Process
    from threading import Thread
    from threading import Semaphore
    f = open('config.txt', 'r')
    cfgline = f.readlines()
    f.close()
    # model = str(input('Model: '))
    model = cfgline[1]
    pattern = re.compile('".*?"')
    model = pattern.search(model).group(0)
    model = model.replace('"', '')
    sizes = cfgline[2]
    pattern = re.compile('".*?"')
    sizes = pattern.search(sizes).group(0)
    sizes = sizes.replace('"', '')
    f = open('proxies.txt')
    prx = f.readlines()
    f.close()
    if '"y"' in cfgline[17]:
        print(now(), 'Creating thread pool...')
        try:
            thread_count = len(sizes.split(','))
            sizes = sizes.split(',')
            if int(thread_count) == 1:
                print(now(), 'You entered only one size.')
                exit()
            if int(thread_count) > len(prx):
                print(now(), 'You should have minimum', thread_count, 'proxies to start bot.')
                exit()
        except:
            print('You should write size for each pair comma separated in quotation marks')
            exit()
        else:
            print(now(), 'Initializing threads with input arguments...')
            thread_num = 0
            for size in sizes:
                thread_num += 1
                proxy = prx[thread_num - 1]
                if '\n' in proxy:
                    proxy = proxy.replace('\n', '')
                proc = Thread(target=launch_yeezy, args=(model,size,thread_num,proxy))
                proc.start()
    else:
        size = sizes
        if len(size) > 3:
            print(now(), 'Fatal error. Check your field number 17')
            exit()
        thread_num = 1
        proxy = 0
        launch_yeezy(model, size, thread_num,proxy)
    