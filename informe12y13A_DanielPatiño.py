import random


cartas=["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"] 


premium = ["AIVLI" , "LEIRBAG" , "NAILUJ" , "SOLRAC" , "ANAID"]


abecedario=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


cartas_total=(cartas+premium)


def imprimir (lista):
    print (lista)
    print (len(lista))


def generador (a,n):
    r=[]
    cont=0
    while cont < n:
        cont=cont+1
        eleccion=random.choice(a)
        if eleccion not in r:
            r.append(eleccion)
    return r


jugador=generador(cartas,10)


def combinador (a,b):
    r=(a+b)
    random.shuffle(r)
    return r


juego=combinador(cartas,premium)


sobre_uno=generador(juego,5)
sobre_dos=generador(juego,5)
sobre_tres=generador(juego,5)


paquete=combinador(sobre_uno,sobre_dos)
paquete=combinador(paquete,sobre_tres)


def loteria (a):
    cont=0
    randomizador=[]
    premium_conseguidas=[]
    for i in range (0,len(a)):
        for j in range (0,len(premium)):
            if a[i]==premium[j]:
                cont=cont+1
                premium_conseguidas.append(a[i])
            if cont > 1:
                condicion1=False
            else:
                condicion1=True
        repetidas=a.count(a[i])
        if repetidas > 1:
            prueba_condicion2=repetidas
            if prueba_condicion2 >= 2:
                condicion2=True
            else:
                condicion2=False
    if condicion1 and condicion2 == True:
        premium.remove(premium_conseguidas[0])
        for i in range(0,10):
            randomizador.append(i)
        aleatorio=random.choice(randomizador)
        if aleatorio==7:
            carta_obtenida=random.choice(premium)
            premium_conseguidas.append(carta_obtenida)
            return premium_conseguidas
    else:
        return None


#10.1
def cant_premium(a):
    cont=0
    cartas_premium=[]
    for i in range (0,len(a)):
        for j in range (0,len(premium)):
            if a[i]==premium[j]:
                cont = cont+1
                cartas_premium.append(a[i])
    return cartas_premium
cartas_premium_obtenidas=cant_premium(paquete)
print ("Cartas premium:",cartas_premium_obtenidas)


#10.2
def cant_repetidas(a):
    cont=0
    for i in range (0,len(a)):
        repes=a.count(a[i])
        if repes >= 2:
            cont=cont+1
    return cont/2
cartas_repetidas=cant_repetidas(paquete)
print ("Cantidad de cartas repetidas:",cartas_repetidas)


#10.3
def cant_cartas(a):
    cartas_usadas=[]
    for i in range(0,len(a)):
        if a[i] not in cartas_usadas:
            print ("Carta:",a[i],"\nCantidad de veces que aparece:",a.count(a[i]),)
            cartas_usadas.append(a[i])
cant_cartas(paquete)


#10.4
def letras_nombres (a):
    cont=0
    for i in range(0,len(abecedario)):
        for j in range (0,len(a)):
            if a[j][0]==abecedario[i]:
                cont=cont+1
        print (cont," comienzan con la letra ",abecedario[i])
        cont=0
letras_nombres(paquete)


#10.5
def nombre_largo_corto(a):
    nombre_largo=a[0]
    nombre_corto=a[0]
    for i in range (0,len(a)):
        if len(nombre_largo) <= len(a[i]):
            nombre_largo=a[i]
        if len(nombre_corto) > len(a[i]):
            nombre_corto=a[i]
    print ("La carta con el nombre mas largo es: ",nombre_largo)
    print ("La carta con el nombre mas corto es: ",nombre_corto)
nombre_largo_corto(paquete)


#10.6
def letras_premium (a):
    cont=0
    cartas_premium=[]
    for i in range (0,len(a)):
        if a[i] in premium:
            premium_minuscula=a[i].lower()
            cartas_premium.append(premium_minuscula)
    for h in range (0,len(a)):
        for j in range (0,len(cartas_premium)):
            if a[h][-1] == cartas_premium[j][0]:
                print ("La carta ",a[h],"cumple la condicion de acabar con la letra que empieza una carta premium")
                cont=cont+1
    if len(cartas_premium)==0:
        print ("No tiene cartas premium")
letras_premium(paquete)