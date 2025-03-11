# Exercício 9: Crie uma função que conte quantas vogais existem em uma string fornecida.
palavra = input("Digite uma palavra: ")
vogais = "aeiou"
contagem = 0
def ex(palavra):
    global contagem
    for i in palavra:
        if i in vogais:
            contagem +=1
    return contagem 

print(ex(palavra))