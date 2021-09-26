def minutos_para_horas(qtd_minutos):
    horas = qtd_minutos // 60
    minutos = qtd_minutos %60
    return f'{horas}h:{minutos}min'

minutos = int(input('Digite uma quantidade de minutos:'))
horas = minutos_para_horas(minutos)
print(f'A quantidade de {minutos} minutos em horas é igual a {horas}')
