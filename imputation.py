import pandas as pd
import numpy as np
data = {
    'Item': ['Apples', 'Bananas', 'Bread', 'Milk', 'Eggs', 'Butter', 'Cheese', 'Tomatoes', 'Potatoes', 'Onions'],
    'Category': ['Fruit', 'Fruit', 'Bakery', 'Dairy', 'Dairy', 'Dairy', 'Dairy', 'Vegetable', 'Vegetable', 'Vegetable'],
    'Price': [120, 60, np.nan, 45, 80, np.nan, 150, 90, 50, 40],
    'Quantity_Sold': [30, np.nan, 25, 40, 50, 20, np.nan, 35, 60, np.nan],
    'Discount': [5, 10, 0, np.nan, 5, 0, 10, np.nan, 0, 0]
}

df = pd.DataFrame(data)
print("Before Imputation Data:\n", df)
input_from_user = input("Enter the type of imputation (mean/median/mode): ").strip().lower()

if input_from_user == 'mean':
    for column in ['Price', 'Quantity_Sold', 'Discount']:
        df[column].fillna(df[column].mean(), inplace=True)
        print("\nAfter Imputation Data:\n", df)

elif input_from_user == 'median':
    for column in ['Price', 'Quantity_Sold', 'Discount']:
        df[column].fillna(df[column].median(), inplace=True)
        print("\nAfter Imputation Data:\n", df)

elif input_from_user == 'mode':
    for column in ['Price', 'Quantity_Sold', 'Discount']:
        df[column].fillna(df[column].mode()[0], inplace=True)
        print("\nAfter Imputation Data:\n", df)

else:
    print("Invalid input. Please enter 'mean', 'median', or 'mode'.")
    
