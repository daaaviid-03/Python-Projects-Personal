import numpy as np
import random
from turtle import *

longitud = int(input("Longitud:   "))
veces = int(input("veces:   "))
mesa = np.ones((longitud,longitud))
for i in range(longitud):
    for j in range(longitud):
        if i == 0 or i == longitud - 1 or j == 0 or j == longitud - 1:
            mesa[i,j] = 2
posxi = random.randint(1,longitud - 2)
posyi = random.randint(1,longitud - 2)
posx = posxi
posy = posyi
mesa[posx,posy] = 0
val = np.array([[0,1],[1,0],[0,-1],[-1,0]])
for i in range(veces):
    mov = random.randint(0,3)
    lon = random.randint(1,int(longitud / 3))
    for j in range(lon):
        if mesa[posx + val[mov,0],posy + val[mov,1]] != 2:
            mesa[posx + val[mov,0],posy + val[mov,1]] = 0
            posx += val[mov,0]
            posy += val[mov,1]
    if mesa[posx + val[mov,0],posy + val[mov,1]] == 0:
        while mesa[posx + val[mov,0],posy + val[mov,1]] == 0:
            posx += val[mov,0]
            posy += val[mov,1]
    mesa[posx + val[mov,0],posy + val[mov,1]] = 2
up()
delay(0)
t = longitud/2
for i in range(longitud):
    for j in range(longitud):
        goto((j - t)*10, (-i + t)*10)
        if mesa[i,j] == 2 or mesa[i,j] == 1:
            dot(5,"red")
        else:
            dot(10, "blue")           
goto((posyi - t)*10,(-posxi + t)*10)
dot(10, "green")
input()





























