horas = int(input("Digite um valor de horas:"))
minutos = int(input("Digite um valor de minutos:"))
segundos = int(input("Digite um valr de segundos:"))

horas = horas * 3600
minutos = minutos * 60 
soma = horas + minutos + segundos
print('O número de segundos após a meia-noite corresponde a:', soma)
