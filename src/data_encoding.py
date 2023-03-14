# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:57:27 2023

@author: Tanushri Bhaduri
"""
import pandas as pd

def categorical_data_encod(data_file):
    data_file.replace({'no':0, 'yes':1}, inplace=True)
    data_file['job'].replace({'management':1, 'technician':2, 'entrepreneur':3, 'blue-collar':4, 'unknown':0, 'retired':5, 'admin':6, 'services':7,'self-employed':8, 'unemployed':9, 'housemaid':10, 'student':11}, inplace=True)
    data_file['month'].replace({'may':5, 'jun':6, 'jul':7, 'aug':8, 'oct':10, 'nov':11, 'dec':12, 'jan':1, 'feb':2, 'mar':3, 'apr':4}, inplace=True)
    encoded_data = pd.get_dummies(data_file, columns = ['marital', 'contact','education'])
    return(encoded_data)
