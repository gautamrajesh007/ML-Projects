from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib
import tensorflow as tf
import time

start = time.time()

train = pd.read_csv('/home/gautam/Documents/Machine Learning/Titanic Survival/Datasets/train.csv')
test = pd.read_csv('/home/gautam/Documents/Machine Learning/Titanic Survival/Datasets/test.csv')

print(train.head())

y_train = train.pop('Survived')

print(train.describe())

print(train.shape)

print(y_train.head())

print(train.age.hist(bins=20))

end = time.time()
time_loop = end - start

print("Execution time using loops:", time_loop)
