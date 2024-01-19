import math
m=47
M=67
p=1.038
c=3.7
K=0.0054
tw=100
pi=math.pi
while True:
    try:
        seleccion=int(input('seleccione el tipo de huevo\n 1 : grande \n 2 : pequeño\n'))
        if seleccion not in [1,2]:
            print('EL HUEVO NO EXISTO')
        else:    
            break
    except ValueError:
        print ('seleccione una opcion valida ')
if seleccion == 1:
    T0=float(input('ingrese la temperatura inicial del huevo: '))
    hG=((math.pow(M,1/3)*c*math.pow(p,1/3))) / (K*math.pow(pi,2))*(math.pow(((4*pi)/3),2/3))
    ln=math.log((0.76*((T0-100)/(70-100))))
    huevoGrande=hG*ln
    print(round(huevoGrande,2))
else:
    T0=float(input('ingrese la temperatura inicial del huevo: '))
    hp=((math.pow(m,1/3)*c*math.pow(p,1/3))) / (K*math.pow(pi,2))*(math.pow(((4*pi)/3),2/3))
    ln=math.log((0.76*((T0-100)/(70-100))))
    huevoPequeño=hp*ln
    print(round(huevoPequeño,2))



