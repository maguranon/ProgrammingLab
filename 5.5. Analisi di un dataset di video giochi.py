num_videogiochi = len(df)
print(f"Numero totale di videogiochi pubblicati: {num_videogiochi}")

generi_counts = df['Genre'].value_counts()

plt.figure(figsize=(12, 6))
generi_counts.plot(kind='bar', color='skyblue')
plt.title('Popolarità dei Generi di Videogiochi')
plt.xlabel('Genere')
plt.ylabel('Numero di giochi')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

giochi_per_anno = df['Year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
giochi_per_anno.plot(marker='o', linestyle='-')
plt.title('Evoluzione del numero di giochi pubblicati nel tempo')
plt.xlabel('Anno')
plt.ylabel('Numero di giochi')
plt.grid(True)
plt.tight_layout()
plt.show()

vendite_per_piattaforma = df.groupby('Platform')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

vendite_per_piattaforma['Global'] = vendite_per_piattaforma.sum(axis=1)
vendite_per_piattaforma = vendite_per_piattaforma.sort_values('Global', ascending=False).drop('Global', axis=1)

top_10_piattaforme = vendite_per_piattaforma.head(10)

plt.figure(figsize=(12, 8))
top_10_piattaforme.plot(kind='bar', stacked=True, 
                        color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.title('Vendite per Piattaforma e Regione (Top 10)')
plt.xlabel('Piattaforma')
plt.ylabel('Vendite (in milioni)')
plt.legend(title='Regione', labels=['Nord America', 'Europa', 'Giappone', 'Altro'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()