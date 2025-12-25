import pandas as pd

df = pd.read_csv('Dataset .csv')

df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

df['Has Table booking'] = df['Has Table booking'].apply(lambda x: True if x == 'Yes' else False)
df['Has Online delivery'] = df['Has Online delivery'].apply(lambda x: True if x == 'Yes' else False)

total_restaurants = len(df)
restaurants_with_table_booking_and_online_delivery = df[(df['Has Table booking'] == True) & (df['Has Online delivery'] == True)].shape[0]
percentage_table_booking_and_online_delivery = (restaurants_with_table_booking_and_online_delivery / total_restaurants) * 100

avg_rating_with_table_booking = df[df['Has Table booking'] == True]['Aggregate rating'].mean()
avg_rating_without_table_booking = df[df['Has Table booking'] == False]['Aggregate rating'].mean()

bins = [0, 500, 1000, 2000, 5000, 100000]
labels = ['<500', '500-1000', '1000-2000', '2000-5000', '>5000']
df['Price Range'] = pd.cut(df['Average Cost for two'], bins=bins, labels=labels, right=False)

online_delivery_by_price_range = df.groupby('Price Range', observed=False)['Has Online delivery'].value_counts(normalize=True).unstack()
print(f"Percentage of restaurants with table booking and online delivery: {percentage_table_booking_and_online_delivery:.2f}%")
print(f"Average rating of restaurants with table booking: {avg_rating_with_table_booking:.2f}")
print(f"Average rating of restaurants without table booking: {avg_rating_without_table_booking:.2f}")
print("\nOnline delivery availability by price range:")
print(online_delivery_by_price_range)