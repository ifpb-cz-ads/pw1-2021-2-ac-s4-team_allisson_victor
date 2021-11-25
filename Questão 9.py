dias = int(input("Digite os dias: "))
horas = int(input("Digite os horas: "))
minutos = int(input("Digite os minutos: "))
segundos= int(input("Digite os segundos: "))

total = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Tudo isso em segundos é igual a %d segundos." %total)