from unidecode import unidecode
from tkinter import *

def probarLetra(posibles,letras):
    conjunto = ''.join([i for i in posibles])
    setCon = list(set(conjunto))
    optimo = [sum(1 for i in posibles if j in i) for j in setCon if j not in letras]
    letraNueva = setCon[optimo.index(max(optimo))]
    while letraNueva in letras:
        no = optimo.index(max(optimo))
        setCon = setCon[:no]+setCon[no+1:]
        letraNueva = setCon[optimo.index(max(optimo))]
    letras.append(letraNueva)
    return letraNueva

def cambiarSugerencia(text):
    texto = StringVar()
    texto.set(text)
    errorText.config(textvariable = texto)

idioma = input('Introduce el idioma (es) o (en):  ')
ent = int(input('Numero de letras:  '))
name = 'Diccionario_'+('Espanol'if idioma=='es'else'Ingles')+'.txt'
words = list(set(open(name, encoding = 'utf-8').readlines()))
numeroPalabras = 'muchas'
def pista(pos,pista,mala = False):
    newPos = []
    if mala:
        newPos = [i for i in pos if pista not in i]
    else:
        newPos = [i for i in pos if sum(1 for j in range(ent) if (pista[j] != '-' and i[j] != pista[j]) or (pista[j] == '-' and i[j] in pista)) == 0]
    return newPos

def resolver():
    letras = []
    posibles = [unidecode(i)[:-1] for i in words if len(unidecode(i)[:-1]) == ent]
    #actual = ''.join([str(globals()['Entrada_'+str(i)].get()) for i in range(ent)]).replace(' ','-')
    actual2 = [str(globals()['Entrada_'+str(i)].get()) for i in range(ent)]
    actual = ''.join(i if i != '' else '-' for i in actual2)
    fallos = entrada_Fallos.get('1.0',END).split()
    posibles = pista(posibles,actual)
    for i in fallos:
        posibles = pista(posibles,i,True)
        letras.append(i)
    for i in actual:
        if i != '-':
            letras.append(i)
    letras = list(set(letras))
    conteoPalabras = ''
    if len(posibles) == 1:
        for i in range(ent):
            globals()['Entrada_'+str(i)].delete(0, END)
            globals()['Entrada_'+str(i)].insert(0, posibles[0][i])
        cambiarSugerencia('COMPLETO')
        conteoPalabras = 'Hay una palabra posible!!!'
    elif len(posibles) == 0:
        cambiarSugerencia('No existe la palabra introducida.\nRevisa los datos metidos.')
        conteoPalabras = 'No hay ninguna palabra posible :('
    else:
        cambiarSugerencia("Sugerencia: '" + probarLetra(posibles,letras) + "'")
        conteoPalabras = 'Hay ' + str(len(posibles)) + ' palabras posibles.'
    texto = StringVar()
    texto.set(conteoPalabras)
    posiText.config(textvariable = texto)
def borrar():
    for i in range(ent):
        globals()['Entrada_'+str(i)].delete(0, END)
    entrada_Fallos.delete('1.0',END)
    cambiarSugerencia("Sugerencia: ")

win = Tk()
win.title("Hang-Man")
titulo = Label(win, text = "HANG-MAN", font = ("arial", 30, "bold"))
titulo.grid(row = 0, column = 1, columnspan=ent,pady=10)
titulo2 = Label(win, text = "Introduce los datos que tengas:", font = ("arial", 20, "bold"))
titulo2.grid(row = 1, column = 1, columnspan=ent,pady=10)

for i in range(ent):
    globals()['Entrada_'+str(i)] = Entry(win, width = 3)
    globals()['Entrada_'+str(i)].grid(row = 2, column = 1+i)
    barra = Label(win, text = '—')
    barra.grid(row = 3, column = 1+i)

space = Label(win, text = ' '*20)
space.grid(row = 0, column = 1+ent)

titulo3 = Label(win, text = "Letras que no aparecen:", font = ("arial", 20, "bold"))
titulo3.grid(row = 1, column = 3+ent,pady=10)

entrada_Fallos = Text(win, width = 40, height = 4)
entrada_Fallos.grid(row = 2, rowspan = 4, column = 3+ent)
    
space = Label(win, text = ' '*30)
space.grid(row = 0, column = 0)

errorText = Label(win, text = "Sugerencia: ", fg = '#08B800')
errorText.grid(row = 4, column = 1,columnspan = ent)

posiText = Label(win, text = 'Hay ' + numeroPalabras + ' palabras posibles', fg = '#0797C2')
posiText.grid(row = 5, column = 1,columnspan = ent)

sendBut = Button(win,text="CALCULAR",command=resolver, bg = '#FF90FC')
sendBut.grid(row=6,column = 1, columnspan = ent//2, pady = 10)
sendBut = Button(win,text="BORRAR",command=borrar, bg = '#FF6969')
sendBut.grid(row=6,column = ent//2+1, columnspan = ent//2, pady = 10)

#sendBut = Button(win,text="CREAR",command=crear, bg = '#8CFF89')
#sendBut.grid(row=15,column = 1, columnspan = 5, pady = 10)

marcaAgua = Label(win, text = "Software creado por: David Pimentel Montes\nEnpresa: DPM Games", font = ("arial", 7))
marcaAgua.grid(row = 7, column = 3+ent, columnspan = 2,sticky = E+S)

space = Label(win, text = ' '*30)
space.grid(row = 0, column = 4+ent)

win.mainloop()
