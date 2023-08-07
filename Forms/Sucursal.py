from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bson.objectid import ObjectId
import pymongo
import certifi
import os
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
            _idSucursal.set('')
            Sucursal.set('')  
            Direccion.set('')
            Provincia.set('Seleccione') 
    
 
def on_province_selected(event):
    selected_province = province_combobox.get()
    print("Provincia seleccionada:", selected_province)
   
provinces = [
    "San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"
]  
    
#***************************************************************************
#***************************************************************************
#***************************************************************************
#***************************************************************************
#Eliminar una vez completado
frmSucursal = Tk()
frmSucursal.config(width = 1600, #1920
                    heigh = 900,#1080 
                    bg ="#BCCCF3" )
frmSucursal.geometry("1600x900")
frmSucursal.resizable(False,False)# para que no se agrande
frmSucursal.after(0, lambda: centrar_ventana(frmSucursal))
frmSucursal.title("Tipos de Articulo- Flores del Norte")


def obtenerImagen(nombre, tipo):
    script_dir = os.path.dirname(__file__) #Carpeta Actual
    rel_path = "../Imagenes/" #Relative path
    abs_file_path = os.path.join(script_dir, rel_path) #Concatenacion de los 2
    current_file = nombre +"."+tipo 
    ImagenArticulo = abs_file_path+current_file
    return  ImagenArticulo



frmSucursal.iconbitmap(obtenerImagen("flores","ico"))

seleccionCollecion("Sucursales")




#Variables de Creacion, Edicion y Eliminacion
idSucursal = ""

#Variables de los text fields

_idSucursal = StringVar()
Sucursal=StringVar()
Direccion = StringVar()
Provincia=StringVar()


_idSucursal = StringVar()

#DiseÃ±o de los widgets en wd_Articulos

#Label variable (Creacion o edicion/eliminacion)
_idSucursal.set("Estas en modo creacion!!!!")

lbl_NombreArticulo = Label(frmSucursal,textvariable=_idSucursal, bg ="#BCCCF3", font=("",15)).place(x=144,y=75)

#Labels and Text entries 
lbl_NombreArticulo = Label(frmSucursal 
, text = "Codigo Sucursal", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
txt_NombreArticulo = Entry(frmSucursal 
,font=("",15),textvariable=_idSucursal).place(x=144,y=206, width=385,height=36)

lbl_TipoArticulo = Label(frmSucursal 
, text = "Sucursal", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
txt_TipoArticulo = Entry(frmSucursal 
,font=("",15),textvariable=Sucursal).place(x=144,y=290, width=385,height=36)

lbl_SucursalArticulo = Label(frmSucursal 
, text = "Direccion", bg ="#BCCCF3", font=("",15)).place(x=144,y=354)
txt_SucursalArticulo = Entry(frmSucursal 
,font=("",15),textvariable=Direccion).place(x=144,y=379, width=385,height=36)

lbl_Provincia = Label(frmSucursal, text = "Provincia", bg ="#BCCCF3", font=("",15)).place(x=144,y= 443)
province_combobox = ttk.Combobox(frmSucursal,state="readonly",values=provinces,font=("",15),textvariable=Provincia).place(x=144,y=473,width=385,height=36)
Provincia.set('Seleccione')



#Extraer datos
def selectItem(a):
    global idSucursal
    curItem = tbl_Sucursal.focus()
    tupla = tbl_Sucursal.item(curItem)['values']
    #print(tupla)
    idSucursal = tupla[0]
    _idSucursal.set(tupla[1])
    Sucursal.set(tupla[2])
    Direccion.set(tupla[3])
    Provincia.set(tupla[4])
    _idSucursal.set("Estas trabajando con el ID:  " + (str(idSucursal)))
    
    

# Tabla
tbl_ArticuloEstilo = ttk.Style()
tbl_ArticuloEstilo.theme_use('clam')
tbl_ArticuloEstilo.configure('tbl_Sucursalview.Heading', background="#D9D9D9")

# Tabla Header
tbl_Sucursal= ttk.Treeview(frmSucursal, column=("c1", "c2","c3","c4","c5"), show= 'headings', height= 6)

tbl_Sucursal.column("# 1",anchor= CENTER, width=200)
tbl_Sucursal.heading("# 1", text= "Id ")
tbl_Sucursal.column("# 2",anchor= CENTER, width=200)
tbl_Sucursal.heading("# 2", text= "Codigo de Sucursal")
tbl_Sucursal.column("# 3",anchor= CENTER, width=200)
tbl_Sucursal.heading("# 3", text= "Sucursal")
tbl_Sucursal.column("# 4",anchor= CENTER, width=200)
tbl_Sucursal.heading("# 4", text= "Direccion")
tbl_Sucursal.column("# 5",anchor= CENTER, width=200)
tbl_Sucursal.heading("# 5", text= "Provincia")
tbl_Sucursal.bind('<ButtonRelease-1>', selectItem)

#Funcion para mostrar los datos
def mostrardatos():
    try:
        registros=tbl_Sucursal.get_children()
        for registro in registros:
            tbl_Sucursal.delete(registro)
        for documento in coleccion.find():
            tbl_Sucursal.insert('','end',text=documento["_id"],values=(documento["_id"],documento["_idSucursal"],documento["Sucursal"],documento["Direccion"],documento["Provincia"]))
        #cliente.server_info()
        #print("Conexion a Mongo exitosa")
        
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo extendido"+errorTiempo)
    except pymongo.errors.ConectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb"+errorConexion) 

mostrardatos()

#Funcion crear registro
def crearRegistro():    
    global idSucursal
    if len(_idSucursal.get())!=0 and len(Sucursal.get())!=0:

            documento={"_idSucursal": int(_idSucursal.get()),
                        "Sucursal": Sucursal.get(),
                        "Direccion": Direccion.get(),
                        "Provincia": Provincia.get()} 
            coleccion.insert_one(documento)
            refrescar()
            idSucursal = ""
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrardatos()



#Refrescar Valores y setear en modo creacion
def refrescar():
        global idSucursal
        limpiarCampos()
        idSucursal = ""
        _idSucursal.set("Estas en modo creacion!!!!")

#Eliminar Regisrtro
def eliminarRegistro():
    global idSucursal
    global coleccion
    if (idSucursal!=""):
        coleccion.delete_one({'_id': ObjectId(idSucursal)})
        mostrardatos()
        messagebox.showinfo(title="Eliminado",message='Articulo con el ID:'+ str(idSucursal))
        refrescar()
    else:
            messagebox.showerror(message='Debe seleccionar un registro')
#Actualizar Regisrtro

def actualizarRegistro():
    if len(_idSucursal.get())!=0 and len(Sucursal.get())!=0:
        global idSucursal
        global coleccion
        filter = { '_id': ObjectId(idSucursal) }
        
        print(idSucursal)
        print(_idSucursal.get())
        print(Sucursal.get())
        print(Direccion.get())
        print(Provincia.get())
        print(coleccion)
        
        
        
        newvalues = { "$set": { "_idSucursal": _idSucursal.get(),
                        "Sucursal": Sucursal.get(),
                        "Direccion": Direccion.get(),
                        "Provincia": Provincia.get()}}

        coleccion.update_one(filter, newvalues)
        mostrardatos()
        refrescar()
    else:
        messagebox.showerror(message='Los campos no pueden estar vacios')


#Ubicar la tabla en el frame
tbl_Sucursal.place(x=550,y=99, height=780)
btn_Ingresar = Button(frmSucursal,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=538, width=100,height=50)
btn_EjecutarCambios = Button(frmSucursal,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428,y=538, width=100,height=50)
btn_Refrescar = Button(frmSucursal,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=144,y=623, width=100,height=50)
btn_Eliminar = Button(frmSucursal,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=623, width=100,height=50)
mainloop()