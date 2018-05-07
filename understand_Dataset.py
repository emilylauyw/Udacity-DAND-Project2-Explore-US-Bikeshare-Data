"""
Using pandas to better understand the bike share dataset.
"""

import pandas as pd

df = pd.read_csv("chicago.csv")
# start by viewing the first few rows of the dataset.
print(df.head())
#noticed that there NaN values under Gender and Birth Year columns.

# view what are the columns in this dataset
print(df.columns)

# view the different types of values in each column
print(df.info())
