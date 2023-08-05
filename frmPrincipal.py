#from Forms.TipoArticulo import TipoArticulo
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage



# === Inicio de la región: Metodos del formulario ===
def set_background(root, image_path):
    image = PhotoImage(file=image_path)
    background_label = tk.Label(root, image=image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = image

#metodo para salir del sistema 
def exit_app():
    root.destroy()

def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
#----------------------------------------------------------------------------------------------------------------------------
# Formularios
def TipoArticulos():
#     def __init__(self, root):
         TipoArticulo= Toplevel(TipoArticulo)
         TipoArticulo.mainloop()
#----------------------------------------------------------------------------------------------------------------------------
# Crear la ventana principal
root = tk.Tk()
root.title("Formulario con Menú")
#este es el tamaño del formulario
root.geometry("800x800")
root.resizable(False,False)
root.after(0, lambda: centrar_ventana(root))
#Codigo para agregar el fondo de pantalla
#set_background(root,"E:\Andrey\Documents\Fidelitas\2023\02 Cuatri II\01 Base de Datos NOSQL\ProyectoNoSQL\Base-de-Datos-NoSQL\Img\main.png")

# Función para crear un menú "Archivo" con la opción "Salir"
def create_file_menu():
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Salir", command=exit_app)
    menu_bar.add_cascade(label="Archivo", menu=file_menu)

def articulos():
    
    articulo_bar=menu_bar
    articulos_menu = tk.Menu(articulo_bar, tearoff=0)
    articulos_menu.add_command(label="Tipo de Proveedor")
    articulos_menu.add_command(label="Mantenimiento de Proveedores")
    articulo_bar.add_cascade(label="Proveedores")


# Crear el menú
menu_bar = tk.Menu(root)
create_file_menu()
articulos()
root.config(menu=menu_bar)



# Bucle principal
root.mainloop()
