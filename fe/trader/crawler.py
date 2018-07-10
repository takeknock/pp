import numpy as np
import urllib3
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import codecs
import os
import json
import sys


def main():
    #url = "https://suumo.jp/tochi/soba/hiroshima/area/"
    url = "https://suumo.jp/tochi/hiroshima/sc_hiroshimashinaka/?et=9999999&kj=9&tb=0&tt=9999999"
    driver = webdriver.PhantomJS()
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    soup = bs(html, "lxml")

    ## description
    # output
    print(soup.find_all(class_="dottable-line"))
    # write the output as a json file


if __name__ == "__main__":
    main()