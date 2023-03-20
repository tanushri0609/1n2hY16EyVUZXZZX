# Term Deposite Marketing

## Introduction

Our client, a European Bank wants to improve the success rate of the calls made to customers for investing in their deposit schemes. For this, the client has provided us their call centre data to train a model that can identify whether a customer will invest in the scheme. The dataset consists of 40000 rows and 14 columns.

 ## Installation
 
Download Anaconda <br>
conda install -c anaconda jupyter <br>
conda install -c anaconda spyder <br>
$ conda list -e > requirements.txt<br>

## Structure


|---[.ipynb_checkpoints](.ipynb_checkpoints)<br>
|---[Notebook](./Notebook)<br>
 &emsp;|---[Term_Deposit.ipynb](./Notebook/Term_Deposit.ipynb)<br>
|---[data](./data)<br>
 &emsp;|---[term-deposit-marketing-2020.csv](./data/term-deposit-marketing-2020.csv)<br>
|---[src](./src)<br>
 &emsp;|---[data_encoding.py](./src/data_encoding.py)<br>
 &emsp;|---[evaluate_model.py](./src/evaluate_model.py)<br>
 &emsp;|---[feature_selection.py](./src/feature_selection.py)<br>
 &emsp;|---[main.py](./src/main.py)<br>
 &emsp;|---[partition_data.py](./src/partition_data.py)<br>
 &emsp;|---[read_file.py](./src/read_file.py)<br>
 &emsp;|---[split_data.py](./src/split_data.py)<br>
 &emsp;|---[treat_imbalance.py](./src/treat_imbalance.py)<br>
|---[README.md](./README.md)
 
 
