import math
try:
    r=int(input('cual es el radio del circulo: '))
except:
    print('escriba un dato valido')
else:
    pi=math.pi
    perimetro=r*pi*2
    area= pi *(r**2)
    print(f'el perimetro del circulo es {perimetro}')
    print(f'el area del circulo es {area}')