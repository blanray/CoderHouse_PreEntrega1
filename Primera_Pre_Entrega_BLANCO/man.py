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

def leerBase():
    try:
        with open('baseDatos.json', 'r') as archivoDatos:
            datos = json.load(archivoDatos)

        if len(datos)== 0:
            print("La base está vacía")
        else:
            for key, value in datos.items():
                print(f"Clave: {key}")
                print(f"Valor: {value}")

    except Exception as error:
        print("Ocurrio un error:", type(error).__name__) 


def alta():

    with open('tu_archivo.json', 'w') as jf: 
        json.dump(data, jf, ensure_ascii=False, indent=2)
    
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


    
