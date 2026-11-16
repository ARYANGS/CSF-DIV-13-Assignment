import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eve', np.nan],
    'Age': [20, 21, np.nan, 20, 22, 23, 22],
    'Marks': [85, 90, 78, 85, np.nan, 92, 88],
    'City': ['New York', 'London', 'Paris', 'New York', 'Tokyo', np.nan, 'Berlin']
}

df = pd.DataFrame(data)
print("ORIGINAL DATA")
print(df)
print("\n" + "="*40 + "\n")

print("FIRST 3 ROWS")
print(df.head(3))

print("\n DATASET INFO")
df.info()
print("\n" + "="*40 + "\n")

mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

df = df.dropna(subset=['Name', 'Marks'])
print("AFTER HANDLING MISSING VALUES")
print(df)
print("\n" + "="*40 + "\n")

print("CHECKI FOR DUPLICATE ROWS")
print(df.duplicated())

df = df.drop_duplicates()
print("\nAFTER REMOVING DUPLICATES")
print(df)
print("\n" + "="*40 + "\n")

print("=== FILTERED DATA (Marks > 80 using loc[]) ===")
high_scorers = df.loc[df['Marks'] > 80, ['Name', 'Marks', 'City']]
print(high_scorers)
