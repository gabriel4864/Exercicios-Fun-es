# 2. Crie uma função que recebe uma lista de números e retorna a quantidade de números positivos.
Lista = [1,-3,4,-2,-3,7]
def positivos(Lista):
    contagem = 0
    for i in Lista:
        if i > 0:
            contagem += 1
    return contagem
print(positivos(Lista))