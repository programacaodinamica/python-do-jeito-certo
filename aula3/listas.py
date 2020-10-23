# Faça um programa que recebe uma lista de números reais 
# e exibe o seu maior elemento.

numeros_em_texto = input('Digite alguns números:\n')
# quebra uma string nos espaços
lista = numeros_em_texto.split()
numeros = []
for elem in lista:
    n = float(elem)
    numeros.append(n)

maior = -999999999999
for n in numeros:
    if n > maior:
        maior = n
print(maior)

# fizemos um código equivalente a esta função:
print(max(numeros))
