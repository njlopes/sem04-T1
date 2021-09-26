def area_do_piso(largura, comprimento):
    return largura * comprimento
def volume_da_sala(largura, comprimento, altura):
    return largura * comprimento * altura
def area_das_paredes(altura, largura, comprimento):
    return 2 * altura * largura + 2 * altura * comprimento

altura=int(input('Valor da altura:'))
comprimento=int(input('Valor do comprimento:'))
largura=int(input('Valor da largura:'))

print('Área do piso corresponde a:', area_do_piso(largura, comprimento))
print('Volume da sala correponde a:', volume_da_sala(largura, comprimento, altura))
print('Área das paredes correponde a:', area_das_paredes(altura, largura, comprimento))

