import numpy as np 
uti=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])
def promedio (uti):
    long=len(uti)
    media1=(uti[0]+uti[1])/2
    media2=(uti[long-1]+uti[long-2])/2
    promedio=media1-media2
    print("La diferencia de la media es de: ",promedio)
    return promedio
promedio(uti)
def diferencia (uti):
    minuti=np.min(uti)
    maxuti=np.max(uti)
    diferencia=maxuti-minuti
    print("La diferencia entre las utilidades fue: ",diferencia)
    return diferencia
diferencia(uti)
def mediana (uti):
    uti=np.sort(uti)
    long=len(uti)
    n=int(long/2)
    mediana=(uti[n]+uti[n-1])/2
    print("La mediana de la utilidad es: ",mediana)
    return mediana
mediana(uti)
def porcentaje (uti):
    long=len(uti)
    cont=2008
    suma=np.sum(uti)
    porcentajes=[]
    for i in range (0,long):
        porcentaje=(uti[i]*100)/suma
        porcentajes.append(porcentaje)
        print("El porcentaje en el año ",cont," fue de ",porcentajes[i],"%")
        cont=cont+1
    return porcentaje
porcentaje(uti)
deficit=uti[9]-uti[8]
print("El deficit en la utilidad del año 2017 con respecto al año 2016 es de: ",deficit," millones de COP")
