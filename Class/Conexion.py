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
class ConexionMongoDB:
    #************************************************************************************************
    def __init__(self,collection):
        self.mongo_uri = mongo_uri,
        self.client = client,
        self.collection = collection,
        self.database = database

    def conectar(self):
        try:
            self.cliente = pymongo.MongoClient(self.mongo_uri)
            self.base_datos = self.cliente[self.base_datos]
            print("Conexión a MongoDB establecida")
        except pymongo.errors.ConnectionFailure as error:
            print("Error al conectar a la base de datos de Flores:", error)
            
    def desconectar(self):
        if self.cliente:
            self.cliente.close()
            print("Conexión a Cerrada")
    #****************************************************************************************************
    def mostrardatos():
        try:
            registros = tabla.get_children()
            for registro in registros:
                tabla.delete(registro)
            for documento in collection.find():
                tabla.insert('', 0, text=documento["IdTipoArticulo"], values=documento["Articulo"])
            client.close()
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo extendido" + str(errorTiempo))
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a MongoDB" + str(errorConexion))
    
    
def crearRegistro():
    if len(nombre.get())!=0 and len(calificacion.get())!=0 and len(sexo.get())!=0:

            documento={"nombre": nombre.get(),"sexo":sexo.get()} 
            coleccion.insert(documento)
            nombre.delete(0,END)
            sexo.delete(0,END)
            calificacion.delete(0,END) 
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")                  
    mostrardatos()


            
    