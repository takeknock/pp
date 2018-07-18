from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

LANDMLIT_URL = 'http://www.land.mlit.go.jp/webland/download.html'
CHROME = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER = 'C:\Program Files (x86)\Google\chromedriver_win32\chromedriver.exe'
LANDMLIT_SERVLET_URL = 'http://www.land.mlit.go.jp/webland/servlet/DownloadServlet'

def create_driver():
    options = Options()
    options.binary_location = CHROME
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--lang=ja')
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(LANDMLIT_SERVLET_URL)
    driver_wait = WebDriverWait(driver, 10)
    driver_wait.until(ec.presence_of_all_elements_located)
    return driver

def get_from_list(driver):
    id_ = "TDIDFrom"
    from_list = get_by_id(driver, id_)
    return from_list

def get_to_list(driver):
    id_ = "TDIDTo"
    to_list = get_by_id(driver, id_)
    return to_list

def get_prefecture_list(driver):
    id_ = "TDK"
    prefecture_list = get_by_id(driver, id_)
    return prefecture_list

def get_city_list(driver):
    id_ = "SKC"
    city_list = get_by_id(driver, id_)
    return city_list


def get_by_id(driver, id_):
    return driver.find_element_by_id(id_).text.replace(" ", "").split("\n")

def main():
    from_xpath = '//*[@id="TDIDFrom"]'
    to_xpath = '//*[@id="TDIDTo"]'
    prefecture_xpath = '//*[@id="TDK"]'
    city_xpath = '//*[@id="SKC"]'

    driver = create_driver()
    from_list = get_from_list(driver)
    to_list = get_to_list(driver)
    prefecture_list = get_prefecture_list(driver)
    city_list = get_city_list(driver)
    print(city_list)

if __name__ == "__main__":
    main()
