from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bson.objectid import ObjectId
import pymongo
import certifi
#***************************************************************************
#variables de la conexion de la base de datos 
MONGO_USERNAME = "andreyszcr"
MONGO_PASSWORD = "Andy2024"
MONGO_CLUSTER = "cluster0.xcbz5rf.mongodb.net"
MONGO_DATABASE = "Flores"
# Conectarse a MongoDB Atlas
mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DATABASE}?retryWrites=true&w=majority"
cliente = pymongo.MongoClient(mongo_uri, tlsCAFile=certifi.where())
MONGO_COLECCION=""
basedatos=cliente[MONGO_DATABASE]
coleccion=""
#***************************************************************************
# Metodos generales 
#***************************************************************************
# metodo para la coleccion
def seleccionCollecion(parColeccion):
    global coleccion
    global basedatos
    coleccion=basedatos[parColeccion]

#metodo para centrar la ventana
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}") 
    
# Limpiar Campos
def limpiarCampos():
            IdTipoProveedor.set('')
            Proveedor.set('')   
    
    
#***************************************************************************
#***************************************************************************
#***************************************************************************
#***************************************************************************
#Eliminar una vez completado
fmProveedor = Tk()
fmProveedor.config(width = 1600, #1920
                    heigh = 900,#1080 
                    bg ="#BCCCF3" )
fmProveedor.geometry("1600x900")
fmProveedor.resizable(False,False)# para que no se agrande
fmProveedor.after(0, lambda: centrar_ventana(fmProveedor))
fmProveedor.title("Tipos de Proveedor- Flores del Norte")
fmProveedor.iconbitmap(r'flores.ico')

seleccionCollecion("TiposProveedor")

#Sucursales


#Variables de Creacion, Edicion y Eliminacion
idArticulo = ""

#Variables de los text fields

IdTipoProveedor = StringVar()
Proveedor=StringVar()

_idArticulo = StringVar()

#DiseÃ±o de los widgets en wd_Articulos

#Label variable (Creacion o edicion/eliminacion)
_idArticulo.set("Estas en modo creacion!!!!")


lbl_NombreArticulo = Label(fmProveedor,textvariable=_idArticulo, bg ="#BCCCF3", font=("",15)).place(x=144,y=75)
lbl_NombreArticulo

#Labels and Text entries 
lbl_NombreArticulo = Label(fmProveedor, text = "Codigo", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
txt_NombreArticulo = Entry(fmProveedor,font=("",15),textvariable=IdTipoProveedor).place(x=144,y=206, width=385,height=36)

lbl_Proveedor = Label(fmProveedor, text = "Tipo de Proveedor", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
txt_Proveedor = Entry(fmProveedor,font=("",15),textvariable=Proveedor).place(x=144,y=290, width=385,height=36)


#Extraer datos
def selectItem(a):
    global idArticulo
    curItem = tbl_TiposProveedor.focus()
    tupla = tbl_TiposProveedor.item(curItem)['values']
    #print(tupla)
    idArticulo = tupla[0]
    IdTipoProveedor.set(tupla[1])
    Proveedor.set(tupla[2])
    _idArticulo.set("Estas trabajando con el ID:  " + (str(idArticulo)))
    

# Tabla
tbl_ArticuloEstilo = ttk.Style()
tbl_ArticuloEstilo.theme_use('clam')
tbl_ArticuloEstilo.configure('tbl_TiposProveedorview.Heading', background="#D9D9D9")

# Tabla Header
tbl_TiposProveedor= ttk.Treeview(fmProveedor, column=("c1", "c2","c3"), show= 'headings', height= 3)

tbl_TiposProveedor.column("# 1",anchor= CENTER, width=200)
tbl_TiposProveedor.heading("# 1", text= "Id ")
tbl_TiposProveedor.column("# 2",anchor= CENTER, width=200)
tbl_TiposProveedor.heading("# 2", text= "Codigo de Tipo de Proveedor")
tbl_TiposProveedor.column("# 3",anchor= CENTER, width=200)
tbl_TiposProveedor.heading("# 3", text= "Tipo de Proveedor")
tbl_TiposProveedor.bind('<ButtonRelease-1>', selectItem)

#Funcion para mostrar los datos
def mostrardatos():
    try:
        registros=tbl_TiposProveedor.get_children() 
        for registro in registros:
            tbl_TiposProveedor.delete(registro)
        for documento in coleccion.find():
            tbl_TiposProveedor.insert('','end',text=documento["_id"],values=(documento["_id"],documento["IdTipoProveedor"],documento["Proveedor"]))
        #cliente.server_info()
        #print("Conexion a Mongo exitosa")
        
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo extendido"+errorTiempo)
    except pymongo.errors.ConectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb"+errorConexion) 

mostrardatos()

#Funcion crear registro
def crearRegistro():    
    global idArticulo
    if len(IdTipoProveedor.get())!=0 and len(Proveedor.get())!=0:

            documento={"IdTipoProveedor": int(IdTipoProveedor.get()),
                        "Proveedor": Proveedor.get()} 
            coleccion.insert_one(documento)
            refrescar()
            idArticulo = ""
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrardatos()



#Refrescar Valores y setear en modo creacion
def refrescar():
        global idArticulo
        limpiarCampos()
        idArticulo = ""
        _idArticulo.set("Estas en modo creacion!!!!")

#Eliminar Regisrtro
def eliminarRegistro():
    global idArticulo
    global coleccion
    if (idArticulo!=""):
        coleccion.delete_one({'_id': ObjectId(idArticulo)})
        mostrardatos()
        messagebox.showinfo(title="Eliminado",message='Articulo con el ID:'+ str(idArticulo))
        refrescar()
    else:
            messagebox.showerror(message='Debe seleccionar un registro')
#Actualizar Regisrtro

def actualizarRegistro():
    if len(IdTipoProveedor.get())!=0 and len(Proveedor.get())!=0:
        global idArticulo
        global coleccion
        filter = { '_id': ObjectId(idArticulo) }
        
        newvalues = { "$set": { "IdTipoProveedor": IdTipoProveedor.get(),
                        "Proveedor": Proveedor.get()}}

        coleccion.update_one(filter, newvalues)
        mostrardatos()
        refrescar()
    else:
        messagebox.showerror(message='Los campos no pueden estar vacios')


#Ubicar la tabla en el frame
tbl_TiposProveedor.place(x=700,y=99, height=780)
btn_Ingresar = Button(fmProveedor,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=358, width=100,height=50)
btn_EjecutarCambios = Button(fmProveedor,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428,y=358, width=100,height=50)
btn_Refrescar = Button(fmProveedor,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=144,y=423, width=100,height=50)
btn_Eliminar = Button(fmProveedor,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=423, width=100,height=50)

mainloop()