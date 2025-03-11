# 1. Crie uma função que recebe duas palavras e retorna True se forem anagramas uma da outra.
palavra1 = "amor"
palavra2 = "roma"
def anagramas(palavra1):
    for i in palavra2:
        if i in palavra1:
            return "True"
        else: 
            return "False"
print(anagramas(palavra1))
