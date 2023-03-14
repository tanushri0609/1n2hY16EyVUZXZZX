# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:04:06 2023

@author: Tanushri Bhaduri
"""

def split_target_features(data_file):
    y=data_file['y']
    features=data_file.drop(['y'],axis=1)
    return(y,features)