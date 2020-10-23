# Escreva um programa que recebe um número inteiro 
# do usuário e responde se esse número é par ou não

def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def maximo(lista):
    maior = -9999999999
    for n in lista:
        if n > maior:
            maior = n
    return maior

def media(lista):
    m = 0
    for n in lista:
        # acumulando a soma da lista
        m = m + n
    # retorna a média
    return m/len(lista)

def fatorial(n):
    produto = 1
    while n > 0:
        produto = produto * n
        n = n - 1
    return produto
