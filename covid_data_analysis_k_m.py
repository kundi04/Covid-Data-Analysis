# -*- coding: utf-8 -*-
"""Covid Data Analysis K.M

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w-zVHvNt8VQZmEs5kCYSc9UQsOk7l2bz
"""

import pandas as pd
import numpy as np
import seaborn as sns

"""#Data Preparation"""

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)
df.head()

"""## Getting to know your dataset"""

#describe my dataset
df.describe()

"""# Handling Duplicates"""

#check duplicated
df.duplicated().sum()
df.drop_duplicates(inplace=True)

"""# Handling Null Values"""

#check null values
df.isnull().sum()

"""# Dropping Nulls"""

#drop nulls

df.dropna(inplace=True)
df1 = df.dropna(subset =['total_cases'])

"""# Imputation"""

#Numerical Values
#using mean
df['new_cases'] = df['new_cases'].fillna(df['new_cases'].mean())

#Now use median to impute null values
df['new_cases'] = df['new_cases'].fillna(df['new_cases'].median())

#Categorical Values
#Select any Column with Categorical Values, impute using mode
df['continent'] = df['continent'].fillna(df['continent'].mode())

"""# Dropping Columns"""

#drop column named iso_code
df.drop('iso_code', axis=1, inplace=True)

#now, write code to drop column named new_deaths_smoothed
df.drop('new_deaths_smoothed', axis=1, inplace=True)

"""# Getting a Subset of your Data"""

# Filter for rows where 'location' is either 'Zimbabwe' or 'Rwanda'
subset = df[(df['location'] == 'Zimbabwe') | (df['location'] == 'Rwanda')]

# Display the first few rows of the subset
subset.head()

"""# Let's Save Our Cleaned Data"""

#Save the Data you have Cleaned
df.to_csv('url')