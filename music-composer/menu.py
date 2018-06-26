from tkinter import filedialog
from tkinter import*
from tkinter.filedialog import askopenfilename
from music21 import *

#*---------Variables----------*#
i = 0
composicion = [stream.Part(),stream.Part(),stream.Part(),stream.Part()]

#*-----------Ventana----------*#
window = Tk()
window.title("Compositor Musical")
window.resizable(0,0)
window.iconbitmap("icono.ico")
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
        #assert(posible)
        s = converter.parse(ruta)
        parte.append(s)
    except:
        print("La ruta especificada no es válida.")

def playAll():
    top = Toplevel()
    top.title("Compositor Musical")
    top.resizable(1,1)
    top.iconbitmap("icono.ico")
    top.geometry("500x300")
    top.config(bg="#999999")

    msg = Label(top, text="Reproducción de la composición", height=5, width=100)
    msg.config(font=("Helvetica", 20), bg="#999999")
    msg.pack()

    back = PhotoImage(file="button_regresar.png")
    botonBack = Button(top, image=back, border=0, bg="#999999", command = lambda: top.destroy())
    botonBack.pack()

    top.mainloop()

def show_frame(page_name):
    page_name.tkraise()

def cambiar_parte(j:int):
    global i
    i = j

def reproducir(parte:stream.Part)->"void":
    """
    Esta función reproduce una parte.
    """
    #Precondición de la definición:
    assert(True)
    parte.show("midi")
    #Postcondición de la definición:
    assert(True)

#*----------------------Widgets----------------------*#
#*--------- Frame 1---------*#
image = PhotoImage(file="titulo.png")
label = Label(frame1, image=image)
label.place(width="500", height="300")

imgP1 = PhotoImage(file="button1.png")
botonParte1 = Button(frame1, cursor="hand2", image=imgP1, border=0, bg="#999999", command = lambda: [show_frame(newframe),cambiar_parte(0)])
botonParte1.grid(row=0, column=0)

imgP2 = PhotoImage(file="button2.png")
botonParte2 = Button(frame1, cursor="hand2", image=imgP2, border=0, bg="#999999", command = lambda: show_frame(newframe))
botonParte2.grid(row=1, column=0)

imgP3 = PhotoImage(file="button3.png")
botonParte3 = Button(frame1, cursor="hand2", image=imgP3, border=0, bg="#999999", command = lambda: show_frame(newframe))
botonParte3.grid(row=2, column=0)

imgP4 = PhotoImage(file="button4.png")
botonParte4 = Button(frame1, cursor="hand2", image=imgP4, border=0, bg="#999999", command = lambda: show_frame(newframe))
botonParte4.grid(row=3, column=0)

imgEsc = PhotoImage(file="playb.png")
botonEsc = Button(frame1, cursor="hand2", image=imgEsc, border=0, bg="#999999", command = lambda: playAll())
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
image=imgArpegio, border=0, bg="#999999", command = lambda: show_frame(frameArp))
botonArpegio.grid( row=3, column=1, sticky=W+E+N+S)

imgTransportar = PhotoImage(file="button_transportar.png")
botonTransportar = Button(newframe, cursor="hand2",
image=imgTransportar, border=0, bg="#999999", command = lambda: show_frame(frameTrans))
botonTransportar.grid(row=6, column=0, sticky=W+E+N+S)

imgPlay = PhotoImage(file="button_escuchar.png")
botonPlay = Button(newframe, cursor="hand2", image=imgPlay,
border=0, bg="#999999", command = lambda: [show_frame(frameP), reproducir(composicion[i])])
botonPlay.grid(row=6, column=1, sticky=W+E+N+S)

imgBorrar = PhotoImage(file="button_borrar.png")
botonBorrar = Button(newframe, cursor="hand2", image=imgBorrar,
border=0, bg="#999999", command = lambda: show_frame(frameBorrar))
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
msgTrans = Label(frameTrans, text="Transponer Parte", height=5, width=100)
msgTrans.config(font=("Helvetica", 20), bg="#999999")
msgTrans.pack()

backTrans = PhotoImage(file="button_regresar.png")
botonBackTrans = Button(frameTrans, image=backTrans, border=0, bg="#999999",
command = lambda: show_frame(newframe))
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

show_frame(frame1)

window.mainloop()
