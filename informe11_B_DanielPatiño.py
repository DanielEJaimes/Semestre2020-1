import random
import numpy as np
def generador (min,max):
    datos=np.random.randint(min,max,size=18).reshape(3,6)
    return datos


Bárbaro=generador(10,18)
Bardo=generador(10,18)
Clérigo=generador(10,18)
Druida=generador(10,18)
Guerrero=generador(10,18)
Mago=generador(10,18)
Paladín=generador(10,18)
Pícaro=generador(10,18)


clases=np.array([Bárbaro,Bardo,Clérigo,Druida,Guerrero,Mago,Paladín,Pícaro],dtype=int)
clases2=np.array([Bárbaro,Bardo,Clérigo,Druida,Guerrero,Mago,Paladín,Pícaro],dtype=int)
tipo_clase=np.array(["Bárbaro","Bardo","Clérigo","Druida","Guerrero","Mago","Paladín","Pícaro"])


num_jugadores=int(input("Ingrese el numero de jugadores: "))
for i in range (0,num_jugadores):
    nombre=str(input("Ingrese su username: "))
    clase=random.choice(clases)
    for j in range (0,8):
        if (clase==clases2[j]).all():
            personaje=tipo_clase[j]
        carac_per=random.choice(clase)
        carac_per=np.sort(carac_per)
        if (clase==clases[0]).all() or (clase==clases[4]).all() or (clase==clases[6]).all() or (clase==clases[7]).all():
            carac_per=np.flip(carac_per)
    print (nombre," su personaje es ",personaje," y sus caracteristicas son:\nFuerza:",carac_per[0],"\nDestreza:",carac_per[1],"\nConstitución:",carac_per[2],"\nInteligencia",carac_per[3],"\nSabiduría:",carac_per[4],"\nCarisma",carac_per[5])