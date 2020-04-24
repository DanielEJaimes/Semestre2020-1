import math
lista=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]
lista2=lista.copy()
lista2.sort()
long=len(lista)


def diferencia_mayor_menor(lista):
    dif=lista[-1]-lista[0]
    return dif
dif=diferencia_mayor_menor(lista2)
print ("La diferencia entre la mayor y menor presion promedio semanal registrada es de:", dif)


def suma_presiones_total (lista):
    suma_presiones=0
    for i in range(0,long):
        suma_presiones=suma_presiones+lista[i]
    return suma_presiones
suma_presiones=suma_presiones_total(lista)


def media(lista):
    promedio=suma_presiones/long
    return promedio
media=media(lista)
print ("La media de las presiones es: ",media)


def mediana(lista):
    long=len(lista2)
    cant_datos=long/2
    cant_datos=int(cant_datos)
    mediana_total=lista2[cant_datos]+lista2[cant_datos-1]
    mediana_total=mediana_total/2
    return mediana_total
mediana_total=mediana(lista2)
print("La mediana de las presiones es: ",mediana_total)


def mayores_promedio (lista):
    lista3=[]
    for i in range (0,long):
        if lista[i] > media:
            lista3.append(lista[i])
    return lista3
lista3=mayores_promedio(lista)
print ("Las presiones mayores al promedio son:",lista3)




def temperatura_semanal (lista):
    temperaturas=[]
    for i in range (0,long):
        presion=lista[i]/101
        temperatura=((presion*510)/(17.16*0.082))-273
        temperaturas.append(temperatura)
    return temperaturas
temperaturas=temperatura_semanal(lista)


def suma_temperaturas_total (temperaturas):
    suma_temperaturas=0
    for i in range(0,long):
        suma_temperaturas=suma_temperaturas+temperaturas[i]
    return suma_temperaturas
suma_temperaturas=suma_temperaturas_total(temperaturas)


def media_temperaturas(temperaturas):
    promedio_temperaturas=suma_temperaturas/long
    return promedio_temperaturas
media_temperaturas=media_temperaturas(temperaturas)
print ("La media de las temperaturas es:",media_temperaturas)


def desviacion_estandar_temperaturas(lista):
    suma_temperaturas=0
    for i in range (0,long):
        suma_temperaturas=suma_temperaturas+((lista[i]-media_temperaturas)**2)
        s=math.sqrt(suma_temperaturas/(long-1))
    return s
s= desviacion_estandar_temperaturas(temperaturas)
print ("La desviacion estandar de las temperaturas es:",s)


def mayores_temperaturas_promedio (temperaturas):
    temperaturas2=[]
    for i in range (0,long):
        if temperaturas[i] > media_temperaturas:
            temperaturas2.append(temperaturas[i])
    return temperaturas2
temperaturas2=mayores_temperaturas_promedio(temperaturas)
print ("Las temperaturas mayores a el promedio son:",temperaturas2)


def menores_temperaturas_promedio (temperaturas):
    temperaturas3=[]
    for i in range (0,long):
        if temperaturas[i] < media_temperaturas:
            temperaturas3.append(temperaturas[i])
    return temperaturas3
temperaturas3=menores_temperaturas_promedio(temperaturas)
print ("Las temperaturas menores a el promedio son:",temperaturas3)

