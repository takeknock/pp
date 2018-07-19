from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

CHROME = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER = 'C:\Program Files (x86)\Google\chromedriver_win32\chromedriver.exe'


def create(url):
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
    driver.get(url)
    driver_wait = WebDriverWait(driver, 10)
    driver_wait.until(ec.presence_of_all_elements_located)
    return driver
