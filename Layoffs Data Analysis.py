#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing the necessary libraries
import pandas as pd
import numpy as np


# In[3]:


# loading the dataset
filePath = "C:\\Users\\AE-H\\Desktop\\archive\\layoffs_data.csv"
layoffsData = pd.read_csv(filePath)


# In[4]:


#  handling missing values by filling with the median of the column in cases of numeric values and N/A in the case of categorical values
layoffsData['Laid_Off_Count'] = layoffsData['Laid_Off_Count'].fillna(layoffsData['Laid_Off_Count'].median())
layoffsData['Funds_Raised'] = layoffsData['Funds_Raised'].fillna(layoffsData['Funds_Raised'].median())
layoffsData['Percentage'] = layoffsData['Percentage'].fillna(layoffsData['Percentage'].median())
layoffsData['List_of_Employees_Laid_Off'] = layoffsData['List_of_Employees_Laid_Off'].replace('Unknown', 'N/A')
layoffsData['List_of_Employees_Laid_Off'] = layoffsData['List_of_Employees_Laid_Off'].fillna('N/A')


# In[5]:


# converting date values into datetime
layoffsData['Date'] = pd.to_datetime(layoffsData['Date'])
layoffsData['Date_Added'] = pd.to_datetime(layoffsData['Date_Added'])


# In[ ]:


# ensuring numeric columns are in numeric format
layoffsData['Laid_Off_Count'] = pd.to_numeric(layoffsData['Laid_Off_Count'])
layoffsData['Funds_Raised'] = pd.to_numeric(layoffsData['Funds_Raised'])
layoffsData['Percentage'] = pd.to_numeric(layoffsData['Percentage'])


# In[6]:


# removing Duplicates
layoffsData = layoffsData.drop_duplicates()


# In[7]:


# ensuring consistency in categorical values
layoffsData['Industry'] = layoffsData['Industry'].str.strip().str.title()
layoffsData['Country'] = layoffsData['Country'].str.strip().str.title()
layoffsData['Location_HQ'] = layoffsData['Location_HQ'].str.strip().str.title()


# In[8]:


# adding a new 'Region' column
country_to_region = {
    'United States': 'North America',
    'Canada': 'North America',
    'Israel': 'Middle East',
    'Norway': 'Europe',
    'India': 'Asia',
    'Germany': 'Europe',
    'United Kingdom': 'Europe',
    'Australia': 'Oceania',
}
layoffsData['Region'] = layoffsData['Country'].map(country_to_region).fillna('Other')


# In[9]:


# exporting the cleaned data
layoffsData.to_csv('cleanedLayoffsData.csv', index=False)


# In[ ]:




