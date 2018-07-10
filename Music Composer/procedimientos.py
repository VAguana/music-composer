from music21 import *



"""
Una melodía es una lista de notas.
Una parte es un objeto del tipo "stream.Part"
Una canción es un objeto del tipo "stream.Score"
"""
nota = "null"
intervalo = "null"
intervalos_validos = ["P1","m2","M2","m3","M3"
                      "P4","P5","m6","M6","m7"
                      "M7","P8"]


def para_todo(lista):
    """
    cuantificador universal
    """
    p = True
    for i in lista:
        p = p and i
    return p

def existe(lista):
    """
    cuantificador existencial
    """
    p = False
    for i in lista:
        p = p or i
    return p

#FUNCIONAL
def convertir_parte(Melodia:list) -> stream.Part:
    """
    Esta función recibe una melodía (lista de notas) y devuelve una parte.
    """
    #Precondición de la definición:
    assert(True)
    parte = stream.Part()

    for i in Melodia:
        parte.append(i)

    #Postcondición de la definición:
    #Parte será la Melodía convertida a Parte

    return parte

#FUNCIONAL
def trasponer(parte:stream.Part,intervalo:str) -> stream.Part:
    """
    Esta funcion devuelve la traspuesta de una parte.
    """
    #Precondición de la definición:
    try:
        assert(existe(intervalo==i for i in intervalos_validos))
    except:
        print("El intervalo que ha introducido no es válido")
    #Programa
    try:
        assert(existe(intervalo==i for i in intervalos_validos))
        p = parte.transpose(intervalo)
    except:
        print("El intervalo no es válido.")
    return p
    #Postcondición de la definición:
    #p es la traspuesta de parte


#FUNCIONAL
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



def reiniciar_parte() -> "void":
    """
    Este procedimiento reinicia una parte, la deja vacía.
    """
    #Precondición de la definición:
    parte = stream.Part()
    #Postcondición de la definición:
    #parte ahora está vacía.

def reiniciar_cancion():
    """
    Este procedimiento reinicia una cancion
    """
    global cancion
    cancion = stream.Score()

#FUNCIONAL
def crear_arpegio(nota:note.Note,intervalo:str) -> stream.Part:
    """
    Este procedimiento crea un arpegio de 8 notas partiendo de una nota y
    serparado por un intervalo "intervalo".
    """
    #Precondición de la definición:
    try:
        assert(existe(i==intervalo for i in intervalos_validos) and (nota != "null") and (intervalo!="null"))
        parte = stream.Part()
        for i in range(8):
            parte.append(nota)
            nota = nota.transpose(intervalo)
    except:
        print("Ese intervalo no es válido.")

    #Postcondición de la definición:
    #parte es un arpegio de 8 notas separadas por "intervalo"

    return parte

#FUNCIONAL
def reproducir(parte:stream.Part)->"void":
    """
    Esta función reproduce una parte.
    """
    #Precondición de la definición:
    assert(True)
    parte.show("midi")
    #Postcondición de la definición:
    assert(True)


#FUNCIONAL
def componer(partes:list) -> "void":
    """
    Esta función crea una canción al componer una lista de partes
    """
    global cancion
    cancion = stream.Score()
    for i in partes:
        cancion.insert(0,i)

def comp_play(partes:list)-> "void":
    """
    Este procedimiento compone y reproduce una lista de notas.
    """
    componer(partes)
    reproducir(cancion)






#LAS SIGUIENTES SON VARIABLES DE TESTEO:
p0 = stream.Part()
p1 = stream.Part()

f = note.Note("F5")
g = note.Note("A5")

prueba = crear_arpegio(f,"m3")
prueba2 = crear_arpegio(g,"P8")
partes = [prueba, prueba2]
cancion = stream.Score()
cargar("/home/blitz/midis/cancion.tinynotation",cancion)
comp_play(partes)
