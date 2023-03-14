# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:26:23 2023

@author: Tanushri Bhaduri
"""

def select_features(dataframe):
    data_frame = dataframe.drop(['education_unknown','education_tertiary','education_primary','campaign','loan','housing','default'], axis=1)
    return(data_frame)