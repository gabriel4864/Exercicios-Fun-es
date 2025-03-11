# 3. Crie uma função que recebe uma lista de números e retorna a
# quantidade de números que são múltiplos de 3.

Lista = [6,4,3,5,9,12,1]
def multiplos(Lista):
    contagem = 0
    for i in Lista:
        if i % 3 == 0:
            contagem +=1
    return contagem
print(multiplos(Lista))
    