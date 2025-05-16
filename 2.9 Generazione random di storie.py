import random 

lista_parole = [
    'INSEDIAMENTO', 'SEPARAZIONE', 'DIFFERENZA', 'APPLICAZIONE', 'ATTEGGIAMENTO', 'VERDURA', 'IMPERO', 'RICEVIMENTO',
    'IGNORANZA', 'BIOGRAFIA', 'VISIONE', 'AGENTE DI POLIZIA', 'PROVA', 'PRESTAZIONE', 'PRESENTAZIONE', 'PARENTE',
    'GIUSTIFICAZIONE', 'FILOSOFIA', 'DIREZIONE', 'BENEFICIARIO', 'BATTERIA', 'CERIMONIA', 'AGONIA', 'RECUPERO',
    'ALFABETIZZAZIONE', 'CONSEGNA', 'SERBATOIO', 'VOLONTARIO', 'DEPOSITO', 'BIRILLO DA BOWLING', 'NEMICO', 'ANNUNCIO',
    'CARAMELLA ZUCCHERATA', 'FULMINE', 'PALLONCINO', 'COPERTA', 'SCOPERTA', 'PENALITÀ', 'GENERALE', 'ALPACA',
    'VANTAGGIO', 'HOT DOG', 'ABITO', 'MATEMATICA', 'VARIANTE'
]

parole_estratte = random.choices(lista_parole, k=5)

frase = f"""
"In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico {parole_estratte[0]} che proteggeva.
Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto abbondante e le offrì il {parole_estratte[1]} come dono, i suoi occhi si spalancarono e lei esclamò una sola parola, "{parole_estratte[2]}".
Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un {parole_estratte[3]}.
Nel 101° giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla donna saggia per donarglielo.
Con un sorriso da un orecchio all’altro, e cantando canti di festa, la donna saggia guardò i suoi compaesani e disse: "Ora è giunto il tempo del banchetto - nessuno rimarrà mai più senza {parole_estratte[4]}!"

Ci fu grande gioia e celebrazione."
"""

print(frase)
