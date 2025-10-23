import pandas as pd
import numpy as np

data = {
    'Age': [22, 25, 28, 24, 30, 35, 40, 26, 31, 27],
    'Salary': [30000, 35000, 40000, 32000, 45000, 50000, 55000, 37000, 48000, 39000],
    'Department': ['HR', 'IT', 'Sales', 'HR', 'Sales', 'IT', 'HR', 'IT', 'Sales', 'HR'],
    'Education': ['High School', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Masters', 'High School', 'Bachelors']
}

df = pd.DataFrame(data)
dictionary = {}  
print("Original DataFrame:\n", df)

for education in df['Education'].unique():
    number = float(input(f"Enter number u want to assign for {education}: "))
    
    dictionary[education] = number

df.replace({
    'Education': dictionary
}, inplace=True)

print("\nDataFrame after Ordinal Encoding:\n",df)
