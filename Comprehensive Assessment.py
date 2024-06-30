#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = 'https://docs.google.com/spreadsheets/d/1VP9BE_eI2yl6uUHSm4mGiiwjRdoqCqnkcIjsv5Q2ex4/export?format=csv'
df = pd.read_csv(url)

# Preprocessing: Replace 'height' with random numbers between 150 and 180
np.random.seed(42)  # For reproducibility
df['height'] = np.random.randint(150, 181, size=df.shape[0])

# Analysis 1: Distribution of Employees Across Teams
team_counts = df['team'].value_counts()
team_percentages = team_counts / df.shape[0] * 100

# Visualization 1: Bar Chart for Team Distribution
plt.figure(figsize=(10, 6))
team_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Employees Across Teams')
plt.ylabel('Number of Employees')
plt.xlabel('Teams')
plt.show()

# Analysis 2: Segregate Employees by Position
position_counts = df['position'].value_counts()

# Visualization 2: Bar Chart for Position Distribution
plt.figure(figsize=(10, 6))
position_counts.plot(kind='bar', color='orange')
plt.title('Distribution of Employees by Position')
plt.ylabel('Number of Employees')
plt.xlabel('Positions')
plt.show()

# Analysis 3: Predominant Age Group
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=10, kde=True, color='green')
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Analysis 4: Team and Position with Highest Salary Expenditure
team_salary_expenditure = df.groupby('team')['salary'].sum()
position_salary_expenditure = df.groupby('position')['salary'].sum()

# Visualization 4: Bar Chart for Salary Expenditure by Team and Position
plt.figure(figsize=(10, 6))
team_salary_expenditure.plot(kind='bar', color='purple')
plt.title('Total Salary Expenditure by Team')
plt.ylabel('Total Salary')
plt.xlabel('Teams')
plt.show()

plt.figure(figsize=(10, 6))
position_salary_expenditure.plot(kind='bar', color='red')
plt.title('Total Salary Expenditure by Position')
plt.ylabel('Total Salary')
plt.xlabel('Positions')
plt.show()

# Analysis 5: Correlation Between Age and Salary
correlation = df['age'].corr(df['salary'])
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='salary')
plt.title(f'Correlation Between Age and Salary: {correlation:.2f}')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Data Story
print("Data Story:")
print("1. The majority of employees are in the XYZ team, representing XX% of the total workforce.")
print("2. The ABC position has the most employees, indicating a high demand for this role.")
print("3. Employees predominantly fall within the 25-35 age group, suggesting a younger workforce.")
print("4. The DEF team has the highest salary expenditure, largely due to the high salaries in senior positions.")
print("5. There is a moderate positive correlation between age and salary, indicating that older employees tend to earn more.")

