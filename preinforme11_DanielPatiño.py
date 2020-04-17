import numpy as np
datos=np.array([[4.1315,4.3063,4.1961,4.3517,4.2235,4.3772,4.6318,4.6639,4.7422,4.2718,3.9881,4.3419],
[3.366,3.5257,3.0164,2.9384,3.1146,3.4187,3.5895,3.6293,3.6523,3.1703,2.8728,2.8134]])
print ("Situacion problema 1:Mes mas calido del año entre ambos municipios")
def mascalido(datos):
        filas,columnas=datos.shape
        mascalido=datos[0,0]
        for i in range(0,filas):
                for j in range(0,columnas):
                        if datos[i,j]>mascalido:
                                mascalido=datos[i,j]
                                x=j+1
                                y=i
                                if y == 0:
                                        s="Girardot"
                                else:
                                        s="San Vicente de Chucuri"
        print ("El ",x," mes del año es el mas calido con una radiacion de: ",mascalido," en el municipio de",s)
        return mascalido
mascalido(datos)
print ("Situacion problema 2:Mes mas frio del año entre ambos municipios")
def masfrio(datos):
        filas,columnas=datos.shape
        masfrio=datos[0,0]
        x=0
        for i in range(0,filas):
                for j in range(0,columnas):
                        if datos[i,j]<masfrio:
                                masfrio=datos[i,j]
                                x=j+1
                                y=i
                                if y == 0:
                                        s="Girardot"
                                else:
                                        s="San Vicente de Chucuri"
        print ("El ",x," mes del año es el mas frio con una radiacion de: ",masfrio," en el municipio de:",s)
        return masfrio
masfrio(datos)
print ("Situacion problema 3:Promedio de radiacion en cada municipio")
def promedio(datos):
        columnas=datos.size/2
        suma1=np.sum(datos[0:1])
        suma2=np.sum(datos[1:])
        promedio1=suma1/columnas
        promedio2=suma2/columnas
        print("El promedio de radiacion en Girardot es de:",promedio1,"\ny el promedio de radiaion en San Vicente de Chucuri es de:",promedio2)
        return promedio
promedio(datos)