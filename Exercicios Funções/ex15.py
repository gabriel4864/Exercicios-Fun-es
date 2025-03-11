# 5. Crie uma função que recebe uma lista de números e substitui os números negativos por zero.
Lista = [-1,3,-4,2,-9,-1]
def substituir(Lista):
    for i in range(len(Lista)):
        if Lista[i]<0:
            Lista[i]=0
    return Lista
print(substituir(Lista))
