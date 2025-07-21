import numpy as np
stipendi = np.array([50000.0, 105250.0, 55000.0, 89000.0])
print("Salario iniziale:", stipendi)

totale_iniziale = np.sum(stipendi)
print("\nSalario iniziale totale:", totale_iniziale)
stipendi[stipendi == 105250.0] *= 1.15
print("\nADopo il primo tentativo (float dtype):", stipendi)
stipendi = np.array([50000.0, 105250.0, 55000.0, 89000.0], dtype=object)
print("\nRicreare array con object dtype:", stipendi)
stipendi[stipendi == 105250] = 105250 * 1.15
stipendi[stipendi == 50000] = 50000 * 1.20
print("\nDopo una specifica crescita:", stipendi)

for i in range(len(stipendi)):
    if stipendi[i] not in [105250 * 1.15, 50000 * 1.20]:
        stipendi[i] *= 1.10
print("\nDopo tutte le crescite:", stipendi)        

totale_finale = np.sum(stipendi)
print("\nsalario totale finale:", totale_finale)

aumento_ceo = 105250 * 0.15
costo_aumento_ceo = totale_finale - totale_iniziale
print("\nCEO crescita:", aumento_ceo)
print("Total tutte crescite costo:", costo_aumento_ceo)
