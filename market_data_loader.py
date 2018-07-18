# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 01:16:54 2018

@author: Takehiro Mimasu
"""

import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import pandas as pd

def fetch_nikkei225(start='1949/5/16', end='2018/3/24'):
    N225 = pdr.DataReader("NIKKEI225", 'fred', start, end)
    return N225


def fetch_usdjpy(start='1949/5/16', end='2018/3/24'):
    fx = pdr.DataReader('DEXJPUS', 'fred', start, end)
    return fx


def fetch_nikkei225_detail(start='1984/1/4', end='2018/3/24'):
    price = pdr.DataReader('^N225', 'yahoo', start, end)
    return price

def aquire_data():
    n225 = fetch_nikkei225()
    fx = fetch_usdjpy()
    n225.to_csv("../market_data/n225.csv")
    fx.to_csv("../market_data/usdjpy.csv")
    port = pd.concat([n225, fx], axis=1).dropna()
    port.to_csv("../market_data/port.csv")
    print('all data saved!')

def main():
    port = pd.read_csv('../market_data/port.csv')
        
    
if __name__ == "__main__":
    main()
