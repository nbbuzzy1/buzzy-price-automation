from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")


def buzzy_price_automation():
	chrome_browser = webdriver.Chrome('./chromedriver.exe', options=options)
	chrome_browser.get('https://buzzyprice.com')
	time.sleep(20)
	buzzy_price_page_interaction(chrome_browser)
	chrome_browser.get('https://google.com')
	google_page_interaction(chrome_browser)
	time.sleep(20)
	buzzy_price_page_interaction(chrome_browser)
	chrome_browser.close()


def buzzy_price_page_interaction(chrome_browser):
	auction_item_input = chrome_browser.find_element_by_id('auctionLink')
	auction_item_url = 'https://www.ebay.com/itm/Playstation-5-Disc-Version-PS5/293764734938?hash=item4465be1fda:g:r3kAAOSwkplfa9Tn'
	auction_item_input.send_keys(auction_item_url)
	time.sleep(20)
	auction_item_input.send_keys(Keys.ENTER)
	time.sleep(75)


def google_page_interaction(chrome_browser):
	google_search_input = chrome_browser.find_element_by_class_name('gLFyf')
	google_search_input.send_keys('buzzyprice ebay alert')
	google_search_input.send_keys(Keys.ENTER)
	time.sleep(35)
	buzzy_price_url = 'https://www.buzzyprice.com/'
	buzzy_price_link = chrome_browser.find_element_by_xpath('//a[@href="'+ buzzy_price_url +'"]')
	buzzy_price_link.click()


successful_automations = 0

while True:
	buzzy_price_automation()
	successful_automations += 1
	print('successful automation', successful_automations)
	time.sleep(10800)

