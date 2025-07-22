import numpy as np

numeri_primi = np.array([2, 3, 5, 7]) 

print("Quanti numeri ci sono nell'array? " + str(len(numeri_primi))) 
print("Quanti numeri ci sono nell'array? " + str(numeri_primi.size)) 

'''
Quale pensi sia il tipo di dato (dtype) del vettore?
Prova a rispondere senza eseguire il codice e
verifica la tua risposta accedendo all'attributo .dtype del vettore.
'''

print("Tipo di dato dell'array (dtype):", numeri_primi.dtype)  

def is_primo(n):
    if n < 2:
        return False
    
    div = 0
    i = n
    while i >= 1:
        if n % i == 0:
            div += 1
            if div > 2: 
                return False
        i -= 1
    
    return div == 2

array_num_primi = np.array([i for i in range(10) if is_primo(i)])
print("Numeri primi tra 0 e 9:", array_num_primi)
