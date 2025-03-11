# 7. Crie uma função que recebe uma lista de números e retorna a soma apenas dos números pares.
Lista = [2,3,4,5,2,9]
pares = []
def soma(Lista):
    for i in Lista:
        if i % 2 == 0:
            pares.append(i)
    return sum(pares)   
print(soma(Lista))
