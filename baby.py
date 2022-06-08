from glob import glob
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

from pandas.core import indexing
filename=glob('baby_names/*.txt')
baby_list=[]
for file in filename:
    new_df=pd.read_csv(file,names=['names','sex','count'])
    year=int(re.findall('\d\d\d\d', file)[0])
    if year>2010:
        break
    new_df['year']=year
    baby_list.append(new_df)
final_df=pd.concat(baby_list,axis=0,ignore_index=True)
df_2010=final_df[final_df['year']==2010]
df_fname=df_2010[df_2010['sex']=='F']
sort_f=df_fname.sort_values('count', ascending = False, ignore_index = True)
print(sort_f['names'][0:5])
df_m2010=final_df[final_df['year']==2010]
df_mname=df_2010[df_2010['sex']=='M']
sort_m=df_mname.sort_values('count', ascending = False, ignore_index = True)
print(sort_m['names'][0:5])
grouped_multiple = final_df.groupby(['year', 'sex']).agg({'count': ['sum']})
print(grouped_multiple)
grouped_multiple.plot(kind='bar')
grouped_multiple[0:10].plot(kind='bar')


