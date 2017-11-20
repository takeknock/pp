#!/usr/bin/env python

import datetime

class yieldcurve():
    def __init__(self, market_set, interpolator, asof):
        self.market_set = market_set
        self.interpolator = interpolator
        self.asof = asof

    def build(self):
        print("call build")

    def get_df(self,date):
        print("call get_df")
    


if __name__ == "__main__":
    str_date = '2017/11/20'
    dt = datetime.datetime.strptime(str_date, '%Y/%m/%d')
    market_set = []
    interpolator = 'test'
    yc = yieldcurve(market_set, interpolator, dt)

    yc.build()
    yc.get_df(dt)
