from tkinter import filedialog
from tkinter import*
from tkinter.filedialog import askopenfilename
from music21 import *


#*---------Variables----------*#
i = 1
composicion = [stream.Part(),stream.Part(),stream.Part(),stream.Part(),stream.Score()]
intervalos_validos = ["...", "P1","m2","M2","m3","M3",
                      "P4","P5","m6","M6","m7",
                      "M7","P8","-m2","-M2",
                      "-m3","-M3","-P4","-P5","-m6",
                      "-M6","-m7","-M7","-P8"]

notaPiano = None #Esta variable sirve para guardar de forma temporal una nota
intArp = None #Esta variable sirve para guardar de forma temporal un intervalo
variable = ""


#*-----------Ventana----------*#
window = Tk()
window.title("Compositor Musical")
window.resizable(0,0)
#window.iconbitmap("icono.ico")
window.geometry("500x300")


#*-----------Frames----------*#
frame1 = Frame()
frame1.config(bg="#999999")

newframe = Frame()
newframe.config(bg="#999999")

frameArp = Frame()
frameArp.config(bg="#999999")

frameTrans = Frame()
frameTrans.config(bg="#999999")

frameP = Frame()
frameP.config(bg="#999999")

frameBorrar = Frame()
frameBorrar.config(bg="#999999")

for frame in (frame1, newframe, frameArp, frameTrans, frameP, frameBorrar):
    frame.place(width="500", height="300")


#*---------------------- Funciones----------------------*#
def tinystr(direccion:str) -> str:
    """
    Esta función permite formatear string para quedarse con la ruta que interesa,
    la ruta a un archivo tinynotation.
    """
    i = 0
    p = False
    while i<=(len(direccion)-13) and p==False:
        p = (direccion[i:i+13:1] == ".tinynotation")
        i = i+1
    if p == True:
        return direccion[0:i+12:1]
    else:
        print("Esa dirección no es válida")

def OpenFile():
    """
    Esta es una implementación de una función in-built de Tkinter. Devuelve una 
    ruta de archivo
    """
    name = askopenfilename(initialdir="C:/", filetypes =(("Tinynotation File", "*.tinynotation"),("All Files","*.*")), title = "Choose a file.")
    return name

def cargar(ruta:str,parte:stream.Part) -> "void":
    """
    Este procedimiento carga un archivo en formato tinynotation y lo convierte en una
    parte.
    """
    #Precondición de la definición:
    #La ruta especificada lleva a un archivo
    posible = True #Posible indica si es posible o no efectuar la carga.

    try:
        assert(ruta[len(ruta)-13::1]==".tinynotation")
    except:
        print("La extensión del archivo especificado no es válida.")
        posible = False

    try:
        assert(posible)
        s = converter.parse(ruta)
        parte.append(s)
    except:
        print("La ruta especificada no es válida.")

def piano_window():
    """
    Un procedimiento para tkinter, sirve para invocar la ventana del piano
    """
    piano = Toplevel()

def show_frame(page_name):
    """
    Muestra una página de la ventana
    """
    page_name.tkraise()

def cambiar_parte(j:int):
    """
    Este procedimiento cambia el valor del índice i a j con 1<=j<=4
    """
    global i
    i = j

    global notaPiano
    notaPiano = None

def reproducir(parte:stream.Part)->"void":
    """
    Esta función reproduce una parte.
    """
    #Precondición de la definición:
    assert(True)
    parte.show("midi")
    #Postcondición de la definición:
    assert(True)

def reiniciar_parte() -> "void":
    """
    Este procedimiento reinicia la parte alojada en composición[i]
    """
    global i
    global composicion
    composicion[i] = stream.Part()

def reiniciar_cancion() -> "void":
    """
    Este procedimiento reinicia la canción alojada en composición[i]
    """
    global i
    global composicion
    composicion[4] = stream.Score()

def componer(partes:list) -> "void":
    """
    Esta función crea una canción al componer una lista de partes
    """
    global composicion
    composicion[4] = stream.Score()
    for i in partes:
        composicion[4].insert(0,i)

def comp_play(partes:list)-> "void":
    """
    Este procedimiento compone y reproduce una lista de notas.
    """
    global composicion
    componer(partes)
    reproducir(composicion[4])

def transponer(parte:stream.Part,intervalo:str) -> stream.Part:
    """
    Esta función devuelve la traspuesta de una parte.
    """
    #Precondición de la definición:
    #Programa
    try:
        #assert(existe(intervalo==i for i in intervalos_validos))
        p = parte.transpose(intervalo)
        composicion[i] = p
    except:
        print("El intervalo no es válido.")
    
    #Postcondición de la definición:
    #p es la traspuesta de parte

def crear_arpegio(nota:note.Note,intervalo:str):
    """
    Este procedimiento crea un arpegio de 8 notas partiendo de una nota y
    serparado por un intervalo "intervalo".
    """
    global composicion
    #Precondición de la definición:
    try:
        #assert(existe(k==intervalo for k in intervalos_validos))
        parte = stream.Part()
        for j in range(8):
            parte.append(nota)
            nota = nota.transpose(intervalo)
            composicion[i] = parte
    except:
        print("Ese intervalo no es válido.")

    #Postcondición de la definición:
    #parte es un arpegio de 8 notas separadas por "intervalo"
    

def arpegio2():
    """
    Este procedimiento es solo una concatenación de procedimientos. Sirve para 
    simplificar las llamadas de acciones de los botones de tkinter
    """
    global notaPiano
    global intArp
    global composicion
    global variable
    intArp = variable.get()
    crear_arpegio(notaPiano,intArp)
    intArp = None
    notaPiano = None

def piano_nota(nota: str):
    """
    Este procedimiento es para cambiar el valor notaPiano segun la entrada del piano
    """
    global notaPiano
    notaPiano = note.Note(nota)


#*----------------------Widgets----------------------*#
#*--------- Frame 1---------*#
image = PhotoImage(file="titulo.png")
label = Label(frame1, image=image)
label.place(width="500", height="300")

imgP1 = PhotoImage(file="button1.png")
botonParte1 = Button(frame1, cursor="hand2", image=imgP1, border=0, bg="#999999", command = lambda: [show_frame(newframe),cambiar_parte(0)])
botonParte1.grid(row=0, column=0)

imgP2 = PhotoImage(file="button2.png")
botonParte2 = Button(frame1, cursor="hand2", image=imgP2, border=0, bg="#999999", command = lambda: [show_frame(newframe),cambiar_parte(1)])
botonParte2.grid(row=1, column=0)

imgP3 = PhotoImage(file="button3.png")
botonParte3 = Button(frame1, cursor="hand2", image=imgP3, border=0, bg="#999999", command = lambda: [show_frame(newframe),cambiar_parte(2)])
botonParte3.grid(row=2, column=0)

imgP4 = PhotoImage(file="button4.png")
botonParte4 = Button(frame1, cursor="hand2", image=imgP4, border=0, bg="#999999", command = lambda: [show_frame(newframe),cambiar_parte(3)])
botonParte4.grid(row=3, column=0)

imgEsc = PhotoImage(file="playb.png")
botonEsc = Button(frame1, cursor="hand2", image=imgEsc, border=0, bg="#999999", command = lambda: comp_play(composicion[0:4:1]))
botonEsc.grid(row=4, column=0)

imgSalir = PhotoImage(file="exitb.png")
botonSalir = Button(frame1, cursor="hand2", image=imgSalir, border=0, bg="#999999", command = lambda: window.destroy())
botonSalir.grid(row=5, column=0)


#*--------- New Frame ---------*#
imgCargar = PhotoImage(file="button_cargar.png")
botonCargar = Button(newframe, cursor="hand2", image=imgCargar, border=0, bg="#999999", command= lambda: cargar(OpenFile(),composicion[i]))
botonCargar.grid(row=3, column=0, sticky=W+E+N+S)

imgArpegio = PhotoImage(file="button_arpegio.png")
botonArpegio = Button(newframe, width="121", height="35",cursor="hand2",
image=imgArpegio, border=0, bg="#999999", command = lambda: piano_window())
botonArpegio.grid( row=3, column=1, sticky=W+E+N+S)

imgTransportar = PhotoImage(file="button_transportar.png")
botonTransportar = Button(newframe, cursor="hand2",
image=imgTransportar, border=0, bg="#999999", command = lambda: show_frame(frameTrans))
botonTransportar.grid(row=6, column=0, sticky=W+E+N+S)

imgPlay = PhotoImage(file="button_escuchar.png")
botonPlay = Button(newframe, cursor="hand2", image=imgPlay,
border=0, bg="#999999", command = lambda:  reproducir(composicion[i]))
botonPlay.grid(row=6, column=1, sticky=W+E+N+S)

imgBorrar = PhotoImage(file="button_borrar.png")
botonBorrar = Button(newframe, cursor="hand2", image=imgBorrar,
border=0, bg="#999999", command = lambda: reiniciar_parte())
botonBorrar.grid(row=8, column=0)

imgRegresar = PhotoImage(file="button_regresar.png")
botonRegresar = Button(newframe, cursor="hand2", image=imgRegresar, border=0, bg="#999999", command= lambda: show_frame(frame1))
botonRegresar.grid(row=8, column=1)


#*--------- Frame Arpegio ---------*#
msgArp = Label(frameArp, text="Generar Arpegio", height=5, width=100)
msgArp.config(font=("Helvetica", 20), bg="#999999")
msgArp.pack()

backArp = PhotoImage(file="button_regresar.png")
botonBackArp = Button(frameArp, image=backArp, border=0, bg="#999999",
command = lambda: show_frame(newframe))
botonBackArp.pack()

#*--------- Frame Transponer ---------*#
msgTrans = Label(frameTrans, text="Elija el intervalo a transponer", height=5, width=100)
msgTrans.config(font=("Helvetica", 20), bg="#999999")
msgTrans.pack()

var = StringVar(frameTrans)
var.set("...") # default value
menu = OptionMenu(frameTrans, var,"...", "P1","m2","M2","m3","M3",
                      "P4","P5","m6","M6","m7",
                      "M7","P8","-m2","-M2",
                      "-m3","-M3","-P4","-P5","-m6",
                      "-M6","-m7","-M7","-P8")
menu.place(x = 225, y = 110)

botonTransportar = Button(frameTrans, cursor="hand2",
image=imgTransportar, border=0, bg="#999999", command = lambda: transponer(composicion[i], var.get()))
botonTransportar.pack()

backTrans = PhotoImage(file="button_regresar.png")
botonBackTrans = Button(frameTrans, image=backTrans, border=0, bg="#999999",
command = lambda: show_frame(newframe), cursor="hand2")
botonBackTrans.pack()

#*--------- Frame Play Part ---------*#
msgP = Label(frameP, text="Escuchar Parte", height=5, width=100)
msgP.config(font=("Helvetica", 20), bg="#999999")
msgP.pack()

backP = PhotoImage(file="button_regresar.png")
botonBackP = Button(frameP, image=backP, border=0, bg="#999999",
command = lambda: show_frame(newframe))
botonBackP.pack()

#*--------- Frame Borrar ---------*#
msgBorrar = Label(frameBorrar, text="Borrar Parte", height=5, width=100)
msgBorrar.config(font=("Helvetica", 20), bg="#999999")
msgBorrar.pack()

backBorrar = PhotoImage(file="button_regresar.png")
botonBackBorrar = Button(frameBorrar, image=backBorrar, border=0, bg="#999999",
command = lambda: show_frame(newframe))
botonBackBorrar.pack()


#*--------- Frame Piano ---------*#
def piano_window():
    """
    Procedimiento para llamar al piano.
    """
    piano = Tk()
    piano.title("Compositor Musical")
    piano.resizable(0,0)
    #piano.iconbitmap("icono.ico")
    piano.geometry("1110x600")


    #De aquí en adelante son los botones del piano ordenados de izquierda a derecha.
    botonC1 = Button(piano, text= "C1",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C1'))
    botonC1.place(x =20, y =150)

    botonD1 = Button(piano, text= "D1",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C1'))
    botonD1.place(x =58, y =150)

    botonE1 = Button(piano, text= "   E1",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E1'))
    botonE1.place(x = 96, y =150)

    botonF1 = Button(piano, text= "F1",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F1'))
    botonF1.place(x = 134, y =150)

    botonG1 = Button(piano, text= "G1",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G1'))
    botonG1.place(x = 172, y =150)

    botonA1 = Button(piano, text= "A1",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A1'))
    botonA1.place(x = 210, y =150)

    botonB1 = Button(piano, text= "  B1",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B1'))
    botonB1.place(x = 248, y =150)

    botonC2 = Button(piano, text= "C2",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C2'))
    botonC2.place(x =286, y =150)

    botonD2 = Button(piano, text= "D2",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('D2'))
    botonD2.place(x =324, y =150)

    botonE2 = Button(piano, text= "   E2",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E2'))
    botonE2.place(x = 362, y =150)

    botonF2 = Button(piano, text= "F2",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F2'))
    botonF2.place(x = 400, y =150)

    botonG2 = Button(piano, text= "G2",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G2'))
    botonG2.place(x = 438, y =150)

    botonA2 = Button(piano, text= "A2",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A2'))
    botonA2.place(x = 476, y =150)

    botonB2 = Button(piano, text= "   B2",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B2'))
    botonB2.place(x = 514, y =150)

    botonC3 = Button(piano, text= "C3",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C3'))
    botonC3.place(x =552, y =150)

    botonD3 = Button(piano, text= "D3",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('D3'))
    botonD3.place(x =590, y =150)

    botonE3 = Button(piano, text= "   E3",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E3'))
    botonE3.place(x = 628, y =150)

    botonF3 = Button(piano, text= "F3",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F3'))
    botonF3.place(x = 666, y =150)

    botonG3 = Button(piano, text= "G3",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G3'))
    botonG3.place(x = 704, y =150)

    botonA3 = Button(piano, text= "A3",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A3'))
    botonA3.place(x = 742, y =150)

    botonB3 = Button(piano, text= "   B3",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B3'))
    botonB3.place(x = 780, y =150)

    botonC4 = Button(piano, text= "C4",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C4'))
    botonC4.place(x = 818, y =150)

    botonD4 = Button(piano, text= "D4",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('D4'))
    botonD4.place(x =856, y =150)

    botonE4 = Button(piano, text= "   E4",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E4'))
    botonE4.place(x = 894, y =150)

    botonF4 = Button(piano, text= "F4",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F4'))
    botonF4.place(x = 932, y =150)

    botonG4 = Button(piano, text= "G4",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G4'))
    botonG4.place(x = 970, y =150)

    botonA4 = Button(piano, text= "A4",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A4'))
    botonA4.place(x = 1008, y =150)

    botonB4 = Button(piano, text= "   B4",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B4'))
    botonB4.place(x = 1046, y =150)



    #*-----------------------*#
    botonC5 = Button(piano, text= "C5",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C5'))
    botonC5.place(x =20, y =370)

    botonD5 = Button(piano, text= "D5",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('D5'))
    botonD5.place(x =58, y =370)

    botonE5 = Button(piano, text= "   E5",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E5'))
    botonE5.place(x = 96, y =370)

    botonF5 = Button(piano, text= "F5",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F5'))
    botonF5.place(x = 134, y =370)

    botonG5 = Button(piano, text= "G5",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G5'))
    botonG5.place(x = 172, y =370)

    botonA5 = Button(piano, text= "A5",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A5'))
    botonA5.place(x = 210, y =370)

    botonB5 = Button(piano, text= "   B5",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B5'))
    botonB5.place(x = 248, y =370)

    botonC6 = Button(piano, text= "C6",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C6'))
    botonC6.place(x =286, y =370)

    botonD6 = Button(piano, text= "D6",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('D6'))
    botonD6.place(x =324, y =370)

    botonE6 = Button(piano, text= "   E6",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E6'))
    botonE6.place(x = 362, y =370)

    botonF6 = Button(piano, text= "F6",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F6'))
    botonF6.place(x = 400, y =370)

    botonG6 = Button(piano, text= "G6",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G6'))
    botonG6.place(x = 438, y =370)

    botonA6 = Button(piano, text= "A6",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A6'))
    botonA6.place(x = 476, y =370)

    botonB6 = Button(piano, text= "   B6",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B6'))
    botonB6.place(x = 514, y =370)

    botonC7 = Button(piano, text= "C7",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C7'))
    botonC7.place(x =552, y =370)

    botonD7 = Button(piano, text= "D7",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('D7'))
    botonD7.place(x =590, y =370)

    botonE7 = Button(piano, text= "   E7",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E7'))
    botonE7.place(x = 628, y =370)

    botonF7 = Button(piano, text= "F7",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F7'))
    botonF7.place(x = 666, y =370)

    botonG7 = Button(piano, text= "G7",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G7'))
    botonG7.place(x = 704, y =370)

    botonA7 = Button(piano, text= "A7",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A7'))
    botonA7.place(x = 742, y =370)

    botonB7 = Button(piano, text= "   B7",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B7'))
    botonB7.place(x = 780, y =370)

    botonC8 = Button(piano, text= "C8",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('C8'))
    botonC8.place(x = 818, y =370)

    botonD8 = Button(piano, text= "D8",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('D8'))
    botonD8.place(x =856, y =370)

    botonE8 = Button(piano, text= "   E8",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('E8'))
    botonE8.place(x = 894, y =370)

    botonF8 = Button(piano, text= "F8",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('F8'))
    botonF8.place(x = 932, y =370)

    botonG8 = Button(piano, text= "G8",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('G8'))
    botonG8.place(x = 970, y =370)

    botonA8 = Button(piano, text= "A8",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('A8'))
    botonA8.place(x = 1008, y =370)

    botonB8 = Button(piano, text= "   B8",
    bg= 'white', fg = 'black', width = 4, height = 10, command = lambda: piano_nota('B8'))
    botonB8.place(x = 1046, y =370)

    #-----------------------------------#
    botonCb1 = Button(piano, text= "C#1",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#1'))
    botonCb1.place(x =46, y =150)

    botonDb = Button(piano, text= "D#1",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#1'))
    botonDb.place(x =84, y =150)

    botonFb = Button(piano, text= "F#1",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#1'))
    botonFb.place(x =160, y =150)

    botonGb = Button(piano, text= "G#1",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#1'))
    botonGb.place(x =198, y =150)

    botonAb = Button(piano, text= "A#1",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#1'))
    botonAb.place(x =236, y =150)


    botonCb2 = Button(piano, text= "C#2",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#2'))
    botonCb2.place(x =312, y =150)

    botonDb2 = Button(piano, text= "D#2",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#2'))
    botonDb2.place(x =350, y =150)

    botonFb2 = Button(piano, text= "F#2",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#2'))
    botonFb2.place(x =426, y =150)

    botonGb2 = Button(piano, text= "G#2",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#2'))
    botonGb2.place(x =464, y =150)

    botonAb2 = Button(piano, text= "A#2",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#2'))
    botonAb2.place(x =502, y =150)


    botonCb3 = Button(piano, text= "C#3",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#3'))
    botonCb3.place(x =578, y =150)

    botonDb3 = Button(piano, text= "D#3",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#3'))
    botonDb3.place(x =616, y =150)

    botonFb3 = Button(piano, text= "F#3",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#3'))
    botonFb3.place(x =692, y =150)

    botonGb3 = Button(piano, text= "G#3",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#3'))
    botonGb3.place(x =730, y =150)

    botonAb3 = Button(piano, text= "A#3",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#3'))
    botonAb3.place(x =768, y =150)


    botonCb4 = Button(piano, text= "C#4",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#4'))
    botonCb4.place(x =844, y =150)

    botonDb4 = Button(piano, text= "D#4",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#4'))
    botonDb4.place(x =882, y =150)

    botonFb4 = Button(piano, text= "F#4",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#4'))
    botonFb4.place(x =958, y =150)

    botonGb4 = Button(piano, text= "G#4",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#4'))
    botonGb4.place(x =996, y =150)

    botonAb4 = Button(piano, text= "A#4",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#4'))
    botonAb4.place(x =1034, y =150)

    #------------------------------------#
    botonCb5 = Button(piano, text= "C#5",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#5'))
    botonCb5.place(x =46, y =370)

    botonDb5 = Button(piano, text= "D#5",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#5'))
    botonDb5.place(x =84, y =370)

    botonFb5 = Button(piano, text= "F#5",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#5'))
    botonFb5.place(x =160, y =370)

    botonGb5 = Button(piano, text= "G#5",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#5'))
    botonGb5.place(x =198, y =370)

    botonAb5 = Button(piano, text= "A#5",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#5'))
    botonAb5.place(x =236, y =370)


    botonCb6 = Button(piano, text= "C#6",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#6'))
    botonCb6.place(x =312, y =370)

    botonDb6 = Button(piano, text= "D#6",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#6'))
    botonDb6.place(x =350, y =370)

    botonFb6 = Button(piano, text= "F#6",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#6'))
    botonFb6.place(x =426, y =370)

    botonGb6 = Button(piano, text= "G#6",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#6'))
    botonGb6.place(x =464, y =370)

    botonAb6 = Button(piano, text= "A#6",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#6'))
    botonAb6.place(x =502, y =370)


    botonCb7 = Button(piano, text= "C#7",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#7'))
    botonCb7.place(x =578, y =370)

    botonDb7 = Button(piano, text= "D#7",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#7'))
    botonDb7.place(x =616, y =370)

    botonFb7 = Button(piano, text= "F#7",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#7'))
    botonFb7.place(x =692, y =370)

    botonGb7 = Button(piano, text= "G#7",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#7'))
    botonGb7.place(x =730, y =370)

    botonAb7 = Button(piano, text= "A#7",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#7'))
    botonAb7.place(x =768, y =370)


    botonCb8 = Button(piano, text= "C#8",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('C#8'))
    botonCb8.place(x =844, y =370)

    botonDb8 = Button(piano, text= "D#8",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('D#8'))
    botonDb8.place(x =882, y =370)

    botonFb8 = Button(piano, text= "F#8",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('F#8'))
    botonFb8.place(x =958, y =370)

    botonGb8 = Button(piano, text= "G#8",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('G#8'))
    botonGb8.place(x =996, y =370)

    botonAb8 = Button(piano, text= "A#8",
    bg= 'black', fg = 'white', width = 2, height = 6, command = lambda: piano_nota('A#8'))
    botonAb8.place(x =1034, y =370)

    title = Label(piano, text="Escoja una nota y un intervalo")
    title.config(font=("Helvetica", 24))
    title.place(x = 350, y = 10)

    texto = Label(piano, text="Intervalo:")
    texto.config(font=("Helvetica", 14))
    texto.place(x = 510, y = 66)

    global variable
    variable = StringVar(piano)
    variable.set("...") # default value
    w = OptionMenu(piano, variable, "...", "P1","m2","M2","m3","M3",
                          "P4","P5","m6","M6","m7",
                          "M7","P8","-m2","-M2",
                          "-m3","-M3","-P4","-P5","-m6",
                          "-M6","-m7","-M7","-P8")
    w.place(x = 525, y = 90)


    ok = Button(piano, text="Aceptar", command = lambda: arpegio2())
    ok.place(x = 525, y = 540)

    cerrar = Button(piano, text="Regresar", command = lambda: piano.destroy())
    cerrar.place(x = 525, y = 560)

    piano.mainloop()

show_frame(frame1)
window.mainloop()
