import pandas as pd
import plotly.express as px

df = pd.read_csv('Dataset .csv')

df['Cuisines'] = df['Cuisines'].fillna(df['Cuisines'].mode()[0])

fig = px.scatter_map(df,
                     lat="Latitude",
                     lon="Longitude",
                     color="Aggregate rating",
                     size="Votes",
                     hover_name="Restaurant Name",
                     hover_data=["City", "Country Code", "Cuisines", "Price range"],
                     zoom=1,
                     title="Restaurant Locations with Aggregate Rating and Votes",
                    )

fig.show()

avg_rating_per_country = df.groupby('Country Code')['Aggregate rating'].mean().sort_values(ascending=False)
print("\nAverage Aggregate Rating per Country Code:\n", avg_rating_per_country)

avg_rating_per_city = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(20)
print("\nAverage Aggregate Rating per City (Top 20):\n", avg_rating_per_city)