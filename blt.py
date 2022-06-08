from numpy.lib.histograms import histogram
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('Baltimore.csv')
df['AnnualSalary']=df['AnnualSalary'].astype(str)
df['AnnualSalary']=(df['AnnualSalary'].apply(lambda x:x.replace('$','')))
df['AnnualSalary']=df['AnnualSalary'].astype(float)
grp=df.groupby(['JobTitle'])['AnnualSalary']
aggr=grp.agg([np.mean,np.sum])
print(aggr)

plt.plot(df['JobTitle'].value_counts(),kind='hist')
agency=df[['Agency','AgencyID']]
print(agency)
print(df['GrossPay'].isnull().sum())
