import requests
import time
import re
from random_proxy import RandomProxy
from UserAgentRandom import LoadHeader
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
userag = str(LoadHeader())
WINDOW_SIZE = "1920,1080"
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=%s" % WINDOW_SIZE)
from selenium.webdriver.common.proxy import Proxy, ProxyType
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = str(RandomProxy())
capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

#driver = webdriver.Chrome(desired_capabilities=capabilities, options=options) - run with proxy
driver = webdriver.Chrome(options=options) # run without proxy
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', "platform":"Windows"})
#####################################################################################################################################################
username = 'testbotsneak@gmail.com'
password = 'Georgy20044'
urlstock = 'https://accounts.stockx.com/login'
modeladi = 'B28054'
sizeadi = 10.5
earlyurl = 'https://stockx.com/supreme-san-francisco-box-logo-tee-black'

######################################################################################################################################################
cartpageadi = "https://www.adidas.ru/on/demandware.store/Sites-adidas-RU-Site/ru_RU/Cart-Show"
payloadstock = {
	'username': username,
	'password': password
}



headersadi = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.9",
	#"Host": "www.adidas.com",
	"Connection": "keep-alive",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.9",
	"Connection": "keep-alive",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": userag
}


def StockX():
	responsecode = re.compile('200')
	with requests.Session() as session:
		session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
		session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
		session.post(urlstock, data=payloadstock)
		auth = session.get(urlstock)
		res = 'Error :/'
		if str(auth) == '<Response [200]>':
			res = 'Code 200, Success!'
		print('First stage completed, authorised with login',
			  username + '. Server returns:', res)

		r = None
		try:
			r = session.get(earlyurl)
		except:
			res = 'Error :/'

		if str(r) == '<Response [200]>':
			res = 'Code 200, Success!'
		print('Second stage completed, item url opened successefully. Server returns:', res)

	# etc...


def CheckStockAdidas(modeladi, sizeadi):
	print('Your current size is:', sizeadi)
	print('Your picked model is:', modeladi)
	# Generates URLs for releases on Adidas.com
	BaseSizeadi = 580
	# Base Size is for Shoe Size 6.5
	ShoeSizeadi = sizeadi - 6.5
	ShoeSizeadi = ShoeSizeadi * 20
	RawSizeadi = ShoeSizeadi + BaseSizeadi
	ShoeSizeCodeadi = int(RawSizeadi)
	urladi = 'https://adidas.ru/' + \
		str(modeladi) + '.html?forceSelSize=' + \
		str(modeladi) + '_' + str(ShoeSizeCodeadi)
	
	try:
		itempage = requests.get(urladi, headers=headersadi)									
	except:
		print('No response. Check your internet connection.')
		exit()
	print('Bot connected to server with code:', itempage.status_code)
	print('Begin initial export sizes as list.')
	print('\n')
	driver.get(urladi)
	SizesListRaw = driver.find_element_by_class_name(
			"gl-menu.gl-square-list.gl-square-list--condensed")
	options = [x for x in SizesListRaw.find_elements_by_tag_name("li")]
	SizesList = []
	for element in options:
		x = re.compile('\d*\.?\d\sUK')
		x1 = x.search(element.get_attribute("title")).group(0)
		x1 = x1.replace(' UK', '')
		x1 = float(x1) + 0.5
		x1 = str('{0:g}'.format(x1))
		SizesList.append(x1)
		
	print('List of sizes available:',SizesList)
	if not str(sizeadi) in SizesList:
		print('No your size available.')
		exit()
	else:
		SizeIndex = SizesList.index(str(sizeadi))
		print('Your size:', str(sizeadi)+ '\n'+'Size available:', SizesList[SizeIndex])
	AddToCart = driver.find_element_by_class_name(
			"gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag")
	AddToCart.submit()
	timer = 60.0
	threads = 0
	time.sleep(0.5)
	while timer != 0:
		try:
			driver.find_element_by_class_name(
				"gl-cta.gl-cta--secondary.gl-cta--full-width")
		except NoSuchElementException as e:
			timer -= 0.5
			threads += 1
			time.sleep(0.5)
			print('No match. Thread number:', str(threads) + '/60')
			if timer == 60:
				print('Timeout error.')
				exit()
		else:
			print('Element match success!')
			break
	BuyButton = driver.find_element_by_class_name(
				"gl-cta.gl-cta--secondary.gl-cta--full-width")
	BuyButton.click()
	print('Transfering on billing page...')
	
	driver.quit();
	
#CheckStockAdidas(modeladi,sizeadi)
exit()

