# save - salvar em arquivo
def save(mensagem):
    # salva a mensagem em um arquivo
    arquivo = open('mensagem.txt', 'w')
    arquivo.write(mensagem)
    arquivo.close()

def status_de_voto(idade):
    if idade >= 18 and idade < 70:
        return 'obrigatorio'
    elif idade >= 16:
        return 'facultativo'
    else:
        return 'proibido'

# Resolvendo de outra forma
def voto_eleitoral(idade):
    if idade >= 16 and idade < 18 or idade >= 70:
        return 'facultativo'
    elif idade < 16:
        return 'proibido'
    else:
        return 'obrigatório'
    
idade = int(input('Digite sua idade: '))
resposta = status_de_voto(idade)

print(f'Com {idade} anos, seu voto é {resposta}')