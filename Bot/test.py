import urllib.request
import requests
prefix = request.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
link = "http://chromedriver.storage.googleapis.com/" + prefix.text + '/chromedriver_mac64.zip'
urllib.request.urlretrieve(link, "chromedriver.zip")