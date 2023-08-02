from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymongo

#Conexion con Mongo Compas
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
mongo_uri="mongodb://"+ MONGO_HOST+":"+ MONGO_PUERTO
cliente=pymongo.MongoClient(mongo_uri,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)


MONGO_BASEDATOS="Floristeria"
MONGO_COLECCION=""
basedatos=cliente[MONGO_BASEDATOS]
coleccion=""

# Variables para determinar la apertura de alguna ventana
ventanaArticuloAbierta = False


#Funcion que selecciona la coleccion
def seleccionCollecion(parColeccion):
    global coleccion
    global basedatos
    coleccion=basedatos[parColeccion]


 
# creacion de la ventana main
menuPrincipal = Tk()
 
menuPrincipal.geometry("200x200")



def openWd_Articulo():
    
    #Obtener la collecion a trabjar
    seleccionCollecion("Articulos")
    global coleccion

    wd_Articulos = Toplevel(menuPrincipal)
    wd_Articulos.title('Floristeria') #Nombre de la pagina
    #wd_Articulos.iconbitmap('xxxx.ico') #Ver icono en ese momento ------


    f_Articulos = Frame(wd_Articulos)
    f_Articulos.config(width = 1440, 
                        heigh = 1024, 
                        bg ="#CBEEA8" )

    f_Articulos.pack(fill="both",expand="True")

    #Variables de los text fields
    nombreArticulo = StringVar()
    tipoArticulo = StringVar()
    sucursalArticulo = StringVar()
    descripcionArticulo = StringVar()
    precioArticulo = StringVar()
    cantidadArticulo = StringVar()

    #Diseño de los widgets en wd_Articulos

    #Labels, Text entries,  
    lbl_NombreArticulo = Label(f_Articulos, text = "Nombre del Articulo", bg ="#CBEEA8", font=("",15)).place(x=144,y=176)
    txt_NombreArticulo = Entry(f_Articulos,font=("",15),textvariable=nombreArticulo).place(x=144,y=206, width=385,height=36)

    lbl_TipoArticulo = Label(f_Articulos, text = "Tipo de Articulo", bg ="#CBEEA8", font=("",15)).place(x=144,y=265)
    txt_TipoArticulo = Entry(f_Articulos,font=("",15),textvariable=tipoArticulo).place(x=144,y=290, width=385,height=36)

    lbl_SucursalArticulo = Label(f_Articulos, text = "Sucursal", bg ="#CBEEA8", font=("",15)).place(x=144,y=354)
    txt_SucursalArticulo = Entry(f_Articulos,font=("",15),textvariable=sucursalArticulo).place(x=144,y=379, width=385,height=36)

    lbl_DescripcionArticulo = Label(f_Articulos, text = "Descripcion", bg ="#CBEEA8", font=("",15)).place(x=144,y= 443)
    txt_DescripcionArticulo  = Entry(f_Articulos,font=("",15), textvariable=descripcionArticulo).place(x=144,y=473,width=385,height=36)

    lbl_PrecioArticulo = Label(f_Articulos, text = "Precio", bg ="#CBEEA8", font=("",15)).place(x=144,y=532)
    txt_PrecioArticulo = Entry(f_Articulos,font=("",15), textvariable=precioArticulo ).place(x=144,y=562, width=385,height=36)

    lbl_CantidadArticulo = Label(f_Articulos, text = "Cantidad", bg ="#CBEEA8", font=("",15)).place(x=144,y=621)
    txt_CantidadArticulo = Entry(f_Articulos,font=("",15), textvariable=cantidadArticulo).place(x=144,y=651, width=385,height=36)


    # Tabla
    tbl_ArticuloEstilo = ttk.Style()
    tbl_ArticuloEstilo.theme_use('clam')
    tbl_ArticuloEstilo.configure('tbl_Articulosview.Heading', background="#D9D9D9")

    # Tabla Header
    tbl_Articulos= ttk.Treeview(f_Articulos, column=("c1", "c2","c3","c4","c5","c6","c7"), show= 'headings', height= 8)
    
    tbl_Articulos.column("# 1",anchor= CENTER, width=50)
    tbl_Articulos.heading("# 1", text= "Id")
    tbl_Articulos.column("# 2",anchor= CENTER)
    tbl_Articulos.heading("# 2", text= "Nombre Articulo")
    tbl_Articulos.column("# 3", anchor= CENTER)
    tbl_Articulos.heading("# 3", text= "Tipo Articulo")
    tbl_Articulos.column("# 4",anchor=CENTER)
    tbl_Articulos.heading("# 4", text= "Sucursal")
    tbl_Articulos.column("# 5",anchor=CENTER)
    tbl_Articulos.heading("# 5", text= "Descripcion")
    tbl_Articulos.column("# 6",anchor=CENTER)
    tbl_Articulos.heading("# 6", text= "Precio")
    tbl_Articulos.column("# 7",anchor=CENTER)
    tbl_Articulos.heading("# 7", text= "Cantidad")

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
            cliente.close()
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo extendido"+errorTiempo)
        except pymongo.errors.ConectionFailure as errorConexion:
            print("Fallo al conectarse a mongodb"+errorConexion) 
    
    mostrardatos()

    #Funcion crear registro
    def crearRegistro():
        if len(nombreArticulo.get())!=0 and len(tipoArticulo.get())!=0 and len(sucursalArticulo.get())!=0 and len(descripcionArticulo.get())!=0 and len(precioArticulo.get())!=0 and len(cantidadArticulo.get())!=0:

                documento={"NombreArticulo": nombreArticulo.get(),
                           "IdTipoArticulo": int(tipoArticulo.get()),
                           "_idSucursal": int(sucursalArticulo.get()),
                           "Descripcion" : descripcionArticulo.get(),
                           "PrecioUnitario":int(precioArticulo.get()), 
                           "Cantidad":int(cantidadArticulo.get())} 
                coleccion.insert(documento)
                nombreArticulo.set('')
                tipoArticulo.set('')
                sucursalArticulo.set('')
                descripcionArticulo.set('')
                precioArticulo.set('')
                cantidadArticulo.set('')
        else:
            messagebox.showerror(message="Los campos no pueden estar vacios")
        mostrardatos()                 
    

    #Ubicar la tabla en el frame
    tbl_Articulos.place(x=656,y=99, height=827)


    #Funcion del btn_Agregar
    def crearArticulo():
        nombreArticulo.set("")

    btn_Ingresar = Button(f_Articulos,text="Ingresar", command=crearRegistro, bg ="#79C397", font=("",15)).place(x=144,y=738, width=100,height=50)
    btn_EjecutarCambios = Button(f_Articulos,text="Actualizar", bg ="#7CA3EF", font=("",15)).place(x=428,y=738, width=100,height=50)



# Estilo del menu principal
label = Label(menuPrincipal,
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = Button(menuPrincipal,
             text ="Click to open a new window",
             command = openWd_Articulo)
btn.pack(pady = 10)

mainloop()

