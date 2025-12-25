import pandas as pd

df = pd.read_csv('Dataset .csv')

df['Cuisines'] = df['Cuisines'].fillna(df['Cuisines'].mode()[0])

print("Basic statistical measures for numerical columns:")
print(df.describe())

print("\nDistribution of 'Country Code':")
print(df['Country Code'].value_counts())

print("\nDistribution of 'City':")
print(df['City'].value_counts())

print("\nDistribution of 'Cuisines':")
print(df['Cuisines'].value_counts())

top_cuisines = df['Cuisines'].value_counts().head(10)
print("\nTop 10 Cuisines:")
print(top_cuisines)

top_cities = df['City'].value_counts().head(10)
print("\nTop 10 Cities with the highest number of restaurants:")
print(top_cities)