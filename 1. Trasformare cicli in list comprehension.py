quadrati = []
for i in range(10):
    quadrati.append(i**2)

quadrati = [i**2 for i in range(10)]

pari = []
for i in range(10):
   if i % 2 == 0:
       pari.append(i)

pari = [i for i in range(10) if i % 2 == 0]

pari_e_quadrati = []

for i in range(100):
   if i % 2 == 0:
       pari_e_quadrati.append(i**2)

pari_e_quadrati = [i**2 for i in range(100) if i % 2 == 0]

