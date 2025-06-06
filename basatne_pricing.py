# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns of the DataFrame
pd.set_option('display.max_columns', None)

# Ignore warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

# Reading multiple Excel files into separate DataFrames
df_1 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.ae_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-26-03-242Z.xlsx')
df_2 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.ca_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-01-02-221Z.xlsx')
df_3 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.co.jp_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-58-31-953Z.xlsx')
df_4 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.co.uk_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-03-34-982Z.xlsx')
df_5 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.com_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T14-57-24-753Z.xlsx')
df_6 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.com.au_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-48-50-851Z.xlsx')
df_7 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.com.be_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-23-15-300Z.xlsx')
df_8 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.com.br_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-50-53-387Z.xlsx')
df_9 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.com.mx_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-02-09-631Z.xlsx')
df_10 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.com.tr_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-51-38-841Z.xlsx')
df_11 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.de_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-04-37-199Z.xlsx')
df_12 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.es_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-20-46-437Z.xlsx')
df_13 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.fr_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-19-16-001Z.xlsx')
df_14 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.in_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T14-58-51-065Z.xlsx')
df_15 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.it_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-20-03-094Z.xlsx')
df_16 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.nl_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-21-29-215Z.xlsx')
df_17 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.pl_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-22-32-765Z.xlsx')
df_18 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.sa_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-35-13-922Z.xlsx')
df_19 = pd.read_excel('D:/basatne_finance/version_5_f/amazon.se_91264ceb-d1c7-4f33-8343-c69e318cbae9_2025-01-07T15-25-11-665Z.xlsx')

# Combining all the DataFrames into one using vertical concatenation
df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19], axis=0, ignore_index=True)

# Dropping duplicate rows to ensure unique entries
df.drop_duplicates(inplace=True)

# Dropping unnecessary columns 'Item Name' and 'Domain'
df = df.drop(['Item Name', 'ASIN'], axis=1)

# Filtering out rows where 'Is Refurbished' is not 'Yes'
df = df.drop(df[df['Is Refurbished'] != 'Yes'].index)

# Dropping the column 'Is Refurbished' as it is no longer needed
df = df.loc[:, df.columns != 'Is Refurbished']

# Cleaning the 'Price (USD)' column: removing '$' and converting to float
df['Price (USD)'] = df['Price (USD)'].str.replace('$', '', regex=False).astype(float)

# Replacing missing values in 'Price (USD)' with 0
df['Price (USD)'].fillna(0, inplace = True)

# Filling missing values in the 'Condition' column with 'Not Found'
df["Condition"].fillna("Not Found", inplace = True)

# Mapping 'Condition' values to numerical grades
replace_dict_con = {
    'new': 1,
    'premium': 2,
    'excellent': 3,
    'good': 4,
    'acceptable': 5,
    'Not Found': 6
}
df['Condition Grade'] = df['Condition'].map(replace_dict_con)

# Capitalize each word in the 'Condition' column
df['Condition'] = df['Condition'].str.title()

# Capitalize each word in the 'Color' column
df['Color'] = df['Color'].str.title()

# Filtering out rows where 'Condition' is not 'Not Found'
df = df.drop(df[df['Condition'] == 'Not Found'].index)

# Filling missing values in the 'Service Provider' column with 'Not Found'
df["Service Provider"].fillna("Not Found", inplace = True)

# Creating a new column 'Storage' as a copy of the 'Size' column
df['Storage'] = df['Size']

# Cleaning 'Size' column: removing 'GB' and 'TB' suffixes
df['Size'] = df['Size'].str.replace(r'(GB|TB)', '', regex=True)

# Replacing '1' with '1024' (assuming '1' refers to 1 TB)
df.replace('1', '1024', inplace = True)

# Renaming the 'Size' column to 'Size(GB)'
df.rename(columns={'Size': 'Size(GB)'}, inplace=True)

# Dropping rows where 'Size(GB)' is 'Not Found'
df = df.drop(df[df['Size(GB)'] == 'Not Found'].index)

# Creating a new column 'Model-Size' by concatenating 'Model' and 'Size(GB)'
df['Model-Size'] = df['Model'] + ' - ' + df['Size(GB)']

# Mapping country-specific Amazon domains to country names
replace_dict = {
    'amazon.ae': 'UAE',
    'amazon.ca': 'Canada',
    'amazon.co.jp': 'Japan',
    'amazon.pl': 'Poland',
    'amazon.nl': 'Netherlands',
    'amazon.it': 'Italy',
    'amazon.in': 'India',
    'amazon.fr': 'France',
    'amazon.es': 'Spain',
    'amazon.com': 'USA',
    'amazon.de': 'Germany',
    'amazon.com.tr': 'Turkey',
    'amazon.com.au': 'Australia',
    'amazon.co.uk': 'UK',
    'amazon.sa': 'Saudi Arabia',
    'amazon.se': 'Sweden',
    'amazon.com.mx': 'Mexico',
    'amazon.com.br': 'Brazil',
    'amazon.com.be': 'Belgium',
}
df['Country'] = df['Country'].map(replace_dict).fillna(df['Country'])

# Filtering rows where 'Price (USD)' is between 99 and 1599
df = df.drop(df[(df['Price (USD)'] < 99.0) | (df['Price (USD)'] > 1599.0)].index)

# Display the final DataFrame
basatne_finance_data = df

# save as a .csv file
# basatne_finance_data.to_csv('basatne_finance_data.csv', index=False)