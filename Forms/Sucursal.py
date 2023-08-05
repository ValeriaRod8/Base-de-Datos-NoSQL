from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymongo

MONGO_USERNAME = "andreyszcr"
MONGO_PASSWORD = "Andy2024"
MONGO_CLUSTER = "cluster0.xcbz5rf.mongodb.net"
MONGO_DATABASE = "Flores"
MONGO_COLLECTION = "Sucursales"

# Conectarse a MongoDB Atlas
mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DATABASE}?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)
database = client[MONGO_DATABASE]
collection = database[MONGO_COLLECTION]
#

def mostrardatos():
    try:
        registros = tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in collection.find():
            tabla.insert('', 0, text=documento["_idSucursal"], values=(documento["Sucursal"],),text1=documento["Direccion"])
        client.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo extendido" + str(errorTiempo))
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a MongoDB" + str(errorConexion))

def crearRegistro():
    if len(nombre.get()) != 0 and len(sexo.get()) != 0:
        documento = {"nombre": nombre.get(), "sexo": sexo.get()}
        collection.insert_one(documento)
        nombre.delete(0, END)
        sexo.delete(0, END)
    else:
        messagebox.showerror(message="Los campos no pueden estar vacíos")
    mostrardatos()

ventana = Tk()

tabla = ttk.Treeview(ventana, columns=("_idSucursal", "nombre", "Direccion", "Provincia"))
#tabla = ttk.Treeview(ventana, columns=3)
tabla.grid(row=1, column=0, columnspan=4)
tabla.heading("#0", text="Codigo Sucursal")
tabla.heading("#1", text="Sucursal")
tabla.heading("#2", text="Direccion")
tabla.heading("#3", text="Provincia")

Label(ventana, text="Nombre").grid(row=2, column=0)
nombre = Entry(ventana)
nombre.grid(row=2, column=1)

Label(ventana, text="Sexo").grid(row=3, column=0)
sexo = Entry(ventana)
sexo.grid(row=3, column=1)

crear = Button(ventana, text="Crear Sucursal", command=crearRegistro, bg="blue", fg="white")
crear.grid(row=4, columnspan=2)

mostrardatos()
ventana.mainloop()
