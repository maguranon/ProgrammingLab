import numpy as np

co2_emissions = np.round(np.random.uniform(4, 20, 200), 2)
print(f"Prime 10 emissioni: {emissioni_co2[:10]}")

sopra_18 = co2_emissions > 18
quanti_sopra = np.sum(sopra_18)
print(f"\nNumero di valori sopra 18 tonnellate: {quanti_sopra}")
media_sopra = np.mean(co2_emissions[sopra_18])
print(f"Media delle emissioni sopra 18: {media_sopra:.2f} tonnellate")

somma_sopra = np.sum(co2_emissions[sopra_18])
somma_totale = np.sum(co2_emissions)
frazione = somma_sopra / somma_totale

print(f"\nAnalisi complessiva:")
print(f"Emissioni totali: {somma_totale:.2f} tonnellate")
print(f"Emissioni sopra 18t: {somma_sopra:.2f} tonnellate")
print(f"Frazione contributo: {frazione:.1%}")
