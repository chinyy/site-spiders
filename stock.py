#!/usr/bin/python
# coding: UTF-8

"""This script parse stock info"""

import tushare as ts

STOCK = [
    '600704',
    '600816',
    '600958',
    '600959',
    '603958',
    '000776',
    '300253',
]
def get_all_price(code_list):
    '''process all stock'''
    df = ts.get_realtime_quotes(STOCK)
    print df

if __name__ == '__main__':
    get_all_price(STOCK)
