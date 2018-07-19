import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import os
from selenium.webdriver.common.keys import Keys


import driver_factory


LANDMLIT_URL = 'http://www.land.mlit.go.jp/webland/download.html'
LANDMLIT_SERVLET_URL = 'http://www.land.mlit.go.jp/webland/servlet/DownloadServlet'

INPUT_FOLDER = os.path.join('..', '..', 'input')


def fetch_from_list(driver):
    id_ = "TDIDFrom"
    from_list = fetch_by_id(driver, id_)
    return from_list

def fetch_to_list(driver):
    id_ = "TDIDTo"
    to_list = fetch_by_id(driver, id_)
    return to_list

def fetch_prefecture_list(driver):
    id_ = "TDK"
    prefecture_list = fetch_by_id(driver, id_)
    return prefecture_list

def fetch_city_list(driver):
    id_ = "SKC"
    city_list = fetch_by_id(driver, id_)
    return city_list


def fetch_by_id(driver, id_):
    return driver.find_element_by_id(id_).text.replace(" ", "").split("\n")

def to_dataframe(list):
    return pd.DataFrame(list)

def save(driver):
    from_list = fetch_from_list(driver)
    from_list_df = to_dataframe(from_list)
    from_list_df.to_csv(os.path.join(INPUT_FOLDER, 'realestate', 'from.csv'), encoding='shift_jis', index=False)
    to_list = fetch_to_list(driver)
    to_list_df = to_dataframe(to_list)
    to_list_df.to_csv(os.path.join(INPUT_FOLDER, 'realestate', 'to.csv'), encoding='shift_jis', index=False)
    prefecture_list = fetch_prefecture_list(driver)
    prefecture_list_df = to_dataframe(prefecture_list)
    prefecture_list_df.to_csv(os.path.join(INPUT_FOLDER, 'realestate', 'prefecture.csv'), encoding='shift_jis', index=False)
    city_list = fetch_city_list(driver)
    city_list_df = to_dataframe(city_list)
    city_list_df.to_csv(os.path.join(INPUT_FOLDER, 'realestate', 'city.csv'), encoding='shift_jis', index=False)

def main():
    from_xpath = '//*[@id="TDIDFrom"]'
    to_xpath = '//*[@id="TDIDTo"]'
    prefecture_xpath = '//*[@id="TDK"]'
    city_xpath = '//*[@id="SKC"]'

    prefecture_list = pd.read_csv(os.path.join(INPUT_FOLDER, 'realestate', 'prefecture.csv'), encoding='shift_jis')

    for i in range(1, len(prefecture_list.index)):
        driver = driver_factory.create(LANDMLIT_SERVLET_URL)
        pref_element = driver.find_element_by_id("TDK")
        pref = prefecture_list.iloc[i, 0]
        print(pref)
        pref_element.send_keys(pref)
        city_list = to_dataframe(fetch_city_list(driver))
        city_list.to_csv(os.path.join(INPUT_FOLDER, 'realestate', 'city', str(i)+'_city.csv'), encoding='shift_jis')

if __name__ == "__main__":
    main()
