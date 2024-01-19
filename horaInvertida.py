from os import system
system('clear')
t = float(input('ingrese la hora actual: '))
h = int(input('ingrese el numero entero de horas: '))
for i in range(1):
    hora=(t+h)%24
print(f'la hora futura sera {round(hora,3)}')