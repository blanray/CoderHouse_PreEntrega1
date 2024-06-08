import json

def crearBase():
    try:
        with open('baseDatos.json', 'r') as archivoDatos:
            print("La base ya existe")
    except FileNotFoundError:

        miBaseVacia = {}

        with open('baseDatos.json', 'w') as archivoDatos:
            json.dump(miBaseVacia, archivoDatos, ensure_ascii=False, indent=2)
            print("La base se creó exitosamente")

    except Exception as error:
        with open('baseDatos.json', 'w') as archivoDatos:
            print("Ocurrio un error:", type(error).__name__) 

def abrirBase():
    try:
        with open('baseDatos.json', 'r') as archivoDatos:
            datos = json.load(archivoDatos)
        return datos
    except Exception as error:
        print("Ocurrio un error:", type(error).__name__) 


def leerBase():
    try:

        datos = abrirBase()

        if len(datos)== 0:
            print("La base está vacía")
        else:
            print("Usuario / Password")
            for key, value in datos.items():
                print(f"{key}: {value}")

        return datos
    except Exception as error:
        print("Ocurrio un error:", type(error).__name__) 


def alta():

    try:

        datos = abrirBase()

        miUsuario = input("Ingrese nombre usuario: ")
        miPass = input("Ingrese la contraseña: ")

        datos[miUsuario]= miPass

        with open('baseDatos.json', 'w') as archivoDatos:
            json.dump(datos, archivoDatos, ensure_ascii=False, indent=2)
        
        print("Registro agregado exitosamente")
    
    except Exception as error:
        print("Ocurrio un error:", type(error).__name__) 

def login():
    pass

try:

    opcion = 9

    while opcion!=0:
        print("1- Crear base")
        print("2- Leer base")
        print("3- Ingresar Usuario a la base")
        print("4- Login")
        print("0- Salir")

        opcion = int(input("Ingrese la opcion deseada:"))

        if opcion == 1:
           crearBase()
        elif opcion == 2:
           leerBase()
        elif opcion == 3:
           alta()
        elif opcion == 4:
           login()
        elif opcion == 0:
           break
        else:
           print(f"Tecla {opcion} incorrecta!!!!")
                 
except Exception as error:
    print("Ocurrio el error:", type(error).__name__) 


    
