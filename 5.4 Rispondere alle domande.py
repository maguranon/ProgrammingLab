sales = pd.DataFrame(
    data={
        "employee": [
            "Katrina",
            "Guanyu",
            "Jan",
            "Roman",
            "Jacqueline",
            "Paola",
            "Esperanza",
            "Alaina",
            "Egweyn",
        ],
        "sales": [14, 17, 6, 12, 8, 3, 7, 15, 5],
        "year": [2018, 2019, 2020, 2018, 2020, 2019, 2019, 2020, 2020],
    }
)
sales

print("=== DATAFRAME ORIGINALE ===")
print(sales)

# 1. Mostrami le vendite maggiori di 10
vendite_maggiori_di_10 = sales[sales['sales'] > 10]
print("\n1. Vendite > 10:\n", vendite_maggiori_di_10)

# 2. Mostrami i dati del 2018
dati_2018 = sales[sales['year'] == 2018]
print("\n2. Dati 2018:\n", dati_2018)

# 3. Mostrami le vendite maggiori di 13 e l'anno è il 2018
vendite_maggiori_di_13_2018 = sales[(sales['sales'] > 13) & (sales['year'] == 2018)]
print("\n3. Vendite > 13 nel 2018:\n", vendite_maggiori_di_13_2018)

# 4. Mostrami tutto TRANNE i casi in cui le vendite sono maggiori di 13 e l'anno è il 2018
tranne_vendite_maggiori_di_13_2018 = sales[~((sales['sales'] > 13) & (sales['year'] == 2018))]
print("\n4. Tutto tranne vendite > 13 nel 2018:\n", tranne_vendite_maggiori_di_13_2018)

# 5. Mostrami i dati dove le vendite divise per 3 sono maggiori di 3
vendite_divise_per_3_maggiori_di_3 = sales[sales['sales'] / 3 > 3]
print("\n5. Vendite/3 > 3 (cioè vendite > 9):\n", vendite_divise_per_3_maggiori_di_3)

# 6. Mostrami i dipendenti i cui nomi sono alfabeticamente dopo la J
dipendenti_dopo_J = sales[sales['employee'] > 'J']
print("\n6. Dipendenti dopo la J nell'alfabeto:\n", dipendenti_dopo_J)
