def launch_yeezy(model, size, thread_num, proxy):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    import random
    import requests
    import json
    import time
    import re
    import datetime
    import sys
    def nowINFO():
        now = datetime.datetime.now()
        if len(str(thread_num)) >= 2:
            prefix = str(' - [ID:' + str(thread_num) + '/INFO]')
        else:
            prefix = str(' - [ID:0' + str(thread_num) + '/INFO]')
        result = now.strftime("%X") + prefix
        return result
    def nowERROR():
        now = datetime.datetime.now()
        if len(str(thread_num)) >= 2:
            prefix = str(' - [ID:' + str(thread_num) + '/ERROR]')
        else:
            prefix = str(' - [ID:0' + str(thread_num) + '/ERROR]')
        result = now.strftime("%X") + prefix
        return result
    f = open('config.txt', 'r')
    cfgline = f.readlines()
    options = Options()
    if proxy != 0:
        print(nowINFO(), '-', 'Using proxy:', proxy)
        options.add_argument('--proxy-server=http://%s' % proxy)
    else:
        options.add_argument('--no-proxy-server')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--lang=ru_RU')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    options.add_argument("--headless")
    if sys.platform.startswith('win32'):
        driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
        print(nowINFO(), '-', 'Webdriver in headless mode for windows launched succesefully')
    else:
        driver = webdriver.Chrome(options=options, executable_path='chromedriver')
        print(nowINFO(), '-', 'Webdriver in headless mode for UNIX systems launched succesefully')
    driver.delete_all_cookies()
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
        print(nowINFO(), '-', 'Use selected model:', model)
        print(nowINFO(), '-', 'Use selected size:', size)
        print(nowINFO(), '-', 'Bot started')
        sneaker_bot(model, size)

    def url_gen(model, size):
        BaseSize = 580
        ShoeSize = float(size) - 6
        ShoeSize = ShoeSize * 20
        RawSize = ShoeSize + BaseSize
        url = 'https://www.adidas.ru/yeezy/' + model + \
            '.html?forceSelSize=' + model + '_' + str(int(RawSize))
        print(nowINFO(), '-', 'Url created')
        return url

    def check_stock(model):
        size_url = 'https://www.adidas.ru/api/products/{}/availability'.format(
            model)
        try:
            raw_sizes = requests.get(size_url, headers=headers)
        except:
            print(nowERROR(), '-', 'Proxy error occured. Check your internet connection or authorized ip on your proxy server')
            print(nowERROR(), '-', 'Bot stopped with exit code 1')
            driver.quit()
            exit()
        size_data = json.loads(raw_sizes.text)
        try:
            request_counter = 1
            while size_data['availability_status'] == 'PREVIEW':
                 raw_sizes = requests.get(size_url, headers=headers)
                 size_data = json.loads(raw_sizes.text)
                 print(nowINFO(), '-', 'Availability status - PREVIEW. Continue sending json request number', request_counter,'to:', size_url + '.')
                 request_counter += 1
                 time.sleep(5)
        except:
            print(nowERROR(), '-', 'API or Internet connection error occured')
            print(nowERROR(), '-', 'Bot stopped with exit code 1')
            driver.quit()
            exit()
        print(nowINFO(), '-', 'Recieved response from server API with code',
              raw_sizes.status_code)
        print(nowINFO(), '-', 'Availability status IN_STOCK')
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
        print(nowINFO(), '-', 'Created size list based on API')
        return size_lookup

    def sneaker_bot(model, size):
        sizes = check_stock(model)
        # print(sizes)
        url = url_gen(model, size)
        if str(size) in sizes:
            if str(sizes[str(size)]) == 'IN_STOCK':
                print(nowINFO(), '-', 'Your size is found, start the purchase phase')
                process_cart_adidas(url, size)
                autofill_shipping_adidas()
                autofill_card_adidas()
            else:
                print(nowERROR(), '-', 'Your size is not available')
        else:
            print(nowERROR(), '-', 'During to API error we are not able to save you a pair')

    def process_cart_adidas(url, size):
        # Boot up webdriver; process adidas url
        driver.get(url)
        try:
        	page = requests.get(url, headers=headers)
        except:
            print(nowERROR(), '-', 'Internet or proxy error occured')
            driver.quit()
            exit()
        print(nowINFO(), '-', 'Transfer on item page')
        # Grab CSS to "Add to Bag" button
        try:
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]'))
            )
        except:
            print(nowINFO(), '-', 'You now in virtual queue or model is not dropping')
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
        print(nowINFO(), '-', 'Processing cart')
        Add_To_Cart = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[2]/button')
        Add_To_Cart.click()
        f = open('timerfile.txt', 'a+')
        f.write(now())
        f.close()
        print(nowINFO(), '-', 'Bot succesefully secured your item in', checktime(), 'seconds')
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="dialogcontainer"]/div/a[1]'))
            )
        except:
            print(nowINFO(), '-', 'Geo checker not founded. Continue...')
        else:
                GeoCheck = driver.find_element_by_xpath(
                    '//*[@id="dialogcontainer"]/div/a[1]')
                GeoCheck.click()
                print(nowINFO(), '-', 'Geo checker founded. Continue...')
        print(nowINFO(), '-', 'Processing forward on shipping page')
        # Navigate to Checkout page
        driver.get(
            'https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/CODelivery-Start')
        print(nowINFO(), '-', 'Bot work finished in', checktime(), 'seconds')
    def autofill_shipping_adidas():
        # Read client info from file.
        print(nowINFO(), '-', 'Begin autofill')
        with open('config.txt', 'r', encoding='utf-8') as file:
            # Autofill information
            cfgline = file.readlines()
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located(
                        (By.ID, "dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName"))
                )
            except:
                print(nowERROR(), '-', 'Adress fields could not founded. Please update your chrome to the newest one and check chromedriver in PATH')
                driver.quit()
                exit()
            finally:
                print(nowINFO(), '-', 'Autofilling firstame field')
                textfield = cfgline[3]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    "dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName").send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling lastname field')
                textfield = cfgline[4]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling adress field')
                textfield = cfgline[5]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_city').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling zipcode field')
                textfield = cfgline[6]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling street field')
                textfield = cfgline[7]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling house number field')
                textfield = cfgline[8]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_houseNumber').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling apartament number field')
                textfield = cfgline[9]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_apartmentNumber').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling phone form')
                textfield = cfgline[10]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling email form')
                textfield = cfgline[11]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress').send_keys(textfield)
        print(nowINFO(), '-', 'Accepting privacy policy')
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="dwfrm_delivery"]/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/span').click()
        print(nowINFO(), '-', 'Processing forward on billing page')
        # driver.find_elements_by_css_selector('#dwfrm_delivery_savedelivery')
        driver.get(
            'https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/COSummary2-Start')

    def autofill_card_adidas():
        # Read in card information from file.
        print(nowINFO(), '-', 'Autofilling billing information')
        with open('config.txt', 'r', encoding='utf-8') as card:
            cfgline = file.readlines()
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located(
                        (By.ID, "dwfrm_adyenencrypted_number"))
                )
            finally:
                print(nowINFO(), '-', 'Autofilling holder name')
                textfield = cfgline[13]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_adyenencrypted_holderName').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling card number')
                textfield = cfgline[12]
                pattern = re.compile('".*?"')
                textfield = pattern.search(textfield).group(0)
                textfield = textfield.replace('"', '')
                driver.find_element_by_id(
                    'dwfrm_adyenencrypted_number').send_keys(textfield)
                print(nowINFO(), '-', 'Autofilling card cvc')
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
        print(nowINFO(), '-', 'Autofilling mounth/year')
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
        print(nowINFO(), '-', 'Autofilling billing information success!')
        finalbutton = driver.find_elements_by_xpath(
            '//*[@id="content"]/div/div[1]/div[5]/div/button')
        for btn in finalbutton:
            btn.click()
        print(nowINFO(), '-', 'Closing webdriver')
        driver.quit()
        exit()
    main(model, size)
if __name__ == '__main__':
    def nowERROR():
        import datetime
        now = datetime.datetime.now()
        prefix = ' - [ID:MAIN/ERROR] - '
        result = now.strftime("%X") + prefix
        return result
    def nowINFO():
        import datetime
        now = datetime.datetime.now()
        prefix = ' - [ID:MAIN/INFO] - '
        result = now.strftime("%X") + prefix
        return result
    print('|----------------------------------LOG----------------------------------|')
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.action_chains import ActionChains
        import time
        import random
        import zipfile
        import requests
        import json
        import time
        import re
        import datetime
        import subprocess
        import sys
        from multiprocessing import Process
        from threading import Thread
        from threading import Semaphore
        from subprocess import run
    except ModuleNotFoundError:
        import sys
        import subprocess
        subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print(nowINFO(), 'Packages succesefully installed!')
    finally:
        import os
        if sys.platform.startswith('win32'):
            if os.path.exists('chromedriver.exe'):
                print(nowINFO(), 'Installed chromedriver for win32')
            else:
                print(nowINFO(), 'Installing chromedriver for win32...')
                import urllib.request
                import zipfile as z
                urllib.request.urlretrieve("https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip", "chromedriver.zip")
                with z.ZipFile('chromedriver.zip', 'r') as zip_ref:
                    zip_ref.extractall()
                os.remove('chromedriver.zip')
                print(nowINFO(), 'Chromedriver installed succesefully!')
        else:
            if os.path.exists('chromedriver'):
                print(nowINFO(), 'Installed chromedriver for mac64')
            else:
                print(nowINFO(), 'Installing chromedriver for mac64...')
                import urllib.request
                import zipfile as z
                urllib.request.urlretrieve("https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_mac64.zip", "chromedriver.zip")
                with z.ZipFile('chromedriver.zip', 'r') as zip_ref:
                    zip_ref.extractall()
                os.remove('chromedriver.zip')
                print(nowINFO(), 'Chromedriver installed succesefully!')
        import re
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
        print(nowINFO(), 'Creating thread pool...')
        if len(sizes.split(',')) > 1:
            try:
                thread_count = len(sizes.split(','))
                sizes = sizes.split(',')
                try:
                    for size in sizes:
                        float(size)
                except:
                    print(nowERROR(), 'You entered size which is not a number')
                    exit()
                if int(thread_count) == 1:
                    print(nowERROR(), 'You entered only one size.')
                    exit()
                if int(thread_count) > len(prx):
                    print(nowERROR(), 'You should have minimum', thread_count, 'proxies to start bot.')
                    exit()
            except:
                print(nowERROR(), 'You should write size for each pair comma separated in quotation marks')
                exit()
            else:
                print(nowINFO(), 'Initializing threads with input arguments...')
                thread_num = 0
                for size in sizes:
                    thread_num += 1
                    proxy = prx[thread_num - 1].replace('\n', '')
                    if '\n' in proxy:
                        proxy = proxy.replace('\n', '')
                    print(nowINFO(), 'Initializing thread with ID:', thread_num)
                    proc = Thread(target=launch_yeezy, args=(model,size,thread_num,proxy))
                    proc.start()
        else:
            size = sizes
            thread_num = 1
            proxy = 0
            launch_yeezy(model, size, thread_num,proxy)
        