import random
while(True):
    nPuertas = int(input("Introduce el número de puertas:    "))
    ent = int(input("Elige la puerta:    "))
    cambio = input("Cambio de variable? y/n:    ")
    if cambio == 'y':
        fin = input("En cada turno (y) o solo al final (n):    ")
    veces = int(input("Número de veces:    "))
    tot = 0
    
    for i in range(veces):
        puertas = []
        for j in range(nPuertas):
            puertas.append(int(j+1))
        puertasDef = puertas[:]
        
        ran = random.randint(1,nPuertas)

        '''
        puertas.remove(ent)
        if ran in puertas:
            puertas.remove(ran)
        '''
        if cambio == 'y':
            if fin == 'y':
                for j in range(nPuertas - 2):
                    puertas = puertasDef[:]
                    puertasCas = puertas[:]
                    puertasCas.remove(ent)
                    if ran in puertasCas:
                        puertasCas.remove(ran)
                    puertas.remove(random.choice(puertasCas))
                    puertaDef = puertas[:]
                    puertasCas = puertas[:]
                    puertasCas.remove(ent)
                    ent = random.choice(puertasCas)
            else:
                puertas.remove(ent)
                if ent != ran:
                    puertas.remove(ran)
                for j in range(nPuertas - 2):
                    puertas.remove(random.choice(puertas))
                if puertas != []:
                    ent = puertas[0]
                else:
                    ent = ran
        if ent == ran:
            tot += 1
    print("\nPuntuación: " + str(tot/veces), end = '\n\n')
            
        
