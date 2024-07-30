import sympy as sp

# Definir los símbolos y la función compleja
x, y = sp.symbols('x y')
f = x**2 + 2*x*y + y**2 - 1

# Resolver la ecuación f = 0 para obtener la expresión analítica
sol = sp.solve(f, y)

# Imprimir la expresión analítica
print(sol)
