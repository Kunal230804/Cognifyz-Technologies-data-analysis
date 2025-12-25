import pandas as pd

df = pd.read_csv('Dataset .csv')

df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

df['Restaurant Name Length'] = df['Restaurant Name'].apply(lambda x: len(str(x)))
df['Address Length'] = df['Address'].apply(lambda x: len(str(x)))

df['Has Table booking_Encoded'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online delivery_Encoded'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

print("DataFrame with new features:")
print(df[['Restaurant Name', 'Restaurant Name Length', 'Address', 'Address Length',
          'Has Table booking', 'Has Table booking_Encoded',
          'Has Online delivery', 'Has Online delivery_Encoded']].head())