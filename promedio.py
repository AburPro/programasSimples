notas=[]
for i in range (4)  :
    Nota = int(input('ingrese la nota: '))
    notas.append(Nota)
print (f'las notas de su periodo son:\n{notas}')
suma=0
for Nota in notas:
    suma += Nota 
promedio=suma/len(notas)
print(f'el promedio de periodo lectivo es: {promedio}')