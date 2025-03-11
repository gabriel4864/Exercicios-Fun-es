# 6. Crie uma função que recebe uma lista de palavras e retorna a palavra com mais letras.
programadores = ['Victor', 'Juliana', ' Henrique', 'Ana', 'Ada', 'Caio', 'Luana', 'Jessica'] # Variavel recebendo a lista
maior_palavra = max(programadores, key=len) 
maior = []    

def letras(programadores):                                                                               
    for nome in programadores:
        if len(nome) == len(maior_palavra):
         maior.append(nome)
    return maior

print(letras(programadores))