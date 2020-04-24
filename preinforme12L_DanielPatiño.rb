presiones=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]
presiones2=presiones.sort


def mayor_menor (presiones)
    minpresiones=presiones.min
    maxpresiones=presiones.max
    diferencia=maxpresiones-minpresiones
    puts "La diferencia entre las utilidades fue: #{diferencia}"
end
mayor_menor(presiones)


def media (presiones)
    long=presiones.length
    suma_presiones=presiones.sum
    media_presiones=(suma_presiones)/(long)
    return media_presiones
end

puts "La media de las presiones: #{media(presiones)}"


def mediana (presiones2)
    long=presiones2.length
    mediana_presiones=presiones2[long/2]+presiones2[(long/2)-1]
    mediana_presiones=mediana_presiones/2
    puts "La mediana de las presiones es: #{mediana_presiones}"
end
mediana(presiones2)


def presiones_mayores (presiones)
    presionesMay=[]
    media_presiones=media(presiones)
    media_presiones=gets.to_f
    for i in(0..52)
        if media_presiones < presiones[i]
            presionesMay.push(presiones[i])
        end
    end
    puts "Las presiones mayores son: #{presionesMay}"
end
presiones_mayores (presiones)


