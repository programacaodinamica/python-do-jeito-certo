import csv


# with open('projeto/data/eleitores.csv') as meucsv:
#     leitor = csv.DictReader(meucsv, delimiter=';')
#     with open('teste.csv', 'w') as test:
#         writer = csv.DictWriter(test, fieldnames=[
#             'nome',
#             'mae',
#             'pai',
#             'data_nasc',
#             'titulo', 
#             'zona', 
#             'secao', 
#             'municipio', 
#             'uf', 
#             'data_insc', 
#             'votou'
#         ])
#         writer.writeheader()
#         for linha in leitor:
#             writer.writerow(linha)
#             #print(linha['nome'], linha['mae'], linha['data_nasc'])

with open('projeto/certidao.html') as certidao:
    conteudo = certidao.read()
    atualizada = conteudo.replace('$NOME$', 'Hallison Paz')
    with open('teste.html', 'w') as test:
        test.write(atualizada)