# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:48:31 2023

@author: Tanushri Bhaduri
"""
import split_data
import pandas as pd
from imblearn.under_sampling import NearMiss
from imblearn.over_sampling import SMOTE

def undersample_data(dataframe):
    y,training_set = split_data.split_target_features(dataframe)
    undersample = NearMiss(version = 2, n_neighbors = 5)
    x,y = undersample.fit_resample(training_set,y)
    undersampled_dataframe=pd.concat([pd.DataFrame(y),pd.DataFrame(x)],axis=1)
    return(undersampled_dataframe)


def oversampling_data(dataframe):
    y,training_set=split_data.split_target_features(dataframe)
    oversample = SMOTE()
    training_set,y =oversample.fit_resample(training_set,y)
    oversampled_dataframe=pd.concat([pd.DataFrame(y),pd.DataFrame(training_set)],axis=1)
    return(oversampled_dataframe)