from turtle import *

def subPaso(pos1,pos2):
    up()
    goto(pos1[0],pos1[1])
    down()
    try:
        circle(pos2)
    except:
        goto(pos2[0],pos2[1])
pos = [[-300,200],20,[-300,200],[-300,150],[-300,150],[-310,110],
       [-300,150],[-290,110],[-280, 175],[-320, 175]]
ini = [[-300,240],[-300,300],-400,300,-400,0,-450,0,-350,0]
def colorear(paso):
    if paso == 0:
        pensize(5)
        subPaso(ini[0],ini[1])
        for i in range(4):
            goto(ini[2+2*i],ini[3+2*i])
    elif paso < 6:
        subPaso(pos[(paso-1)*2],pos[(paso-1)*2+1])
    else:
        color('red')
        for i in range(6):
            colorear(i)
