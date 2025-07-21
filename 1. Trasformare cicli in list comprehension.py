quadrati = []
for i in range(10):
    quadrati.append(i**2)
print("Quadrati (for-loop):", quadrati)

quadrati = [i**2 for i in range(10)]
print("Quadrati (list comprehension):", quadrati)

pari = []
for i in range(10):
   if i % 2 == 0:
       pari.append(i)
print("Numeri pari (for-loop):", pari)

pari = [i for i in range(10) if i % 2 == 0]
print("Numeri pari (list comprehension):", pari)

pari_e_quadrati = []

for i in range(100):
   if i % 2 == 0:
       pari_e_quadrati.append(i**2)
print("Quadrato dei pari (for-loop) - primi 5:", pari_e_quadrati[:5], "...")
pari_e_quadrati = [i**2 for i in range(100) if i % 2 == 0]
print("Quadrato dei pari (list comprehension) - primi 5:", pari_e_quadrati[:5], "...")
