import numpy as np

def generador (min,max):
    a=np.random.randint(min,max,size=48).reshape(4,12)
    return a
generador(2,20)