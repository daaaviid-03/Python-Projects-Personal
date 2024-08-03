# Documentación de librerías básicas

## SymPy

### Instalación
\>\>\> `pip install sympy`

### Ejemplos de uso
> import sympy as sp
>
> \# Definir los símbolos y la función compleja
> x, y = sp.symbols('x y')
> f = x\*\*2 + 2\*x\*y + y\*\*2 - 1
> 
> \# Resolver la ecuación f = 0 para obtener la expresión analítica
> sol = sp.solve(f, y)

# Imprimir la expresión analítica
print(sol)




## New Python

### Instalar una librería

\>\>\> `pip install [librería]`

### Actualizar todas las librerías

\>\>\> `pip-review --local --interactive`

### Librerías principales para instalación

\>\>\> `pip install selenium numpy tensorflow gtts SpeechRecognition playsound pandas matplotlib sympy pyautogui networkx graphviz Pillow pywhatkit pip-review`
\>\>\> `pip-review --local --interactive`



