# Numero par ou impar
Numero = int(input("Digite um numero"))

def par_impar(Numero): 
    if Numero %2 == 0: 
        return "par"
    else:
        return "impar"
    
print(par_impar(Numero))