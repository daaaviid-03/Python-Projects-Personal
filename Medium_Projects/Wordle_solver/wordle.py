'''
á => @
é => _
í => -
ó => :
ú => ;

'''

import random, unidecode
n, cont = int(input('Número de letras:   ')), 0
w = list(set(unidecode.unidecode(i)[:-1]for i in open(input('Introduce el nombre del diccionario:   ')+'.txt','r',encoding='utf-8').readlines() if len(unidecode.unidecode(i))-1==n))
w2 = [i for i in w if len(set(i)) == 5]
print('\nEl código de colores es:  (0: gris; 1: amarillo; 2: verde)\n')
while len(w)>1:
    print(f'Hay {len(w)} palabras que encajan.\nAlguna palabra aleatoria que puede ser: ' + ', '.join(random.choices(w if cont > 1 else w2,k=5) if len(w) > 12 else w) + '.\n')
    p, v, cont = [i for i in input('introduce la palabra:    ')], [int(i) for i in input('Introduce los colores:   ')], cont + 1
    a, b, c = [[p[i], i] for i in range(n) if v[i] == 2], [[p[i], i] for i in range(n) if v[i] == 1], [p[i] for i in range(n) if v[i] == 0 and len(set(v[j] for j in range(n) if p[j] == p[i])) == 1]
    w, w2 = [i for i in w if sum(1 for j in a if i[j[1]] == j[0]) == len(a) and sum(1 for j in b if j[0] in i and i[j[1]] != j[0]) == len(b) and sum(1 for j in c if j not in i) == len(c)], [i for i in w2 if sum(1 for j in p if j not in i) == len(p)]
input(f'La palabra correcta es ({w[0]}).  :) ...')

















    


