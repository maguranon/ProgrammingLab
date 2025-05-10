import numpy as np

co2_emissions = np.round(np.random.uniform(4, 20, 200), 2)

sopra_18 = co2_emissions > 18
quanti_sopra = np.sum(sopra_18)
media_sopra = np.mean(co2_emissions[sopra_18])

# Frazione totale
somma_sopra = np.sum(co2_emissions[sopra_18])
somma_totale = np.sum(co2_emissions)
frazione = somma_sopra / somma_totale