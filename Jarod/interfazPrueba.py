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

seleccionCollecion("Articulos")

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
idArticulo = ""

#Variables de los text fields
nombreArticulo = StringVar()
tipoArticulo = StringVar()
sucursalArticulo = StringVar()
descripcionArticulo = StringVar()
precioArticulo = StringVar()
cantidadArticulo = StringVar()
_idArticulo = StringVar()

#Diseño de los widgets en wd_Articulos

#Label variable (Creacion o edicion/eliminacion)
_idArticulo.set("Estas en modo creacion!!!!")


lbl_NombreArticulo = Label(menuPrincipal,textvariable=_idArticulo, bg ="#BCCCF3", font=("",15)).place(x=144,y=75)


lbl_NombreArticulo

#Labels and Text entries 
lbl_NombreArticulo = Label(menuPrincipal, text = "Nombre del Articulo", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
txt_NombreArticulo = Entry(menuPrincipal,font=("",15),textvariable=nombreArticulo).place(x=144,y=206, width=385,height=36)

lbl_TipoArticulo = Label(menuPrincipal, text = "ID Tipo de Articulo", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
txt_TipoArticulo = Entry(menuPrincipal,font=("",15),textvariable=tipoArticulo).place(x=144,y=290, width=385,height=36)

lbl_SucursalArticulo = Label(menuPrincipal, text = "ID Sucursal", bg ="#BCCCF3", font=("",15)).place(x=144,y=354)
txt_SucursalArticulo = Entry(menuPrincipal,font=("",15),textvariable=sucursalArticulo).place(x=144,y=379, width=385,height=36)

lbl_DescripcionArticulo = Label(menuPrincipal, text = "Descripcion", bg ="#BCCCF3", font=("",15)).place(x=144,y= 443)
txt_DescripcionArticulo  = Entry(menuPrincipal,font=("",15), textvariable=descripcionArticulo).place(x=144,y=473,width=385,height=36)

lbl_PrecioArticulo = Label(menuPrincipal, text = "Precio", bg ="#BCCCF3", font=("",15)).place(x=144,y=532)
txt_PrecioArticulo = Entry(menuPrincipal,font=("",15), textvariable=precioArticulo ).place(x=144,y=562, width=385,height=36)

lbl_CantidadArticulo = Label(menuPrincipal, text = "Cantidad", bg ="#BCCCF3", font=("",15)).place(x=144,y=621)
txt_CantidadArticulo = Entry(menuPrincipal,font=("",15), textvariable=cantidadArticulo).place(x=144,y=651, width=385,height=36)


#Extraer datos
def selectItem(a):
    global idArticulo
    curItem = tbl_Articulos.focus()
    tupla = tbl_Articulos.item(curItem)['values']
    #print(tupla)
    idArticulo = tupla[0]
    nombreArticulo.set(tupla[1])
    tipoArticulo.set(tupla[2])
    sucursalArticulo.set(tupla[3])
    descripcionArticulo.set(tupla[4])
    precioArticulo.set(tupla[5].removeprefix("$"))
    cantidadArticulo.set(tupla[6])
    _idArticulo.set("Estas trabajando con el ID:  " + (str(idArticulo)))
    
    

# Tabla
tbl_ArticuloEstilo = ttk.Style()
tbl_ArticuloEstilo.theme_use('clam')
tbl_ArticuloEstilo.configure('tbl_Articulosview.Heading', background="#D9D9D9")

# Tabla Header
tbl_Articulos= ttk.Treeview(menuPrincipal, column=("c1", "c2","c3","c4","c5","c6","c7"), show= 'headings', height= 8)

tbl_Articulos.column("# 1",anchor= CENTER, width=100)
tbl_Articulos.heading("# 1", text= "Id Articulo")
tbl_Articulos.column("# 2",anchor= CENTER)
tbl_Articulos.heading("# 2", text= "Nombre Articulo")
tbl_Articulos.column("# 3", anchor= CENTER, width=70)
tbl_Articulos.heading("# 3", text= "Id Tipo")
tbl_Articulos.column("# 4",anchor=CENTER, width=70)
tbl_Articulos.heading("# 4", text= "Id Sucursal")
tbl_Articulos.column("# 5",anchor=CENTER)
tbl_Articulos.heading("# 5", text= "Descripcion")
tbl_Articulos.column("# 6",anchor=CENTER, width=70)
tbl_Articulos.heading("# 6", text= "Precio")
tbl_Articulos.column("# 7",anchor=CENTER, width=70)
tbl_Articulos.heading("# 7", text= "Cantidad")

tbl_Articulos.bind('<ButtonRelease-1>', selectItem)

#Funcion para mostrar los datos
def mostrardatos():
    try:
        registros=tbl_Articulos.get_children()
        for registro in registros:
            tbl_Articulos.delete(registro)
        for documento in coleccion.find():
            tbl_Articulos.insert('','end',text=documento["_id"],values=(documento["_id"],documento["NombreArticulo"],documento["IdTipoArticulo"],documento["_idSucursal"],documento["Descripcion"],"$"+ str(documento["PrecioUnitario"]),documento["Cantidad"]))
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
    if len(nombreArticulo.get())!=0 and len(tipoArticulo.get())!=0 and len(sucursalArticulo.get())!=0 and len(descripcionArticulo.get())!=0 and len(precioArticulo.get())!=0 and len(cantidadArticulo.get())!=0:

            documento={"NombreArticulo": nombreArticulo.get(),
                        "IdTipoArticulo": int(tipoArticulo.get()),
                        "_idSucursal": int(sucursalArticulo.get()),
                        "Descripcion" : descripcionArticulo.get(),
                        "PrecioUnitario":float(precioArticulo.get()), 
                        "Cantidad":int(cantidadArticulo.get())} 
            coleccion.insert_one(documento)
            refrescar()
            idArticulo = ""
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrardatos()

# Limpiar Campos
def limpiarCampos():
            nombreArticulo.set('')
            tipoArticulo.set('')
            sucursalArticulo.set('')
            descripcionArticulo.set('')
            precioArticulo.set('')
            cantidadArticulo.set('')


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
    if len(nombreArticulo.get())!=0 and len(tipoArticulo.get())!=0 and len(sucursalArticulo.get())!=0 and len(descripcionArticulo.get())!=0 and len(precioArticulo.get())!=0 and len(cantidadArticulo.get())!=0:
        global idArticulo
        global coleccion
        filter = { '_id': ObjectId(idArticulo) }
        
        newvalues = { "$set": { "NombreArticulo": nombreArticulo.get(),
                        "IdTipoArticulo": int(tipoArticulo.get()),
                        "_idSucursal": int(sucursalArticulo.get()),
                        "Descripcion" : descripcionArticulo.get(),
                        "PrecioUnitario":float(precioArticulo.get()), 
                        "Cantidad":int(cantidadArticulo.get())}}

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