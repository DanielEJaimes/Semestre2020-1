import math
print("Programa para dar solucion a una ecuacion cuadratica")
a=int(input("Ingrese el valor de a,es decir,el numero que acompaña la x al cuadrado\n"))
b=int(input("Ingrese el valor de b,es decir,el numero que acompaña a la x\n"))
c=int(input("Ingrese el valor de c,es decir,el numero que esta solo\n"))
d=(b*b)-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print("El valor de la x1 es:",x1," y el valor de x2 es:",x2)
if d==0:
    x=(-b)/2*a
    print("x1 y x2 son iguales y corresponden a: ",x)
if d<0:
    print("La respuesta no existe dentro del dominio de los numeros reales")
