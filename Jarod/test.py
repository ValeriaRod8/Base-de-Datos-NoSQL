import pymongo

mongoHost = "localhost"
mongoPuerto = "27017"
mongoTiempoFuera = 1000
mongoUri = "mongodb://" + mongoHost + ":" + mongoPuerto
print(mongoUri)
mongoBaseDatos = "Empresa"
mongoColleccion = "Empleados"

try:
    cliente = pymongo.MongoClient(mongoUri, serverSelectionTimeoutMS=mongoTiempoFuera)
    basedatos = cliente[mongoBaseDatos]
    coleccion = basedatos[mongoColleccion]
    cliente.server_info()
    print("conexion a Mongo Exitosa")
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo extendido" + str(errorTiempo))
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)

for i in coleccion.find():
    print(i)
