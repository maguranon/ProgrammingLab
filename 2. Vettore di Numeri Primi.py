import numpy as np

numeri_primi = np.array([2, 3, 5, 7]) 

print("Quanti numeri ci sono nell'array? " + str(len(numeri_primi))) 
print("Quanti numeri ci sono nell'array? " + str(numeri_primi.size)) 

'''
Quale pensi sia il tipo di dato (dtype) del vettore?
Prova a rispondere senza eseguire il codice e
verifica la tua risposta accedendo all'attributo .dtype del vettore.
'''

# Il dtype dovrebbe essere int (intero)
print("Tipo di dato dell'array (dtype):", numeri_primi.dtype)  # Verifica del dtype

def is_primo(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

array_num_primi = np.array([i for i in range(10) if is_primo(i)])