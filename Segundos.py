def h(horas):
    return horas * 3600
def min(minutos):
    return minutos * 60


horas = int(input("Digite um valor de horas:"))
minutos = int(input("Digite um valor de minutos:"))
segundos = int(input("Digite um valor de segundos"))
soma = h(horas) + min(minutos) + segundos
print('O número de segundos após meia-noite correponde a:', soma)
