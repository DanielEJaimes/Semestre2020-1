import numpy as np


meses=np.array(["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
columnas=np.size(meses)


ciudades=np.array(["Bucaramanga","Floridablanca","Girón","Piedecuesta"])
filas=np.size(ciudades)


def generador (min,max):
    datos=np.random.randint(min,max,size=48).reshape(4,12)
    return datos
ingresos=generador(100,181)
egresos=generador(60,131)


def imprimir ():
    print("Ingresos")
    for i in range(0,filas):
        print (ciudades[i],ingresos[i])
    print("Egresos")
    for i in range(0,filas):
        print (ciudades[i],egresos[i])
imprimir ()


print("Ganancias")
def calculador(ingresos,egresos):
    ganancias=(ingresos-egresos)
    return ganancias
ganancias=calculador(ingresos,egresos)


def mejor_ciudad(ganancias):
    m_ciudad="Error"
    mejor=np.sum(ganancias[0])
    for i in range (0,filas):
        if np.sum(ganancias[i])>mejor:
            mejor=np.sum(ganancias[i])
            m_ciudad=ciudades[i]    
    return m_ciudad
a=mejor_ciudad(ganancias)
print("La mejor ciudad es ",a)


def peor_ciudad(ganancias):
    p_ciudad="Error"
    peor=np.sum(ganancias[0])
    for i in range (0,filas):
        if np.sum(ganancias[i])<peor:
            peor=np.sum(ganancias[i])
            p_ciudad=ciudades[i]
    return p_ciudad
b=peor_ciudad(ganancias)
print("La peor ciudad es ",b)


def mejor_mes(ganancias):
    mes=0
    for i in range(0,filas):
        mes=0
        mejor_mes=np.max(ganancias[i])
        for j in range(0,columnas):
            if mejor_mes==ganancias[i,j]:
                mes=meses[j]
    return mes
c=mejor_mes(ganancias)
print("El mejor mes fue ",c)


def imprimir_personalizado(ingresos,minmes,maxmes):
    i_personalizado=ingresos[:4,minmes-1:maxmes]
    for i in range (0,filas):
        print(ciudades[i],i_personalizado[i])
    return i_personalizado
imprimir_personalizado(ingresos,3,6)