import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import json

train_data_1 = pd.read_json('/home/gautam/Documents/Datasets/Honeypot Detection/part0.json')
train_data_1.shape

print(train_data_1.head())

x = train_data_1.iloc[:, 2]
for k in x:
    for l in k:
        for i,j in l.items():
            print(i, ':', j)