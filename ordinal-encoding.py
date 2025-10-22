import pandas as pd
import numpy as np


data = {
    'Age': [22, 25, 28, 24, 30, 35, 40, 26, 31, 27],  # Non-categorical
    'Salary': [30000, 35000, 40000, 32000, 45000, 50000, 55000, 37000, 48000, 39000],  # Non-categorical
    'Department': ['HR', 'IT', 'Sales', 'HR', 'Sales', 'IT', 'HR', 'IT', 'Sales', 'HR'],  # Nominal (categorical, unordered)
    'Education': ['High School', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Masters', 'High School', 'Bachelors'] 
    }

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

df.replace({
    'Education': { 'High School': 1, 'Bachelors': 2, 'Masters': 3, 'PhD': 4 }
}, inplace=True)

print("\nDataFrame after Ordinal Encoding:\n", df)

