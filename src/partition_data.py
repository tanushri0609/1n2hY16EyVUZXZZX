# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:16:18 2023

@author: Tanushri Bhaduri
"""
import split_data
from sklearn.model_selection import train_test_split

def partition_feature_label(dataframe):
    y, training_set = split_data.split_target_features(dataframe)
    X_train, X_test, y_train, y_test = train_test_split(training_set, y, test_size=0.20)
    return(X_train, X_test, y_train, y_test)