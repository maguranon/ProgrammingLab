import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")

top10_alcool = df.sort_values(by='total_litres_of_pure_alcohol', ascending=false).head(10)

media_birra = df['beer_servings'].mean()
media_vino = df['wine_servings'].mean()
media_distillati= df['spirit_servings'].mean()

df[alcohol_index] = (df['beer_servings'] + df['wine_servings'] + df['spirit_servings']) / 3

paese_max_index = df["alcohol_index"].max()

piu_di_100_birre = df[df['beer_servings'] > 100]

plt.figure(figsize=(10,6))
plt.bar(top10_alcool['country'], top10_alcool['total_litres_of_pure_alcohol'], color='red')
plt.xticks(rotation=45)
plt.title("top 10 paesi per il consumo di alcool")
plt.ylabel("litri di alcool")
plt.show

ordinare_vino = df.sort_values(by='wine_serving')
plt.figure(figsize=(12,6))
plt.bar(ordinare_vino['country'], ordinare_vino['wine_servings'], marker='o', linestyle='-')
plt.xticks(rotation=90)
plt.title("consumo di vino")
plt.ylabel("Wine serving")
plt.tight_layout()
plt.show