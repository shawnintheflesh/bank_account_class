import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.svm import LinearSVC
import numpy as np
import seaborn as sns
nba= pd.read_csv('C:/Users/admin/Desktop/2021nbaseason.csv')
kd = pd.read_csv('C:/Users/admin/Desktop/kd2021.csv')

print(kd.head())
print(kd.shape)
print(kd.columns)

print(kd['FP'].mean())
print(kd['FP'].std())
print(kd.describe())










