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
    
def seleccionCollecion1(parColeccion1):
    global coleccion1
    global basedatos
    coleccion1=basedatos[parColeccion1]

def seleccionCollecion2(parColeccion2):
    global coleccion2
    global basedatos
    coleccion2=basedatos[parColeccion2]


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
            IdSucursal.set('Seleccione')
            IdProveedor.set('Seleccione')   
    
    
    
provinces = [
    "San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"
] 
#***************************************************************************
#***************************************************************************
#***************************************************************************
#***************************************************************************
#Eliminar una vez completado
fmProveedorS = Tk()
fmProveedorS.config(width = 1600, #1920
                    heigh = 900,#1080 
                    bg ="#BCCCF3" )
fmProveedorS.geometry("1600x900")
fmProveedorS.resizable(False,False)# para que no se agrande
fmProveedorS.after(0, lambda: centrar_ventana(fmProveedorS))
fmProveedorS.title("Tipos de Proveedor- Flores del Norte")
fmProveedorS.iconbitmap(r'flores.ico')

seleccionCollecion("ProveedorXSucursal")
seleccionCollecion1("Sucursales")
seleccionCollecion2("Proveedor")


proveedores_data = coleccion2.find({}, {"NombreProveedor": 1})
# Crear una lista con los nombres de los proveedores
proveedores_list = [proveedor["NombreProveedor"] for proveedor in proveedores_data]


sucursales_data = coleccion1.find({}, {"Sucursal": 1})
# Crear una lista con los nombres de los proveedores
sucursales_data  = [sucursal["Sucursal"] for sucursal in sucursales_data]



#Variables de Creacion, Edicion y Eliminacion
IdSucPrv = ""

#Variables de los text fields

IdSucursal = StringVar()
IdProveedor=StringVar()
_IdProveeSucur = StringVar()

#DiseÃ±o de los widgets en wd_Articulos

#Label variable (Creacion o edicion/eliminacion)
_IdProveeSucur.set("Estas en modo creacion!!!!")


lblSUCUR = Label(fmProveedorS,textvariable=_IdProveeSucur, bg ="#BCCCF3", font=("",15)).place(x=144,y=75)
lblSUCUR


lbl_IdSucursal = Label(fmProveedorS, text = "Proveedor", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
cbSucursal = ttk.Combobox(fmProveedorS,state="readonly",values=proveedores_list,font=("",15),textvariable=IdSucursal).place(x=144,y=206, width=385,height=36)
IdSucursal.set('Seleccione')


lbl_Sucursal = Label(fmProveedorS, text = "Sucursales", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
cbSucursal = ttk.Combobox(fmProveedorS,state="readonly",values=sucursales_data,font=("",15),textvariable=IdProveedor).place(x=144,y=290, width=385,height=36)
IdProveedor.set('Seleccione')




#Extraer datos
def selectItem(a):
    global IdSucPrv
    curItem = tbl_Prove_Sucur.focus()
    tupla = tbl_Prove_Sucur.item(curItem)['values']
    #print(tupla)
    IdSucPrv = tupla[0]
    IdSucursal.set(tupla[1])
    IdProveedor.set(tupla[2])
    _IdProveeSucur.set("Estas trabajando con el ID:  " + (str(IdSucPrv)))
    

# Tabla
tbl_ArticuloEstilo = ttk.Style()
tbl_ArticuloEstilo.theme_use('clam')
tbl_ArticuloEstilo.configure('tbl_Prove_Sucurview.Heading', background="#D9D9D9")

# Tabla Header
tbl_Prove_Sucur= ttk.Treeview(fmProveedorS, column=("c1", "c2","c3"), show= 'headings', height= 3)

tbl_Prove_Sucur.column("# 1",anchor= CENTER, width=200)
tbl_Prove_Sucur.heading("# 1", text= "Id ")
tbl_Prove_Sucur.column("# 2",anchor= CENTER, width=200)
tbl_Prove_Sucur.heading("# 2", text= "Provedor")
tbl_Prove_Sucur.column("# 3",anchor= CENTER, width=200)
tbl_Prove_Sucur.heading("# 3", text= "Sucursal")
tbl_Prove_Sucur.bind('<ButtonRelease-1>', selectItem)





#Funcion para mostrar los datos
def mostrardatos():
    try:
        registros=tbl_Prove_Sucur.get_children() 
        for registro in registros:
            tbl_Prove_Sucur.delete(registro)
        for documento in coleccion.find():
            tbl_Prove_Sucur.insert('','end',text=documento["_id"],values=(documento["_id"],documento["IdSucursal"],documento["Proveedor"]))
        #cliente.server_info()
        #print("Conexion a Mongo exitosa")
        
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo extendido"+errorTiempo)
    except pymongo.errors.ConectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb"+errorConexion) 

mostrardatos()

#Funcion crear registro
def crearRegistro():    
    global IdSucPrv
    if len(IdSucursal.get())!=0 and len(IdProveedor.get())!=0:

            documento={"IdSucursal": IdSucursal.get(),
                        "Proveedor": IdProveedor.get()} 
            coleccion.insert_one(documento)
            refrescar()
            IdSucPrv = ""
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrardatos()



#Refrescar Valores y setear en modo creacion
def refrescar():
        global IdSucPrv
        limpiarCampos()
        IdSucPrv = ""
        _IdProveeSucur.set("Estas en modo creacion!!!!")

#Eliminar Regisrtro
def eliminarRegistro():
    global IdSucPrv
    global coleccion
    if (IdSucPrv!=""):
        coleccion.delete_one({'_id': ObjectId(IdSucPrv)})
        mostrardatos()
        messagebox.showinfo(title="Eliminado",message='Articulo con el ID:'+ str(IdSucPrv))
        refrescar()
    else:
            messagebox.showerror(message='Debe seleccionar un registro')
#Actualizar Regisrtro

def actualizarRegistro():
    if len(IdSucursal.get())!=0 and len(IdProveedor.get())!=0:
        global IdSucPrv
        global coleccion
        filter = { '_id': ObjectId(IdSucPrv) }
        
        newvalues = { "$set": { "IdSucursal": IdSucursal.get(),
                        "Proveedor": IdProveedor.get()}}

        coleccion.update_one(filter, newvalues)
        mostrardatos()
        refrescar()
    else:
        messagebox.showerror(message='Los campos no pueden estar vacios')


#Ubicar la tabla en el frame
tbl_Prove_Sucur.place(x=700,y=99, height=780)
btn_Ingresar = Button(fmProveedorS,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=358, width=100,height=50)
btn_EjecutarCambios = Button(fmProveedorS,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428,y=358, width=100,height=50)
btn_Refrescar = Button(fmProveedorS,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=144,y=423, width=100,height=50)
btn_Eliminar = Button(fmProveedorS,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=423, width=100,height=50)

mainloop()