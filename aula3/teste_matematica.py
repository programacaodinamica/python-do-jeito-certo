from matematica import eh_par
# Dada uma lista de números inteiros, 
# faça um programa que responda a soma de todos os números pares 
# na lista e o produto de todos os números ímpares.

numeros = [1, 3, 2, 4, 6, 3, 9, 3]
soma = 0
produto = 1
for n in numeros:
    if eh_par(n):
        soma = soma + n
    else:
        produto = produto * n 

print('Soma dos pares: ', soma)
print('Produto dos ímpares: ', produto)