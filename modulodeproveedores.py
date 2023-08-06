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
menuPrincipal = Tk()
menuPrincipal.config(width = 1600, #1920
                    heigh = 900,#1080 
                    bg ="#BCCCF3" )
menuPrincipal.geometry("1600x900")

seleccionCollecion("Proveedor")

'''
wd_Articulos = Toplevel(menuPrincipal)
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
_idProveedor.set("Modulo de Proveedor")


lbl_NombreProveedor = Label(menuPrincipal,textvariable=_idProveedor, bg ="#BCCCF3", font=("",15)).place(x=144,y=75)


lbl_NombreProveedor

#Labels and Text entries 
lbl_NombreArticulo = Label(menuPrincipal, text = "Nombre del Proveedor", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
txt_NombreArticulo = Entry(menuPrincipal,font=("",15),textvariable=NombreProveedor).place(x=144,y=206, width=385,height=36)

lbl_TipoArticulo = Label(menuPrincipal, text = "Apellidos", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
txt_TipoArticulo = Entry(menuPrincipal,font=("",15),textvariable= Apellidos).place(x=144,y=290, width=385,height=36)

lbl_SucursalArticulo = Label(menuPrincipal, text = "Provincia", bg ="#BCCCF3", font=("",15)).place(x=144,y=354)
txt_SucursalArticulo = Entry(menuPrincipal,font=("",15),textvariable=Provincia).place(x=144,y=379, width=385,height=36)

lbl_DescripcionArticulo = Label(menuPrincipal, text = "Correo", bg ="#BCCCF3", font=("",15)).place(x=144,y= 443)
txt_DescripcionArticulo  = Entry(menuPrincipal,font=("",15), textvariable=Correo).place(x=144,y=473,width=385,height=36)

lbl_PrecioArticulo = Label(menuPrincipal, text = "Direccion", bg ="#BCCCF3", font=("",15)).place(x=144,y=532)
txt_PrecioArticulo = Entry(menuPrincipal,font=("",15), textvariable=Direccion ).place(x=144,y=562, width=385,height=36)

lbl_CantidadArticulo = Label(menuPrincipal, text = "Genero", bg ="#BCCCF3", font=("",15)).place(x=144,y=621)
txt_CantidadArticulo = Entry(menuPrincipal,font=("",15), textvariable=genero).place(x=144,y=651, width=385,height=36)

lbl_tipoproveedor = Label(menuPrincipal, text = "Id tipo Proveedor", bg ="#BCCCF3", font=("",15)).place(x=144,y=710)
txt_tipoproveedor = Entry(menuPrincipal,font=("",15), textvariable=IdTipoProveedor).place(x=144,y=681, width=385,height=36)




#Extraer datos
def selectItem(a):
    global idproveedor
    curItem = tbl_Articulos.focus()
    tupla = tbl_Articulos.item(curItem)['values']
    #print(tupla)
    idproveedor = tupla[0]
    NombreProveedor.set(tupla[1])
    Apellidos.set(tupla[2])
    Provincia.set(tupla[3])
    Correo.set(tupla[4])
    Direccion.set(tupla[5])
    genero.set(tupla[6])
    IdTipoProveedor.set(tupla[7])
    _idProveedor.set("Estas trabajando con el ID:  " + (str(idproveedor)))
    
    

# Tabla
tbl_ArticuloEstilo = ttk.Style()
tbl_ArticuloEstilo.theme_use('clam')
tbl_ArticuloEstilo.configure('tbl_Articulosview.Heading', background="#D9D9D9")

# Tabla Header
tbl_Articulos= ttk.Treeview(menuPrincipal, column=("c1", "c2","c3","c4","c5","c6","c7","c8"), show= 'headings', height= 8)

tbl_Articulos.column("# 1",anchor= CENTER, width=100)
tbl_Articulos.heading("# 1", text= "Id Proveedor")
tbl_Articulos.column("# 2",anchor= CENTER)
tbl_Articulos.heading("# 2", text= "Nombre proveedor")
tbl_Articulos.column("# 3", anchor= CENTER, width=70)
tbl_Articulos.heading("# 3", text= "Apellidos")
tbl_Articulos.column("# 4",anchor=CENTER, width=70)
tbl_Articulos.heading("# 4", text= "Provincia")
tbl_Articulos.column("# 5",anchor=CENTER)
tbl_Articulos.heading("# 5", text= "Correo")
tbl_Articulos.column("# 6",anchor=CENTER, width=70)
tbl_Articulos.heading("# 6", text= "Direccion")
tbl_Articulos.column("# 7",anchor=CENTER, width=70)
tbl_Articulos.heading("# 7", text= "Genero")
tbl_Articulos.column("# 8",anchor=CENTER, width=70)
tbl_Articulos.heading("# 8", text= "Id Tipo proveedor")


tbl_Articulos.bind('<ButtonRelease-1>', selectItem)

#Funcion para mostrar los datos
def mostrardatos():
    try:
        registros=tbl_Articulos.get_children()
        for registro in registros:
            tbl_Articulos.delete(registro)
        for documento in coleccion.find():
            tbl_Articulos.insert('','end',text=documento["_id"],values=(documento["_id"],documento["NombreProveedor"],documento["Apellidos"],documento["Provincia"],documento["Correo"],documento["Direccion"],documento["Genero"],documento["IdTipoProveedor"]))
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
tbl_Articulos.place(x=750,y=99, height=780)
btn_Ingresar = Button(menuPrincipal,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=738, width=100,height=50)
btn_EjecutarCambios = Button(menuPrincipal,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428,y=738, width=100,height=50)
btn_Refrescar = Button(menuPrincipal,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=144,y=823, width=100,height=50)
btn_Eliminar = Button(menuPrincipal,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=823, width=100,height=50)

mainloop()