# Term Deposite Marketing

## Introduction

Our Client, an European Bank wants to improve the success rate of the calls made to the customer for investing on their deposit schemes. For this, Company provides us their call centre data to make a machine learning model that identify weather a customer will invest on the scheme or not. The dataset consists of 40000 rows and 14 columns.

 ## Installation
 
Download Anaconda
conda install -c anaconda jupyter
conda install -c anaconda spyder
$ conda list -e > requirements.txt

## Structure


|---[.ipynb_checkpoints](.ipynb_checkpoints)<br>
|---[Notebook](./Notebook)<br>
 &emsp;|---[Term_Deposit.ipynb](./Notebook/Term_Deposit.ipynb)<br>
|---[data](./data)<br>
 &emsp;|---[term-deposit-marketing-2020.csv](./data/term-deposit-marketing-2020.csv)<br>
|---[src]((./src)<br>
 &emsp;|---[data_encoding.py](./src/data_encoding.py)<br>
 &emsp;|---[evaluate_model.py](./src/evaluate_model.py)<br>
 &emsp;|---[feature_selection.py](./src/feature_selection.py)<br>
 &emsp;|---[main.py](./src/main.py)<br>
 &emsp;|---[partition_data.py](./src/partition_data.py)<br>
 &emsp;|---[read_file.py](./src/read_file.py)<br>
 &emsp;|---[split_data.py](./src/split_data.py)<br>
 &emsp;|---[treat_imbalance.py](./src/treat_imbalance.py)<br>
|---[README.md](./README.md)
 
 
