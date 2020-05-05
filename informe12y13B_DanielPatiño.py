import random


ponderado={"A":[1,11],"2":[2],"3":[3],"4":[4],"5":[5],"6":[6],"7":[7],"8":[8],"9":[9],"J":[10],"Q":[10],"K":[10]}


simbolos=["♥","♦","♣","♠"]


def combinador (a,b):
    baraja={}
    elementos=a.items()
    for h in b:
        for i,j in elementos:
            baraja[str(i)+str(h)]=j
    return baraja


baraja=combinador(ponderado,simbolos)

def revolver (a):
    x=0
    elementos=a.keys()
    lista_random=[]
    baraja={}
    for key in elementos:
        lista_random.append(key)
    while x < len(elementos):
        clave=random.choice(lista_random)
        lista_random.remove(clave)
        baraja[str(clave)]=a[clave]
        x=x+1
    return baraja


cartas_jugador=[]
cartas_tallador=[]


def claves_cartas (a):
    carta=a.keys()
    cartas=[]
    for key in carta:
        cartas.append(key)
    return cartas


indices=claves_cartas(baraja)


def repartir_base(a,b,c):
    cartas=a
    cartas_jugador=b
    baraja=c
    suma = 0
    carta_random=random.choice(cartas)
    cartas_jugador.append(carta_random)
    cartas.remove(carta_random)
    valor_carta=c[carta_random][-1]
    suma = suma + valor_carta
    del baraja[carta_random]
    return suma,baraja,cartas_jugador


victorias_tallador=0
victorias_jugador=0


empezar=input("Quiere jugar 21?\n")
if empezar == "Si":
    condicion = True
else: 
    condicion = False


while empezar=="Si":
    while condicion==True:
        valor=0
        baraja=combinador(ponderado,simbolos)
        cartas_jugador=[]
        for i in range(0,2):
            suma,baraja,carta_j=repartir_base(indices,cartas_jugador,baraja)
            i=i+1
            valor=suma+valor
            if valor == 21:
                print ("BlackJack")
                break
        print (carta_j,"\n",valor)
        otra=str(input("Quiere otra carta?\n"))
        while otra=="Si":
            suma,baraja,carta_j=repartir_base(indices,cartas_jugador,baraja)
            valor=suma+valor
            print (carta_j,"\n",valor)
            if valor == 21:
                print ("!21¡")
                otra="No"
            else:
                if valor > 21:
                    print ("Voló")
                    otra="No"
                    victorias_tallador+=1
                    victorias_jugador-=1
                    condicion=False
                    break
                else:
                    otra=str(input("Quiere otra carta?"))
        else:
            print("Planta")
            condicion=False
    cond_t=True
    while cond_t==True:
        valor_j=0
        cartas_tallador=[]
        while valor_j < valor :
            suma_t,baraja,carta_t=repartir_base(indices,cartas_tallador,baraja)
            valor_j=suma_t+valor_j
            if valor_j == 21:
                print (cartas_tallador)
                break
            if valor_j > 21:
                print (cartas_tallador,valor_j)
                valor_j=0
                print ("Voló")
                break
            cond_t=False
            print (cartas_tallador)
    if valor_j >= valor:
        victorias_tallador+=1
    else:
        victorias_jugador+=1
    condicion=True
    empezar=str(input("Quiere jugar otra vez?"))


print ("Victorias tallador:",victorias_tallador)
print ("Victorias jugador:",victorias_jugador)

