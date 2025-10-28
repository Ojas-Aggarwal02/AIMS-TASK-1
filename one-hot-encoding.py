import pandas as pd
import numpy as np

data = {
    'Age': [25, 30, 22, 28, 35, 40, 29, 31, 27, 33],
    'Salary': [30000, 40000, 28000, 35000, 45000, 50000, 37000, 42000, 34000, 46000],
    'Department': ['HR', 'IT', 'Sales', 'HR', 'IT', 'Marketing', 'Sales', 'Marketing', 'IT', 'HR']
}

df = pd.DataFrame(data)

print("Before one-hot encoding:\n" , df)

options=df['Department'].unique()

for i in options:
    x = (df['Department']==i)
    df[i]=x.astype(int)

df.drop(columns='Department', inplace=True)

print("After one hot encoding:\n ", df)
