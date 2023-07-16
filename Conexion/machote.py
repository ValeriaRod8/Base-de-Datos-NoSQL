from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
mongo_uri="mongodb://"+ MONGO_HOST+":"+ MONGO_PUERTO

MONGO_BASEDATOS="Escuela"
MONGO_COLECCION="alumnos"

cliente=pymongo.MongoClient(mongo_uri,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
basedatos=cliente[MONGO_BASEDATOS]
coleccion=basedatos[MONGO_COLECCION]

def mostrardatos():
    try:
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find():
            tabla.insert('',0,text=documento["_id"],values=documento["nombre"])
        #cliente.server_info()
        #print("Conexion a Mongo exitosa")
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo extendido"+errorTiempo)
    except pymongo.errors.ConectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb"+errorConexion)  

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

# Se hace el cambio para poder incluir la ventana que permitira el ingreso de mas documentos
ventana =Tk()
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0",text="ID")
tabla.heading("#1",text="NOMBRE")

#nombre
Label(ventana,text="Nombre").grid(row=2,column=0)
nombre=Entry(ventana)
nombre.grid(row=2,column=1)

#sexo
Label(ventana,text="Sexo").grid(row=3,column=0)
sexo=Entry(ventana)
sexo.grid(row=3,column=1)

#calificacion
Label(ventana,text="Calificacion").grid(row=4,column=0)
calificacion=Entry(ventana)
calificacion.grid(row=4,column=1)

#Boton Crear

crear=Button(ventana,text="Crear Alumno",command=crearRegistro,bg="blue",fg="white")
crear.grid(row=5,columnspan=2)
Label(ventana,text="Calificacion").grid(row=4,column=0)
calificacion=Entry(ventana)
calificacion.grid(row=4,column=1)

mostrardatos()
ventana.mainloop()
