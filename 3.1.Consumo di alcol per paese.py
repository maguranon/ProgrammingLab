import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")

top10_alcool = df.sort_values(by='total_litres_of_pure_alcohol', ascending=False).head(10)

media_birra = df['beer_servings'].mean()
media_vino = df['wine_servings'].mean()
media_distillati= df['spirit_servings'].mean()

print(f"Media birra: {media_birra:.1f} servings")
print(f"Media vino: {media_vino:.1f} servings")
print(f"Media distillati: {media_distillati:.1f} servings")

df['alcohol_index'] = (df['beer_servings'] + df['wine_servings'] + df['spirit_servings']) / 3

paese_max_index = df.loc[df["alcohol_index"].idmax(), 'country']
print(f"\nPaese con indice alcolico più alto: {paese_max_index}")

piu_di_100_birre = df[df['beer_servings'] > 100]
print(f"\nPaesi con più di 100 servings di birra: {len(piu_di_100_birre)}")

plt.figure(figsize=(10,6))
plt.bar(top10_alcool['country'], top10_alcool['total_litres_of_pure_alcohol'], color='red')
plt.xticks(rotation=45)
plt.title("top 10 paesi per il consumo di alcool")
plt.ylabel("litri di alcool")
plt.show()

ordinare_vino = df.sort_values(by='wine_serving')
plt.figure(figsize=(12,6))
plt.plot(ordinare_vino['country'], ordinare_vino['wine_servings'], marker='o', linestyle='-')
plt.xticks(rotation=90)
plt.title("consumo di vino")
plt.ylabel("Wine serving")
plt.tight_layout()
plt.show()
