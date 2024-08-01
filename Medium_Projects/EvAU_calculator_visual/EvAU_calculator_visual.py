from tkinter import *

def comprobar():
    data = open("EvAUData.txt", "r")
    documento = []
    for line in data:
        documento.append(str(float(line)))
    for i in range(len(documento) - 1, 30):
        documento.append('0')
    vueltas = 0
    for i in range(len(asign)):
        for j in range(len(asign[i])):
            globals()["AsEnt" + str(i) + str(j)].delete(0, END)
            globals()["AsEnt" + str(i) + str(j)].insert(0, documento[vueltas])
            vueltas += 1
    for i in range(4):
        globals()["AsEntPon" + str(i)].delete(0, END)
        globals()["AsEntPon" + str(i)].insert(0, documento[vueltas])
        vueltas += 1
    trabajoEnt.delete(0, END)
    trabajoEnt.insert(0, documento[vueltas])
    data.close()
#----------------------------------------------------------------------------------------
def saveData():
    data = open("EvAUData.txt", "w")
    data.write("")
    for i in range(len(asign)):
        for j in range(len(asign[i])):
            if globals()["AsEnt" + str(i) + str(j)].get() != '':
                data.write(globals()["AsEnt" + str(i) + str(j)].get() + "\n")
            else:
                data.write("0\n") 
    for i in range(4):
        if globals()["AsEntPon" + str(i)].get() != '':
            data.write(globals()["AsEntPon" + str(i)].get() + "\n")
        else:
            data.write("0\n")
    data.write(trabajoEnt.get())
    data.close()
#----------------------------------------------------------------------------------------
def calcular():
    notas1, notas2, obli, espec, tot, medB, medO, m = [], [], [], [], 0.0, 0.0, 0.0, []
    
    if trabajoEnt.get() == '':
        trabajoEnt.insert ( 0, '0' )

    for i in range(len(asign)):
        for j in range(len(asign[i])):
            if globals()["AsEnt" + str(i) + str(j)].get() =='':
                globals()["AsEnt" + str(i) + str(j)].insert (0,'0' )
    for i in range(4):
        if globals()["AsEntPon" + str(i)].get() =='':
                globals()["AsEntPon" + str(i)].insert (0,'0' )

    for i in range(9):
        notas1.append(globals()["AsEnt0" + str(i)].get())
    for i in range(8):
        notas2.append(globals()["AsEnt1" + str(i)].get())
    for i in range(4):
        obli.append(globals()["AsEnt2" + str(i)].get())
    for i in range(4):
        espec.append(float(globals()["AsEnt3" + str(i)].get()))
        espec.append(float(globals()["AsEntPon" + str(i)].get()))
        
    trabajoSN = float(trabajoEnt.get())
    
    for i in notas1:
        medB += float(i)

    media1Ent.delete(0,END)
    media1Ent.insert(0,str(round(medB / 9,2)))
    medB1 = 0
    for i in notas2:
        if trabajoSN >= 6 and float(i) <= 9:
            i = float(i) + trabajoSN**2/100
        medB1 += float(i)
    media2Ent.delete(0,END)
    media2Ent.insert(0,str(round(medB1 / 8,2)))
    medB += medB1
    medB = round(medB / 17, 3)
    tot += round(medB * 0.6, 3)
    texto1 = StringVar()
    texto1.set("Tu media en BACHILLERATO es de:  " + str(medB))
    mediaBach.config(textvariable = texto1)

    for i in obli:
        medO += float(i)
    medO = round(medO * 0.1 , 3)
    tot += medO
    texto2 = StringVar()
    texto2.set("Tu media en CAU es de:  " + str(round(tot, 3)))
    mediaCAU.config(textvariable = texto2)

    for i in range(int(len(espec) / 2)):
        m.append(str(round(float(espec[i * 2]) * float(espec[i * 2 + 1]), 3)))
    m = sorted(m,key=None, reverse=True)
    tot += float(m[0]) + float(m[1])
    
    texto3 = StringVar()
    texto3.set("Tu media TOTAL es de:  " + str(round(tot, 3)))
    mediaTot.config(textvariable = texto3)
    saveData()
#-----------------------------------------------------------------------------------------------------
win = Tk()
win.title("EvAU")

titulo = Label(win, text = "Esto es un software para calcular to nota final de EvAU atendiendo a la ponderación de cada parte del examen.\nIntroduce las notas en sus respectivas casillas y dale a CALCULAR")
titulo.grid(columnspan=20,pady=10)

headEx = Label(win, text = "BACHILLERATO:", font = ("arial", 12, "bold"))
headEx.grid(row = 1, column = 0, columnspan=4, pady = 20)

headEx = Label(win, text = "EXAMEN:", font = ("arial", 12, "bold"))
headEx.grid(row = 1, column = 4, columnspan=4, pady = 20)

bloques = ["1º Bachillerato","2º Bachillerato", "Bloque Obligatorio","Bloque Específico"]
for i in range(len(bloques)):
    if i == 3:
        c = 3
    else:
        c = 2
    globals()["Titul" + str(i)] = Label(win, text = bloques[i], font = ("arial", 10, "bold"))
    globals()["Titul" + str(i)].grid(row = 2, column = i*2, columnspan=c, pady = 20)
    
    globals()["Notas" + str(i)] = Label(win, text = "Nota:", font = ("arial", 7))
    globals()["Notas" + str(i)].grid(row = 3, column = 1 + 2*i)

asign = ["Lengua y Literatura", "Inglés", "Filosofía", "Matemáticas",
         "Educación Física", "Física y Química", "Dibujo Técnico", "TICO",
         "Cultura Científica"], ["Lengua y Literatura", "Inglés", "Filosofía", "Matemáticas", "Historia de España",
                                 "Física", "Dibujo Técnico", "TICO"], ["Lengua y Literatura",
                                                                       "Inglés", "Matemáticas","Historia de España"], ["Asignatura1",
                                                                                                                       "Asignatura2", "Asignatura3", "Asignatura4"]

for i in range(len(asign)):
    for j in range(len(asign[i])):
        globals()["AsTxt" + str(i) + str(j)] = Label(win, text = str("    " + asign[i][j] + ":    "))
        globals()["AsTxt" + str(i) + str(j)].grid(row = 4 + j, column = i*2, pady = 2)
        globals()["AsEnt" + str(i) + str(j)] = Entry(win, width = 4)
        globals()["AsEnt" + str(i) + str(j)].grid(row = 4 + j, column = i*2 + 1)
for i in range(4):
    globals()["AsEntPon" + str(i)] = Entry(win, width = 4)
    globals()["AsEntPon" + str(i)].grid(row = 4 + i, column = 8)

headEPon = Label(win, text = "Ponderación:", font = ("arial", 7))
headEPon.grid(row = 3, column = 8)
#----------------------------------------------------------------------
espacio1 = Label(win, text = "    ")
espacio1.grid(row = 13, column = 2)

headENot = Label(win, text = "Nota:", font = ("arial", 7))
headENot.grid(row = 14, column = 1)

media1 = Label(win, text = "MEDIA:    ")
media1.grid(row = 15, column = 0)
media1Ent = Entry(win, width = 4)
media1Ent.grid(row = 15, column = 1)
#----------------------------------------------------------------------
headENot = Label(win, text = "Nota:", font = ("arial", 7))
headENot.grid(row = 14, column = 3)

media2 = Label(win, text = "MEDIA:    ")
media2.grid(row = 15, column = 2)
media2Ent = Entry(win, width = 4)
media2Ent.grid(row = 15, column = 3)
#----------------------------------------------------------------------
espacio2 = Label(win, text = "    ")
espacio2.grid(row = 16, column = 2)

headENot = Label(win, text = "Nota:", font = ("arial", 7))
headENot.grid(row = 17, column = 2)

trabajoTxt = Label(win, text = "Trabajo de investigación:    ")
trabajoTxt.grid(row = 18, column = 0,columnspan=3)
trabajoEnt = Entry(win, width = 4)
trabajoEnt.grid(row = 18, column = 2)

espacio2 = Label(win, text = "    ")
espacio2.grid(row = 19, column = 2, columnspan=3, pady = 30)
#----------------------------------------------------------------------
espacio3 = Label(win, text = "                    ")
espacio3.grid(row = 1, column = 9)

calcularBut = Button(win,text="CALCULAR",command=calcular)
calcularBut.grid(row=1,column = 11)

mediaBach = Label(win, text = "Tu media en bachillerato es de:  --.---")
mediaBach.grid(row = 2, column = 11)

mediaCAU = Label(win, text = "Tu media en CAU es de:  --.---")
mediaCAU.grid(row = 3, column = 11)

mediaTot = Label(win, text = "Tu media TOTAL es de:  --.---", font = ("arial", 12, "bold"))
mediaTot.grid(row = 8, column = 11)
#----------------------------------------------------------------------
comprobar()
calcular()
#----------------------------------------------------------------------
marcaAgua = Label(win, text = "Software creado por: David Pimentel Montes\nEnpresa: DPM Company", font = ("arial", 7))
marcaAgua.grid(row = 100, column = 100)

win.mainloop()
