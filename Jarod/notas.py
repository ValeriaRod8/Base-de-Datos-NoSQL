#-------------------- Notas --------------------
#Tkinter es un puente entre Python y La libreria TCL/TK
'''
from tkin import * #Importar libreria

#Ventanas

raiz = Tk() #Creacion de ventana
raiz.mainloop() #Activar el action listener de la ventana

raiz.geometry("1440x1024")#Tamaño de la ventana
raiz.title('Floristeria') #Title de la ventana
raiz.resizable(0,0)# No permite el cambio de tamaño de la ventana
raiz.icobitmap() #Icono de la app
raiz.config() # Varias propiedades que le permite cambiar --- GUI

#Frame

miFrane = Frame(raiz) #Creacion del frame
miFrame.pack() # Empaqueta el frame a la ventana o otro frame
miFrame.pack(side = "right") # Posicionamiento de los frames en una sola direccion
miFrame.pack(side = "right", anchor="n") #Posicionamiento en dos direcciones
miFrame.pack(fill="x") #Rellenar a lo horizontal
miFrame.pack(fill="y", expand="True") #Rellenar a lo vertical
miFrame.pack(fill="both", expand="True") #Rellenar a ambos lados
miFrame.config(bd=35) #tamaño del borde (Por defecto es 0)
miFrame.config(relief="sunken") #bordes
miFrame.config(cursor="hand2") # cursor

#Label
milabel = Label(<contenedor>,<opciones> )
milabel.place(x="",y="")

<opciones>
Text - Texto que se muestra en el label
Anchor - Controla la posicion del texto
Bg - Color de fondo
Bd - Grosor del borde
Font - Tipo de Fuente
Fg - Color del texto
Image - Imagen dentro del label (Solo png y gif)
justify - Alineación del texto  miImagen = PhotoImage(file=<ruta>)  label(miFrame, Image = miImagen)
width
height
</opciones>

#WidgetsEntry
cuadroTexto = Entry(miFrame).place(x=",y=")
.config(show="*") # Password

#Grid
#Se utliza en lugar del place or pack para ponerlo en un grid
nombreLabel.grid(row = 0, column = 0, padx = 10 , pady=10) #Padding
cuadroTexto.grid(row = 0, column = 1, sticky =w, columnspan = 4) # Se encuentra n,w,s,e y sus intermedios + Column span para abarcar varias columnas

#Widget Text

lbl_Comentarios = Label(miFrame, text= "Comentarios")
txt_Comentario = Text(miFrame)
.config(width=150, heigh=150,)

#Widgt button
btn = Button(<contenedor>,<config>, command=<funcion>)

def codigo
'''