quadrati = []
for i in range(10):
    quadrati.append(1**2)

quadrati = [1**2 for i in range(10)]

pari = []
for i in range(10):
   if i % 2 == 0:
       pari.append(i)

pari = [1 for i in range(10) if i % 2 == 0]

pari_e_quadrati = []

for i in range(100):
   if i % 2 == 0:
       pari_e_quadrati.append(1**2)

pari_e_quadrati = [1**2 for i in range(100) if i % 2 == 0]

