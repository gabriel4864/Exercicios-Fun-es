# Exercício 4: Crie uma função que calcule o fatorial de um número.
numero = int(input("Digite um numero: "))
def fatorial(numero,num = 1):
   for i in range(numero):
      num *= (i+1)
   return num
print(fatorial(numero))