from pandas.core.indexes.base import Index
from sklearn.model_selection import train_test_split
import pandas as pd

df=pd.read_csv('cars.csv')
train_data,test_data=train_test_split(df,test_size=0.5)

train_data.to_csv('train_data.csv',index=False)
test_data.to_csv('test_data.csv',index=False)