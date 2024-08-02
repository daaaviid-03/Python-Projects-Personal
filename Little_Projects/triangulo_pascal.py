from math import factorial as fact

def f(x, n):
    y = 1
    for i in range(x): y *= n + i
    return y

v = lambda fila, pos: f(pos+1, fila-pos) // fact(fila-pos)

def siguienteFila(f):
    f2 = [1]
    for i in range(len(f)-1):
        f2 += [f[i] + f[i+1]]
    f2 += [1]
    return f2

def triangulo(n):
    f = [1]
    print(f)
    for i in range(n):
        f = siguienteFila(f)
        print(f)
