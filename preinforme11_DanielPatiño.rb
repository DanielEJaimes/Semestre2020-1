arreglo=[[4.1315,4.3063,4.1961,4.3517,4.2235,4.3772,4.6318,4.6639,4.7422,4.2718,3.9881,4.3419],[3.366,3.5257,3.0164,2.9384,3.1146,3.4187,3.5895,3.6293,3.6523,3.1703,2.8728,2.8134]]
puts "Situacion problema 1:Mes mas calido del año entre ambos municipios"
def hot(arreglo)
    caliente=arreglo[0][0]
    for i in(0..arreglo.size-1)
        for j in(0..arreglo[i].size-1)
            if caliente<arreglo[i][j]
                caliente=arreglo[i][j]
                x=j+1
                y=i
                if y == 0
                    s="Girardot"
                else
                    s="San Vicente de Chucuri"
                end
            end
        end
    end
    puts "El #{x} mes del año es el mas caliente con una radiacion de: #{caliente} en el municipio de:#{s}"
end
hot(arreglo)
puts "Situacion problema 2:Mes mas frio del año entre ambos municipios"
def frio(arreglo)
    frio=arreglo[0][0]
    for i in(0..arreglo.size-1)
        for j in(0..arreglo[i].size-1)
            if frio>arreglo[i][j]
                frio=arreglo[i][j]
                x=j+1
                y=i
                if y == 0
                    s="Girardot"
                else
                    s="San Vicente de Chucuri"
                end
            end
        end
    end
    puts "El #{x} mes del año es el mas frio con una radiacion de: #{frio} en el municipio de:#{s}"
end
frio(arreglo)
puts "Situacion problema 3:Promedio de radiacion en cada municipio"
def promedio(arreglo)
    columnas=arreglo[0].size
    suma1=arreglo[0].sum
    suma2=arreglo[1].sum
    promedio1=suma1/columnas
    promedio2=suma2/columnas
    puts "El promedio de radiacion en Girardot es de:#{promedio1} y el promedio de radiaion en San Vicente de Chucuri es de:#{promedio2}"
end
promedio(arreglo)