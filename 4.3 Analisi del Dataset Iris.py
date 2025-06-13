import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
df.head()

print(df['species'].value_counts)
media_petali = df.groupby('species')[['petal_length', 'petal_width']].mean()
print(media_petali)

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species')
plt.title('Dimensioni dei petali per specie')
plt.xlabel('Lunghezza petalo')
plt.ylabel('Larghezza petalo')
plt.grid(True)
plt.show()

df['petal_area'] = df['petal_length'] * df['petal_width']
print(df[['species', 'petal_area']].groupby('species').describe())

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='species', y='petal_area')
plt.title('Distribuzione dell’area del petalo per specie')
plt.xlabel('Specie')
plt.ylabel('Area del petalo')
plt.grid(True)
plt.show()