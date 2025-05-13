import pandas as pd

#Load the dataset
df = pd.read_csv('owid-covid-data.csv')
print("Shape : " , df.shape)
print("columns : " , df.columns)

#print(df.head())

#---------------------------------------------------- Cleaning the data ---------------------------------------
# Drop unused columns
df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'population']]

# Drop rows with missing values
df = df.dropna()

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter for a single country, e.g., India
Pak_df = df[df['location'] == 'Pakistan']

print(Pak_df.head())


# ---------------------------------------------------- Data Visualization with Matplotlib & Seaborn ----------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Line plot of new cases
plt.figure(figsize=(12, 6))
sns.lineplot(data=Pak_df, x='date', y='new_cases')
plt.title('Daily New COVID-19 Cases in Pakistan')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.grid(True)
plt.show()

# Total deaths vs total cases
plt.figure(figsize=(8, 6))
sns.scatterplot(data=Pak_df, x='total_cases', y='total_deaths')
plt.title('Total Cases vs Deaths in Pakistan')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.show()



#  ---------------------------------------------------- Statistical Analysis ----------------------------------------------------
print(Pak_df.describe())

# Correlation between total cases and total deaths
correlation = Pak_df['total_cases'].corr(Pak_df['total_deaths'])
print(f"Correlation between total cases and deaths: {correlation:.2f}")
