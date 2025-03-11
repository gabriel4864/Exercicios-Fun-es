# Exercício 6: Crie uma função que receba uma string e retorne True se ela for
# um palíndromo (uma palavra ou frase que se lê da mesma forma de trás para
# frente) e False caso contrário.
palavra = str(input("Digite uma palavra: "))
palavra_inversa = palavra[::-1]
def palidromo(palavra):
    if palavra == palavra_inversa:
        return "True"
    else: 
        return "False" 
print(palidromo(palavra))