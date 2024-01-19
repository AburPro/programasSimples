c1=float(input('Ingrese la nota del certamen 1: '))
c2=float(input('Ingrese la nota del certamen 1: '))
l=float(input('Ingrese la nota del laboratorio: ')) 
c3=((60-(l*0.3))/7)-c1-c2
print(f'Necesita nota {round(c3,2)} en el certamen 3')