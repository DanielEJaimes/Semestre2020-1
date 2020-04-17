arreglo=[27834,23789,30189,30967,32501,32701,31665,17155,4614,834]
def promedio (arreglo)
    long=arreglo.length
    media1=(arreglo[0]+arreglo[1])/2
    media2=(arreglo[long-1]+arreglo[long-2])/2
    promedio=media1-media2
    puts "La mediana de la utilidad es: #{promedio}"
end
promedio(arreglo)
def diferencia (arreglo)
    minarreglo=arreglo.min
    maxarreglo=arreglo.max
    diferencia=maxarreglo-minarreglo
    puts "La diferencia entre las utilidades fue: #{diferencia}"
end
diferencia(arreglo)
def mediana(arreglo)
    arreglo=arreglo.sort
    long=arreglo.length
    num=long/2
    mediana=(arreglo[num]+arreglo[num-1])/2
    puts "La mediana de la utilidad es: #{mediana}"
end
mediana(arreglo)
def porcentaje (arreglo)
    x=0
    long=arreglo.length
    cont=2008
    a=arreglo.sum
    while x<long
        porciento=((arreglo[x]*100)/a)
        x=x+1
        cont=cont+1
        puts "El porcentaje en el año #{cont} fue de #{porciento}%"
    end
end
porcentaje(arreglo)
deficit=arreglo[-1]-arreglo[-2]
puts "El deficit en la utilidad del año 2017 con respecto al año 2016 es de: #{deficit}"