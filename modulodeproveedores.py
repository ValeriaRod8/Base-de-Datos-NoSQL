from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bson.objectid import ObjectId
import pymongo
import certifi


MONGO_USERNAME = "Jarod"
MONGO_PASSWORD = "Parche15"
MONGO_CLUSTER = "cluster0.xcbz5rf.mongodb.net"
MONGO_DATABASE = "Flores"



# Conectarse a MongoDB Atlas
mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DATABASE}?retryWrites=true&w=majority"

cliente = pymongo.MongoClient(mongo_uri, tlsCAFile=certifi.where())

MONGO_COLECCION=""
basedatos=cliente[MONGO_DATABASE]
coleccion=""

def seleccionCollecion(parColeccion):
    global coleccion
    global basedatos
    coleccion=basedatos[parColeccion]

#Eliminar una vez completado
f_Clientes = Tk()
f_Clientes.config(width = 1600, #1920
                    heigh = 900,#1080 
                    bg ="#BCCCF3" )
f_Clientes.geometry("1600x900")

seleccionCollecion("Proveedor")

'''
wd_Articulos = Toplevel(f_Clientes)
wd_Articulos.title('Floristeria - Articulos') #Nombre de la pagina
#wd_Articulos.iconbitmap('xxxx.ico') #Ver icono en ese momento ------

f_Articulos = Frame(wd_Articulos)
f_Articulos.config(width = 1600, #1920
                    heigh = 900,#1080 
                    bg ="#BCCCF3" )

f_Articulos.pack(fill="both",expand="True")
'''


#Variables de Creacion, Edicion y Eliminacion
idproveedor = ""

#Variables de los text fields
IdProveedor = StringVar()

NombreProveedor = StringVar()
Apellidos = StringVar()
Provincia = StringVar()
Correo = StringVar()
Direccion = StringVar()
genero = StringVar()
IdTipoProveedor = StringVar()
_idProveedor = StringVar()


#Diseño de los widgets en wd_Articulos

#Label variable (Creacion o edicion/eliminacion)

lbl_Modulo = Label(f_Clientes,text="Modulo de Proveedores", bg ="#BCCCF3", font=("",15)).place(x=144,y=75)

_idProveedor.set("Modo Creacion")


lbl_NombreProveedor = Label(f_Clientes,textvariable=_idProveedor, bg ="#BCCCF3", font=("",15)).place(x=144,y=120)

#Labels and Text entries 
lbl_NombreProveedor = Label(f_Clientes, text = "Nombre del Proveedor", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
txt_NombreProveedor = Entry(f_Clientes,font=("",15),textvariable=NombreProveedor).place(x=144,y=206, width=385,height=36)

lbl_Apellidos = Label(f_Clientes, text = "Apellidos", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
txt_Apellidos = Entry(f_Clientes,font=("",15),textvariable= Apellidos).place(x=144,y=290, width=385,height=36)

lbl_Provincia = Label(f_Clientes, text = "Provincia", bg ="#BCCCF3", font=("",15)).place(x=144,y=354)
txt_Provincia = Entry(f_Clientes,font=("",15),textvariable=Provincia).place(x=144,y=379, width=385,height=36)

lbl_Correo = Label(f_Clientes, text = "Correo", bg ="#BCCCF3", font=("",15)).place(x=144,y= 443)
txt_Correo  = Entry(f_Clientes,font=("",15), textvariable=Correo).place(x=144,y=473,width=385,height=36)

lbl_Direccion = Label(f_Clientes, text = "Direccion", bg ="#BCCCF3", font=("",15)).place(x=144,y=532)
txt_Direccion = Entry(f_Clientes,font=("",15), textvariable=Direccion ).place(x=144,y=562, width=385,height=36)

lbl_Genero = Label(f_Clientes, text = "Genero", bg ="#BCCCF3", font=("",15)).place(x=144,y=621)
txt_Genero = Entry(f_Clientes,font=("",15), textvariable=genero).place(x=144,y=651, width=385,height=36)

lbl_tipoProveedor = Label(f_Clientes, text = "Id Tipo Prove.", bg ="#BCCCF3", font=("",15)).place(x=144,y=710)
txt_tipoProveedor = Entry(f_Clientes,font=("",15), textvariable=IdTipoProveedor).place(x=144,y=740, width=385,height=36)




#Extraer datos
def selectItem(a):
    global idproveedor
    curItem = tbl_Proveedores.focus()
    tupla = tbl_Proveedores.item(curItem)['values']
    #print(tupla)
    idproveedor = tupla[0]
    NombreProveedor.set(tupla[1])
    Apellidos.set(tupla[2])
    Provincia.set(tupla[3])
    Correo.set(tupla[4])
    Direccion.set(tupla[5])
    genero.set(tupla[6])
    IdTipoProveedor.set(tupla[7])
    _idProveedor.set("Trabajando el ID:  " + (str(idproveedor)))
    
    

# Tabla
tbl_ProveedoresEstilo = ttk.Style()
tbl_ProveedoresEstilo.theme_use('clam')
tbl_ProveedoresEstilo.configure('tbl_Proveedoresview.Heading', background="#D9D9D9")

# Tabla Header
tbl_Proveedores= ttk.Treeview(f_Clientes, column=("c1", "c2","c3","c4","c5","c6","c7","c8"), show= 'headings', height= 8)

tbl_Proveedores.column("# 1",anchor= CENTER, width=100)
tbl_Proveedores.heading("# 1", text= "Id Proveedor")
tbl_Proveedores.column("# 2",anchor= CENTER)
tbl_Proveedores.heading("# 2", text= "Nombre proveedor")
tbl_Proveedores.column("# 3", anchor= CENTER, width=70)
tbl_Proveedores.heading("# 3", text= "Apellidos")
tbl_Proveedores.column("# 4",anchor=CENTER, width=70)
tbl_Proveedores.heading("# 4", text= "Provincia")
tbl_Proveedores.column("# 5",anchor=CENTER)
tbl_Proveedores.heading("# 5", text= "Correo")
tbl_Proveedores.column("# 6",anchor=CENTER, width=70)
tbl_Proveedores.heading("# 6", text= "Direccion")
tbl_Proveedores.column("# 7",anchor=CENTER, width=70)
tbl_Proveedores.heading("# 7", text= "Genero")
tbl_Proveedores.column("# 8",anchor=CENTER, width=70)
tbl_Proveedores.heading("# 8", text= "Id Tipo proveedor")


tbl_Proveedores.bind('<ButtonRelease-1>', selectItem)

#Funcion para mostrar los datos
def mostrardatos():
    try:
        registros=tbl_Proveedores.get_children()
        for registro in registros:
            tbl_Proveedores.delete(registro)
        for documento in coleccion.find():
            tbl_Proveedores.insert('','end',text=documento["_id"],values=(documento["_id"],documento["NombreProveedor"],documento["Apellidos"],documento["Provincia"],documento["Correo"],documento["Direccion"],documento["Genero"],documento["IdTipoProveedor"]))
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
    if len(NombreProveedor.get())!=0 and len(Apellidos.get())!=0 and len(Provincia.get())!=0 and len(Correo.get())!=0 and len(Direccion.get())!=0 and len(genero.get())!=0:

            documento={"NombreProveedor": NombreProveedor.get(),
                        "Apellidos": Apellidos.get(),
                        "Provincia": Provincia.get(),
                        "Correo" : Correo.get(),
                        "Direccion":Direccion.get(), 
                        "Genero":genero.get(), 
                        "IdTipoProveedor":int(IdTipoProveedor.get())} 
            coleccion.insert_one(documento)
            refrescar()
            idproveedor = ""
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrardatos()

# Limpiar Campos
def limpiarCampos():
            
            NombreProveedor.set('')
            Apellidos.set('')
            Provincia.set('')  
            Correo.set('')  
            Direccion.set('')   
            genero.set('')  
            IdTipoProveedor.set('')



#Refrescar Valores y setear en modo creacion
def refrescar():
        global idproveedor
        limpiarCampos()
        idproveedor = ""
        _idProveedor.set("Estas en el modulo de proveedores.")

#Eliminar Regisrtro
def eliminarRegistro():
    global idproveedor
    global coleccion
    if (idproveedor!=""):
        coleccion.delete_one({'_id': ObjectId(idproveedor)})
        mostrardatos()
        messagebox.showinfo(title="Eliminado",message='Proveedor con el ID:'+ str(idproveedor))
        refrescar()
    else:
            messagebox.showerror(message='Debe seleccionar un registro')
#Actualizar Regisrtro

def actualizarRegistro():
    if len(NombreProveedor.get())!=0 and len(Apellidos.get())!=0 and len(Provincia.get())!=0 and len(Correo.get())!=0 and len(Direccion.get())!=0 and len(genero.get())!=0:
        global idproveedor
        global coleccion
        filter = { '_id': ObjectId(idproveedor) }
        
        newvalues = { "$set": { "NombreProveedor": NombreProveedor.get(),
                        "Apellidos": Apellidos.get(),
                        "Provincia": Provincia.get(),
                        "Correo" : Correo.get(),
                        "Direccion":Direccion.get(), 
                        "Genero":genero.get(), 
                        "IdTipoProveedor":int(IdTipoProveedor.get())}}

        coleccion.update_one(filter, newvalues)
        mostrardatos()
        refrescar()
    else:
        messagebox.showerror(message='Los campos no pueden estar vacios')


#Ubicar la tabla en el frame
tbl_Proveedores.place(x=750,y=99, height=780)
btn_Ingresar = Button(f_Clientes,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=798, width=100,height=50)
btn_EjecutarCambios = Button(f_Clientes,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428,y=798, width=100,height=50)
btn_Refrescar = Button(f_Clientes,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=144,y=853, width=100,height=50)
btn_Eliminar = Button(f_Clientes,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=853, width=100,height=50)

mainloop()