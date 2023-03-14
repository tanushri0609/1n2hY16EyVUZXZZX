# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:07:14 2023

@author: Tanushri Bhaduri
"""

from sklearn.metrics import accuracy_score,f1_score

def model_accuracy(y_pred,y_test):
    result = accuracy_score(y_test,y_pred)
    return(result)

def model_f1(y_pred,y_test):
    result = f1_score(y_test,y_pred)
    return(result)