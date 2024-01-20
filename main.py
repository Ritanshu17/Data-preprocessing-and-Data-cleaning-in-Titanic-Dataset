import pandas as pd
import numpy as np 
train_df =  pd.read_csv("train.csv")
test_df= pd.read_csv("test.csv")
train_df.columns
train_df.head(10)
train_df.tail()
train_df.describe()
print(train_df.isnull().sum())
train_df.Cabin = train_df.Cabin.fillna("unknown")
print(train_df.isnull().sum())
print(train_df.shape)# total rows X column  count 
print("\n")
print(train_df.dtypes)# Each column data type
train_df.info()
print('_'*40)
test_df.info()