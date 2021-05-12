# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:45:51 2021

@author: Admin
"""

#import essential libraries
import pandas as pd
data=pd.read_csv('train.csv')

#checking for null values
data.info()
#outlier=data.describe()
data.isnull().sum()
data['Item_Type'].nunique()
data['Item_Type'].value_counts()
data['Item_Fat_Content'].value_counts()
data['Item_Fat_Content'].nunique()

dict_fat={}
dict_fat={'Low Fat':'Low Fat','LF':'Low Fat','low fat':'Low Fat','Regular':'Regular','reg':'Regular'}

data['Item_Fat_Content']=data['Item_Fat_Content'].map(dict_fat)


for i,df in data.groupby(['Item_Type','Item_Fat_Content']):
    print(i)
    print(df['Item_Weight'].mean())
    #if (i[0]==data['Item_Type'] & i[1]==data['Item_Fat_Content']) & (data['Item_Weight'].isnull):
     #   data['Item_Weight'].fillna(df['Item_Weight'].mean())
        
        
        
        
        
        
        
        
        
        
        
        
        
        









