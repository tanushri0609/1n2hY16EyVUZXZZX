# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 07:58:44 2023

@author: Tanushri Bhaduri
"""

import warnings
import read_file
import data_encoding
import treat_imbalance
import feature_selection
import partition_data
import evaluate_model
import split_data
import xgboost as xgb

warnings.filterwarnings("ignore")

# Read the CSV file
data_frame = read_file.read_csv()

# Convert all categorical data into numeric form. 
numeric_data = data_encoding.categorical_data_encod(data_frame)

# Treat the imbalance data 
balance_data = treat_imbalance.undersample_data(numeric_data)

# Prepare data for testing
test_data = treat_imbalance.oversampling_data(numeric_data)

# Select features for building the model
data_for_training = feature_selection.select_features(balance_data) 

# Select features for testing the model
data_for_testing = feature_selection.select_features(test_data) 

# Data partitioning for building model and later validation
X_train,X_validate,y_train,y_validate = partition_data.partition_feature_label(data_for_training)

# Split data for testing model
y_test,X_test = split_data.split_target_features(data_for_testing)

# Build the classification model
#y_predict,y_predict_final = classification_model.classifier(X_train, X_validate, X_test, y_train)


classifier = xgb.XGBClassifier(n_estimators = 100, learning_rate =5)
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_validate)
y_pred_final = classifier.predict(X_test)
    

# Evaluate the model
accuracy = evaluate_model.model_accuracy(y_pred_final,y_test)
f1_score = evaluate_model.model_f1(y_pred_final, y_test)
print("Accuracy of the model:",accuracy)
print("F1 score of the model:",f1_score)