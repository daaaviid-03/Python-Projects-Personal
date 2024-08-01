import random
import time
def barra():
    print("|",end = "")
    for i in range(98):
        print("-", end = "")
    print("|")
while True:
    dineroIni = float(input("Cuanto dinero ingresas?    "))
    apuestaIni = float(input("Cuanto apuestas?    "))
    multPerder = float(input("Por cuanto se multiplica tu apuesta al perder?    "))
    dineroFin = float(input("Con cuanto dinero te marchas?    "))
    posibilidades  = float(input("Cuantas posibilidades de victoria?    "))
    beneficio = float(input("Por cuanto se multiplica la apuesta por victoria?    "))
    intentos = int(input("Cuantas simulaciones?    "))
    win, lose = 0, 0
    percent = intentos // 55
    tiempoIni = 0
    vueltas = 0
    for i in range(intentos):
        if i % percent == 0:
            vueltas += 1
            if vueltas == 1:
                tiempoIni = time.time()
            elif vueltas == 2:
                print("Va a tardar " + str(round(55 * (time.time() - tiempoIni), 1) + 0.5) + " segundos en hacer el cálculo.")
                print("|-------------La barra de carga ocupa esto------------|")
                print("..", end = "")
            else:
                print(".", end = "")
        dinero = dineroIni
        apuesta = apuestaIni
        while True:
            if random.random() < posibilidades:
                dinero += apuesta * (beneficio - 1)
                apuesta = apuestaIni
                if dinero >= dineroFin:
                    win += 1
                    break
            else:
                dinero -= apuesta
                if dinero > apuesta * multPerder:
                    if apuesta * multPerder >= 1:
                        apuesta *= multPerder
                    else:
                        apuesta = 1
                elif dinero > 0:
                    apuesta = dinero
                else:
                    lose += 1
                    break
    print("\n\nHas ganado: " + str(win) + " veces")
    print("Has perdido: " + str(lose) + " veces\n")
    print("La probabilidad de consegirlo es del " + str(float(win)/float(intentos) * 100) + "%\n")
