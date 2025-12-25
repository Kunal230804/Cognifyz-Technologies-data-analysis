import pandas as pd

df = pd.read_csv('Dataset .csv')

num_rows, num_cols = df.shape

missing_values = df.isnull().sum()

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")
print("\nMissing values in each column:\n", missing_values)

df['Cuisines'] = df['Cuisines'].fillna(df['Cuisines'].mode()[0])

missing_values_after_imputation = df.isnull().sum()
print("\nMissing values after imputation:\n", missing_values_after_imputation)

print("\nData types of columns:\n", df.dtypes)

aggregate_rating_distribution = df['Aggregate rating'].value_counts().sort_index()
print("\nDistribution of 'Aggregate rating':\n", aggregate_rating_distribution)