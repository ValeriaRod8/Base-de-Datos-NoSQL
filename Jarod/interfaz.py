from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bson.objectid import ObjectId
from PIL import ImageTk, Image
import pymongo
import certifi
import os

'''
#Conexion con Mongo Compas
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
mongo_uri="mongodb://"+ MONGO_HOST+":"+ MONGO_PUERTO
cliente=pymongo.MongoClient(mongo_uri,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
'''

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

# Variables para determinar la apertura de alguna ventana
ventanaArticuloAbierta = False


#Funcion que selecciona la coleccion
def seleccionCollecion(parColeccion):
    global coleccion
    global basedatos
    coleccion=basedatos[parColeccion]


 
#Creacion de la ventana main
menuPrincipal = Tk()
f_menuPrincipal = Frame(menuPrincipal)
f_menuPrincipal.config(width = 1600, #1920
                        heigh = 900,#1080 
                        bg ="#BCCCF3" )

f_menuPrincipal.pack(fill="both",expand="True")

def openWd_Articulo():
    
    #Obtener la collecion a trabjar
    seleccionCollecion("Articulos")
    global coleccion

    wd_Articulos = Toplevel(menuPrincipal)
    wd_Articulos.title('Floristeria - Articulos') #Nombre de la pagina
    #wd_Articulos.iconbitmap('xxxx.ico') #Ver icono en ese momento ------


    f_Articulos = Frame(wd_Articulos)
    f_Articulos.config(width = 1600, #1920
                        heigh = 1024,#1080 
                        bg ="#BCCCF3" )

    f_Articulos.pack(fill="both",expand="True")

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

    lbl_Modulo = Label(f_Articulos,text="Modulo de Clientes", bg ="#BCCCF3", font=("",15)).place(x=144,y=75)


    lbl_idArticulo = Label(f_Articulos,textvariable=_idArticulo, bg ="#BCCCF3", font=("",15)).place(x=144,y=120)

    _idArticulo.set("Modo Creacion")


    #Labels and Text entries 
    lbl_NombreArticulo = Label(f_Articulos, text = "Nombre del Articulo", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
    txt_NombreArticulo = Entry(f_Articulos,font=("",15),textvariable=nombreArticulo).place(x=144,y=206, width=385,height=36)

    lbl_TipoArticulo = Label(f_Articulos, text = "ID Tipo de Articulo", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
    txt_TipoArticulo = Entry(f_Articulos,font=("",15),textvariable=tipoArticulo).place(x=144,y=290, width=385,height=36)

    lbl_SucursalArticulo = Label(f_Articulos, text = "ID Sucursal", bg ="#BCCCF3", font=("",15)).place(x=144,y=354)
    txt_SucursalArticulo = Entry(f_Articulos,font=("",15),textvariable=sucursalArticulo).place(x=144,y=379, width=385,height=36)

    lbl_DescripcionArticulo = Label(f_Articulos, text = "Descripcion", bg ="#BCCCF3", font=("",15)).place(x=144,y= 443)
    txt_DescripcionArticulo  = Entry(f_Articulos,font=("",15), textvariable=descripcionArticulo).place(x=144,y=473,width=385,height=36)

    lbl_PrecioArticulo = Label(f_Articulos, text = "Precio", bg ="#BCCCF3", font=("",15)).place(x=144,y=532)
    txt_PrecioArticulo = Entry(f_Articulos,font=("",15), textvariable=precioArticulo ).place(x=144,y=562, width=385,height=36)

    lbl_CantidadArticulo = Label(f_Articulos, text = "Cantidad", bg ="#BCCCF3", font=("",15)).place(x=144,y=621)
    txt_CantidadArticulo = Entry(f_Articulos,font=("",15), textvariable=cantidadArticulo).place(x=144,y=651, width=385,height=36)


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
        _idArticulo.set("Trabajando el ID:  " + (str(idArticulo)))
        
        

    # Tabla
    tbl_ArticuloEstilo = ttk.Style()
    tbl_ArticuloEstilo.theme_use('clam')
    tbl_ArticuloEstilo.configure('tbl_Articulosview.Heading', background="#D9D9D9")

    # Tabla Header
    tbl_Articulos= ttk.Treeview(f_Articulos, column=("c1", "c2","c3","c4","c5","c6","c7"), show= 'headings', height= 8)
    
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
         _idArticulo.set("Modo creacion")
    
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
    btn_Ingresar = Button(f_Articulos,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=738, width=100,height=50)
    btn_EjecutarCambios = Button(f_Articulos,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428,y=738, width=100,height=50)
    btn_Refrescar = Button(f_Articulos,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=144,y=823, width=100,height=50)
    btn_Eliminar = Button(f_Articulos,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=823, width=100,height=50)


def openWd_Proveedor():
    
    #Obtener la collecion a trabjar
    seleccionCollecion("Proveedor")
    global coleccion


    wd_Proveedor = Toplevel(menuPrincipal)
    wd_Proveedor.title('Floristeria - Articulos') #Nombre de la pagina
    #wd_Articulos.iconbitmap('xxxx.ico') #Ver icono en ese momento ------


    f_Proveedor = Frame(wd_Proveedor)
    f_Proveedor.config(width = 1600, #1920
                        heigh = 1024,#1080 
                        bg ="#BCCCF3" )

    f_Proveedor.pack(fill="both",expand="True")
    

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

    lbl_Modulo = Label(f_Proveedor,text="Modulo de Proveedores", bg ="#BCCCF3", font=("",15)).place(x=144,y=75)

    _idProveedor.set("Modo Creacion")


    lbl_NombreProveedor = Label(f_Proveedor,textvariable=_idProveedor, bg ="#BCCCF3", font=("",15)).place(x=144,y=120)

    #Labels and Text entries 
    lbl_NombreProveedor = Label(f_Proveedor, text = "Nombre del Proveedor", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
    txt_NombreProveedor = Entry(f_Proveedor,font=("",15),textvariable=NombreProveedor).place(x=144,y=206, width=385,height=36)

    lbl_Apellidos = Label(f_Proveedor, text = "Apellidos", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
    txt_Apellidos = Entry(f_Proveedor,font=("",15),textvariable= Apellidos).place(x=144,y=290, width=385,height=36)

    lbl_Provincia = Label(f_Proveedor, text = "Provincia", bg ="#BCCCF3", font=("",15)).place(x=144,y=354)
    txt_Provincia = Entry(f_Proveedor,font=("",15),textvariable=Provincia).place(x=144,y=379, width=385,height=36)

    lbl_Correo = Label(f_Proveedor, text = "Correo", bg ="#BCCCF3", font=("",15)).place(x=144,y= 443)
    txt_Correo  = Entry(f_Proveedor,font=("",15), textvariable=Correo).place(x=144,y=473,width=385,height=36)

    lbl_Direccion = Label(f_Proveedor, text = "Direccion", bg ="#BCCCF3", font=("",15)).place(x=144,y=532)
    txt_Direccion = Entry(f_Proveedor,font=("",15), textvariable=Direccion ).place(x=144,y=562, width=385,height=36)

    lbl_Genero = Label(f_Proveedor, text = "Genero", bg ="#BCCCF3", font=("",15)).place(x=144,y=621)
    txt_Genero = Entry(f_Proveedor,font=("",15), textvariable=genero).place(x=144,y=651, width=385,height=36)

    lbl_tipoProveedor = Label(f_Proveedor, text = "Id Tipo Prove.", bg ="#BCCCF3", font=("",15)).place(x=144,y=710)
    txt_tipoProveedor = Entry(f_Proveedor,font=("",15), textvariable=IdTipoProveedor).place(x=144,y=740, width=385,height=36)




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
    tbl_Proveedores= ttk.Treeview(f_Proveedor, column=("c1", "c2","c3","c4","c5","c6","c7","c8"), show= 'headings', height= 8)

    tbl_Proveedores.column("# 1",anchor= CENTER, width=100)
    tbl_Proveedores.heading("# 1", text= "Id Proveedor")
    tbl_Proveedores.column("# 2",anchor= CENTER)
    tbl_Proveedores.heading("# 2", text= "Nombre proveedor")
    tbl_Proveedores.column("# 3", anchor= CENTER, width=50)
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
            _idProveedor.set("Modo Creacion")

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
    btn_Ingresar = Button(f_Proveedor,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=798, width=100,height=50)
    btn_EjecutarCambios = Button(f_Proveedor,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428,y=798, width=100,height=50)
    btn_Refrescar = Button(f_Proveedor,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=144,y=853, width=100,height=50)
    btn_Eliminar = Button(f_Proveedor,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=853, width=100,height=50)


def openwd_Cliente():

    #Obtener la collecion a trabjar
    seleccionCollecion("Clientes")
    global coleccion


    wd_Cliente = Toplevel(menuPrincipal)
    wd_Cliente.title('Floristeria - Clientes') #Nombre de la pagina
    #wd_Articulos.iconbitmap('xxxx.ico') #Ver icono en ese momento ------


    f_Clientes = Frame(wd_Cliente)
    f_Clientes.config(width = 1600, #1920
                        heigh = 1024,#1080 
                        bg ="#BCCCF3" )

    f_Clientes.pack(fill="both",expand="True")
    
        
    idCliente = ""

    #Variables de los text fields
    nombreCliente = StringVar()
    apellidosCliente = StringVar()
    nacionalidadCliente = StringVar()
    provinciaCliente = StringVar()
    correoCliente = StringVar()
    direccionCliente = StringVar()
    generoCliente = StringVar()

    #Diseño de los widgets en wd_Clientes
    IdCliente = StringVar()

    #Label variable (Creacion o edicion/eliminacion)
    lbl_Modulo = Label(f_Clientes,text="Modulo de Clientes", bg ="#BCCCF3", font=("",15)).place(x=144,y=75)

    IdCliente.set("Modo Creacion")


    lbl_nombreCliente = Label(f_Clientes,textvariable=IdCliente, bg ="#BCCCF3", font=("",15)).place(x=144,y=120)


    #Labels and Text entries 
    lbl_nombreCliente = Label(f_Clientes, text = "Nombre del Cliente", bg ="#BCCCF3", font=("",15)).place(x=144,y=176)
    txt_nombreCliente = Entry(f_Clientes,font=("",15),textvariable=nombreCliente).place(x=144,y=201, width=385,height=36)

    lbl_apellidosCliente = Label(f_Clientes, text = "Apellidos del Cliente", bg ="#BCCCF3", font=("",15)).place(x=144,y=265)
    txt_apellidosCliente = Entry(f_Clientes,font=("",15),textvariable=apellidosCliente).place(x=144,y=290, width=385,height=36)

    lbl_nacionalidadCliente = Label(f_Clientes, text = "Nacionalidad del Cliente", bg ="#BCCCF3", font=("",15)).place(x=144,y=354)
    txt_nacionalidadCliente = Entry(f_Clientes,font=("",15),textvariable=nacionalidadCliente).place(x=144,y=379, width=385,height=36)

    lbl_provinciaCliente = Label(f_Clientes, text = "Provincia del Cliente", bg ="#BCCCF3", font=("",15)).place(x=144,y=443)
    txt_provinciaCliente = Entry(f_Clientes,font=("",15), textvariable=provinciaCliente).place(x=144,y=468, width=385,height=36)

    lbl_correoCliente = Label(f_Clientes, text = "Correo del Cliente", bg ="#BCCCF3", font=("",15)).place(x=144,y=532)
    txt_correoCliente = Entry(f_Clientes,font=("",15), textvariable=correoCliente).place(x=144,y=557, width=385,height=36)

    lbl_direccionCliente = Label(f_Clientes, text = "Direccion del Cliente", bg ="#BCCCF3", font=("",15)).place(x=144,y=621)
    txt_direccionCliente = Entry(f_Clientes,font=("",15), textvariable=direccionCliente).place(x=144,y=646, width=385,height=36)

    bl_generoCliente = Label(f_Clientes, text = "Genero del Cliente", bg ="#BCCCF3", font=("",15)).place(x=144,y=710)
    txt_generoCliente = Entry(f_Clientes,font=("",15), textvariable=generoCliente).place(x=144,y=735, width=385,height=36)



    #Extraer datos
    def selectItem(a):
        global idCliente
        curItem = tbl_cliente.focus()
        tupla = tbl_cliente.item(curItem)['values']
        #print(tupla)
        idCliente = tupla[0]
        nombreCliente.set(tupla[1])
        apellidosCliente.set(tupla[2])
        nacionalidadCliente.set(tupla[3])
        provinciaCliente.set(tupla[4])
        correoCliente.set(tupla[5])
        direccionCliente.set(tupla[6])
        generoCliente.set(tupla[7])
        IdCliente.set("Trabajando el ID:  " + (str(idCliente)))
        
        

    # Tabla
    tbl_ClienteEstilo = ttk.Style()
    tbl_ClienteEstilo.theme_use('clam')
    tbl_ClienteEstilo.configure('tbl_clienteview.Heading', background="#D9D9D9")

    # Tabla Header
    tbl_cliente= ttk.Treeview(f_Clientes, column=("c1", "c2","c3","c4","c5","c6","c7","c8"), show= 'headings', height= 8)

    tbl_cliente.column("# 1",anchor= CENTER, width=100)
    tbl_cliente.heading("# 1", text= "Id Cliente")
    tbl_cliente.column("# 2",anchor= CENTER)
    tbl_cliente.heading("# 2", text= "Nombre")
    tbl_cliente.column("# 3", anchor= CENTER, width=70)
    tbl_cliente.heading("# 3", text= "Apellidos")
    tbl_cliente.column("# 4",anchor=CENTER, width=70)
    tbl_cliente.heading("# 4", text= "Nacionalidad")
    tbl_cliente.column("# 5",anchor=CENTER)
    tbl_cliente.heading("# 5", text= "Provincia")
    tbl_cliente.column("# 6",anchor=CENTER, width=30)
    tbl_cliente.heading("# 6", text= "Correo")
    tbl_cliente.column("# 7",anchor=CENTER, width=70)
    tbl_cliente.heading("# 7", text= "Direccion")
    tbl_cliente.column("# 8",anchor=CENTER, width=70)
    tbl_cliente.heading("# 8", text= "Genero")

    tbl_cliente.bind('<ButtonRelease-1>', selectItem)

    #Funcion para mostrar los datos
    def mostrardatos():
        try:
            registros=tbl_cliente.get_children()
            for registro in registros:
                tbl_cliente.delete(registro)
            for documento in coleccion.find():
                tbl_cliente.insert('','end',text=documento["_id"],values=(documento["_id"], documento["Nombre"] ,documento["Apellidos"],documento["Nacionalidad"],documento["Provincia"],documento["correo"],documento["Direccion"],documento["Genero"]))
            #cliente.server_info()
            #print("Conexion a Mongo exitosa")
            
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo extendido"+errorTiempo)
        except pymongo.errors.ConectionFailure as errorConexion:
            print("Fallo al conectarse a mongodb"+errorConexion) 

    mostrardatos()

    #Funcion crear registro
    def crearRegistro():
        global idCliente
        if len(nombreCliente.get())!=0 and len(apellidosCliente.get())!=0 and len(nacionalidadCliente.get())!=0 and len(provinciaCliente.get())!=0 and len(correoCliente.get())!=0 and len(direccionCliente.get())!=0 and len(generoCliente.get())!=0:
                documento={"Nombre": nombreCliente.get(),
                            "Apellidos": apellidosCliente.get(),
                            "Nacionalidad": nacionalidadCliente.get(),
                            "Provincia" : provinciaCliente.get(),
                            "correo": correoCliente.get(), 
                            "Direccion": direccionCliente.get(),
                            "Genero": generoCliente.get(),} 
                coleccion.insert_one(documento)
                refrescar()
                idCliente = ""
        else:
            messagebox.showerror(message="Los campos no pueden estar vacios")
        mostrardatos()

    # Limpiar Campos
    def limpiarCampos():
                nombreCliente.set('')
                apellidosCliente.set('')
                nacionalidadCliente.set('')
                provinciaCliente.set('')
                correoCliente.set('')
                direccionCliente.set('')
                generoCliente.set('')

    #Refrescar Valores y setear en modo creacion
    def refrescar():
            global idCliente
            limpiarCampos()
            idCliente = ""
            IdCliente.set("Modo Creacion")

    #Eliminar Regisrtro
    def eliminarRegistro():
        global idCliente
        global coleccion
        if (idCliente!=""):
            coleccion.delete_one({'_id': ObjectId(idCliente)})
            mostrardatos()
            messagebox.showinfo(title="Eliminado",message='Cliente con el ID:'+ str(idCliente))
            refrescar()
        else:
                messagebox.showerror(message='Debe seleccionar un registro')
    #Actualizar Regisrtro

    def actualizarRegistro():
        if len(nombreCliente.get())!=0 and len(apellidosCliente.get())!=0 and len(nacionalidadCliente.get())!=0 and len(provinciaCliente.get())!=0 and len(correoCliente.get())!=0 and len(direccionCliente.get())!=0 and len(generoCliente.get())!=0:
            global idCliente
            global coleccion
            filter = { '_id': ObjectId(idCliente) }
            
            newvalues = { "$set": { "NombreCliente": nombreCliente.get(),
                            "ApellidosCliente": apellidosCliente.get(),
                            "NacionalidadCliente": nacionalidadCliente.get(),
                            "ProvinciaCliente" : provinciaCliente.get(),
                            "CorreoCliente": correoCliente.get(), 
                            "Direccion": direccionCliente.get(),
                            "GeneroCliente": generoCliente.get()}}

            coleccion.update_one(filter, newvalues)
            mostrardatos()
            refrescar()
        else:
            messagebox.showerror(message='Los campos no pueden estar vacios')


    #Ubicar la tabla en el frame
    tbl_cliente.place(x=750,y=99, height=780)
    btn_Ingresar = Button(f_Clientes,text="Agregar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=146,y=799, width=100,height=50)
    btn_EjecutarCambios = Button(f_Clientes,text="Refrescar",command=refrescar, bg ="#7CA3EF", font=("",15)).place(x=428, y=799, width=100,height=50)
    btn_Refrescar = Button(f_Clientes,text="Editar", command=actualizarRegistro, bg ="#AAC213", font=("",15)).place(x=146,y=880, width=100,height=50)
    btn_Eliminar = Button(f_Clientes,text="Eliminar", command = eliminarRegistro, bg ="#F58585", font=("",15)).place(x=428,y=880, width=100,height=50)
     
# Estilo del menu principal
lbl_Floristeria = Label(f_menuPrincipal, text = "Floristeria Flores del Norte", bg ="#BCCCF3", font=("",44)).place(x=415,y=123)
lbl_Bienvenida = Label(f_menuPrincipal, text ="Bienvenid@ "+MONGO_USERNAME, bg ="#BCCCF3", font=("",35)).place(x=550,y=202)



#Obtener la ruta relativa en Windows
def obtenerImagen(nombre, tipo):
    script_dir = os.path.dirname(__file__) #Carpeta Actual
    rel_path = "../Imagenes/" #Relative path
    abs_file_path = os.path.join(script_dir, rel_path) #Concatenacion de los 2
    current_file = nombre +"."+tipo 
    ImagenArticulo = abs_file_path+current_file
    return  ImagenArticulo

#Cambiar tamaño de la imagen
def cambiarTamano(ancho,altura,imagen):
     resized_img = imagen.resize((ancho, altura), Image.LANCZOS)
     return resized_img

#Imagenes y botones
img = Image.open(obtenerImagen("Articulo","jpg"))
imgobj_Articulo = ImageTk.PhotoImage(cambiarTamano(157,157,img))
btn_Articulo = Button(f_menuPrincipal, text="Articulos", image=imgobj_Articulo, compound= TOP, font=("",15), command=openWd_Articulo).place(x=183,y=321, width=232,height=232)

img = Image.open(obtenerImagen("Proveedores","jpg"))
imgobj_Proveedores = ImageTk.PhotoImage(cambiarTamano(157,157,img))
btn_Proveedores = Button(f_menuPrincipal, text="Proveedores", image=imgobj_Proveedores, compound= TOP, font=("",15), command=openWd_Proveedor ).place(x=604,y=321, width=232,height=232)

img = Image.open(obtenerImagen("Clientes","jpg"))
imgobj_Clientes = ImageTk.PhotoImage(cambiarTamano(157,157,img))
btn_Clientes = Button(f_menuPrincipal, text="Clientes", image=imgobj_Clientes, compound= TOP, font=("",15), command=openwd_Cliente).place(x=1025,y=321, width=232,height=232)

img = Image.open(obtenerImagen("Sucursales","jpg"))
imgobj_Sucursales = ImageTk.PhotoImage(cambiarTamano(157,157,img))
btn_Sucursales = Button(f_menuPrincipal, text="Sucursales", image=imgobj_Sucursales, compound= TOP, font=("",15)).place(x=393,y=597, width=232,height=232)

img = Image.open(obtenerImagen("Facturas","png"))
imgobj_Facturas = ImageTk.PhotoImage(cambiarTamano(157,157,img))
btn_Facturas = Button(f_menuPrincipal, text="Facturas", image=imgobj_Facturas, compound= TOP, font=("",15)).place(x=814,y=597, width=232,height=232)






def on_closing():
    if messagebox.askokcancel("Salir", "Deseas salir del programa?"):
        menuPrincipal.destroy()

menuPrincipal.protocol("WM_DELETE_WINDOW", on_closing)

mainloop()

