# 1. Mostrami le vendite maggiori di 10
vendite_maggiori_di_10 = sales[sales['sales'] > 10]

# 2. Mostrami i dati del 2018
dati_2018 = sales[sales['year'] == 2018]

# 3. Mostrami le vendite maggiori di 13 e l'anno è il 2018
vendite_maggiori_di_13_2018 = sales[(sales['sales'] > 13) & (sales['year'] == 2018)]

# 4. Mostrami tutto TRANNE i casi in cui le vendite sono maggiori di 13 e l'anno è il 2018
tranne_vendite_maggiori_di_13_2018 = sales[~((sales['sales'] > 13) & (sales['year'] == 2018))]

# 5. Mostrami i dati dove le vendite divise per 3 sono maggiori di 3
vendite_divise_per_3_maggiori_di_3 = sales[sales['sales'] / 3 > 3]
4. Rispondere alle domande
# 6. Mostrami i dipendenti i cui nomi sono alfabeticamente dopo la J
dipendenti_dopo_J = sales[sales['employee'] > 'J']