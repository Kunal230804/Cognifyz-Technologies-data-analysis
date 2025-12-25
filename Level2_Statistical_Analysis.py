import pandas as pd

df = pd.read_csv('Dataset .csv')

df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

bins = [0, 500, 1000, 2000, 5000, 100000]
labels = ['<500', '500-1000', '1000-2000', '2000-5000', '>5000']
df['Price Range'] = pd.cut(df['Average Cost for two'], bins=bins, labels=labels, right=False)

most_common_price_range = df['Price Range'].mode()[0]

average_rating_by_price_range = df.groupby('Price Range', observed=False)['Aggregate rating'].mean().reset_index()
average_rating_by_price_range.rename(columns={'Aggregate rating': 'Average Rating'}, inplace=True)

highest_avg_rating_row = average_rating_by_price_range.loc[average_rating_by_price_range['Average Rating'].idxmax()]
price_range_with_highest_rating = highest_avg_rating_row['Price Range']

color_for_highest_rated_price_range = df[df['Price Range'] == price_range_with_highest_rating]['Rating color'].mode()[0]


print(f"Most common price range: {most_common_price_range}")
print("\nAverage rating for each price range:")
print(average_rating_by_price_range)
print(f"\nPrice range with the highest average rating: {price_range_with_highest_rating}")
print(f"Color representing the highest average rating: {color_for_highest_rated_price_range}")