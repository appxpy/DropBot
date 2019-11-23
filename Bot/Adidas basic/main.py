 #-*- coding: utf-8 -*-
import requests
import json
import browserOps
import threading
import time
from UserAgentRandom import LoadHeader
from concurrent.futures import ThreadPoolExecutor as Pool
import re
from now import now
thread = 1
open('timerfile.txt', 'w').close()
f = open("timerfile.txt","a+")
f.write(now())
f.write('*')
f.close()
sizes = [8.5, 9, 9.5, 10]
thread_count = 8
print(now() ,'-', 'Bot started')
# :param size spefific size for purchase
def url_gen(model,size):
    BaseSize = 580
    ShoeSize = float(size) - 6
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    url = 'https://www.adidas.ru/yeezy/' + model + '.html?forceSelSize=' + model + '_' + str(int(RawSize))
    print(now() ,'-', 'Url created')
    return url

# :param model specific model of sneaker
# :return size_lookup dictionary of sizes/availability
def check_stock(model):
    #ua = LoadHeader()
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": ua
}
    #CheckSite = requests.get('https://adidas.ru', headers=headers)
    #print(now() ,'-', 'Recieved response from server with code', CheckSite.status_code)
    size_url = 'https://www.adidas.ru/api/products/{}/availability'.format(model)
    raw_sizes = requests.get(size_url,headers=headers)
    size_data = json.loads(raw_sizes.text)
    while size_data['availability_status'] == 'PREVIEW':
        raw_sizes = requests.get(size_url,headers=headers)
        size_data = json.loads(raw_sizes.text)
        print(now() ,'-', 'Availability status - PREVIEW. Repeating attempts ')
        time.sleep(1)
    print(now() ,'-', 'Recieved response from server API with code', raw_sizes.status_code)
    print(now() ,'-', 'Availability status IN_STOCK')
    list = size_data['variation_list']
    size_dict = {}
    size_lookup = {}
    sizes_list = []
    for i in range(21):
        size_dict[i] = {list[i]['size']:list[i]['availability_status']}
    for key,value in size_dict.items():
        size_lookup.update(value)
    for key in size_lookup.keys():
        x = re.compile('\d*\.?\d\sUK')
        x1 = x.search(str(key)).group(0)
        x1 = x1.replace(' UK', '')
        #x1 = float(x1) + 0.5
        #x1 = str('{0:g}'.format(x1))
        sizes_list.append(x1)
    value_list = size_lookup.values()
    size_lookup = dict(zip(sizes_list, value_list))
    print(now() ,'-', 'Created size list based on API')
    return size_lookup

def main():
    #model = str(input('Model: '))
    model = "FW4843"
    print(now() ,'-', 'Use selected model:', model)
    size = "3"
    print(now() ,'-', 'Use selected size:', size)
    #size = str(input('Shoe size: '))
    sneaker_bot(model,size)

# Sets up bot environment to automate purchase sneaker if available.
# :param size specific size for purchase
def sneaker_bot(model,size):
    sizes = check_stock(model)
    #print(sizes)
    url = url_gen(model,size)
    if str(size) in sizes:
        if str(sizes[str(size)]) == 'IN_STOCK':
            print(now() ,'-', 'Your size is found, start the purchase phase')
            browserOps.process_cart_adidas(url)
            browserOps.autofill_shipping_adidas()
            browserOps.autofill_card_adidas()
        else:
            print(now() ,'-', 'Your size is not available')
    else:
        print(now() ,'-', 'During to API error we are not able to save you a pair')

# Allows for multitreading in order to purchase all sizes
# specified in size list
with Pool(thread_count) as executor:
    for size in sizes:
        executor.submit(sneaker_bot,size)
main()
#browserOps.driver.quit()