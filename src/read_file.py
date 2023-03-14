"""
Reading the Term deposit marketing csv file.
"""


import pandas as pd


def read_csv():
    data_frame=pd.read_csv('..\data\\term-deposit-marketing-2020.csv', encoding = 'unicode_escape', sep=',', header=0)
    return(data_frame)
