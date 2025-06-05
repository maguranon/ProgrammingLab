import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df.head()

print(f"Dimensioni del dataset: {df.shape} (righe, colonne)")

print("\nValori mancanti per colonna:")
print(df.isnull().sum())

most_frequent_embarked = df['Embarked'].mode()[0]
df['Embarked'].fillna(most_frequent_embarked, inplace=True)
print(f"\nValore più frequente in 'Embarked': {most_frequent_embarked}")
df.dropna(subset=['Age'], inplace=True)
duplicates = df.duplicated().sum()
print(f"\nNumero di righe duplicate: {duplicates}")

df = pd.read_csv(url)
df['Embarked'].fillna(most_frequent_embarked, inplace=True)

age_means = df.groupby('Pclass')['Age'].mean()
print("\nEtà media per classe:")
print(age_means)

df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Pclass', y='Age')
plt.title('Distribuzione dell\'età per classe')
plt.xlabel('Classe')
plt.ylabel('Età')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Pclass', y='Age', hue='Sex')
plt.title('Distribuzione dell\'età per classe e generre')
plt.xlabel('Classe')
plt.ylabel('Età')
plt.legend(title='Genere')
plt.show()