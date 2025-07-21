import numpy as np
stipendi = np.array([50000.0, 105250.0, 55000.0, 89000.0])
totale_iniziale = np.sum(stipendi)
stipendi[stipendi == 105250.0] *= 1.15
stipendi = np.array([50000.0, 105250.0, 55000.0, 89000.0], dtype=object)
stipendi[stipendi == 105250] = 105250 * 1.15
stipendi[stipendi == 50000] = 50000 * 1.20

for i in range(len(stipendi)):
    if stipendi[i] not in [105250 * 1.15, 50000 * 1.20]:
        stipendi[i] *= 1.10

totale_finale = np.sum(stipendi)
aumento_ceo = 105250 * 0.15
costo_aumento_ceo = totale_finale - totale_iniziale
