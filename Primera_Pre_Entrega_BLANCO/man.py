import json
import msvcrt
import os


def pausa():

    print("Presione barra espacadora para continuar...")
    key = None
    while key != ' ':
        key = msvcrt.getwch()
        os.system("cls")
        

def crearBase():
    try:
        with open('baseDatos.json', 'r') as archivoDatos:
            print("\n----- La base ya existe ----\n")
    except FileNotFoundError:

        miBaseVacia = {}

        with open('baseDatos.json', 'w') as archivoDatos:
            json.dump(miBaseVacia, archivoDatos, ensure_ascii=False, indent=2)
            print("\n---- La base se creó exitosamente ----\n")

    except Exception as error:
        with open('baseDatos.json', 'w') as archivoDatos:
            print("\n---- Ocurrio un error:", type(error).__name__)
    finally:
        pausa()

def abrirBase():
    try:
        with open('baseDatos.json', 'r') as archivoDatos:
            datos = json.load(archivoDatos)
        return datos
    except Exception as error:
        print("\n---- Ocurrio un error:", type(error).__name__) 


def leerBase():
    try:

        datos = abrirBase()

        if len(datos)== 0:
            print("\n---- La base está vacía ----\n")
        else:
            print("Usuario / Password")
            for key, value in datos.items():
                print(f"{key}: {value}")

        return datos
    except Exception as error:
        print("\n---- Ocurrio un error:", type(error).__name__) 
    finally:
        pausa()

def alta():

    try:

        datos = abrirBase()

        encontrado = False
        miUsuario = input("\n - Ingrese nombre usuario: ")
        miPass = input("\n  -- Ingrese la contraseña: ")

        for key in datos:
            if miUsuario == key:
                print("\n---- Error! El usuario ya existe! ----\n")
                encontrado = True
                break
        
        if not(encontrado):
            datos[miUsuario]= miPass
            with open('baseDatos.json', 'w') as archivoDatos:
                json.dump(datos, archivoDatos, ensure_ascii=False, indent=2)

            print("\n----- Registro agregado exitosamente ----\n")
    
    except Exception as error:
        print("\n---- Ocurrio un error:", type(error).__name__) 
    finally:
        pausa()

def login():
    try:

        datos = abrirBase()

        passTemp = ""
        encontrado = False

        if len(datos)== 0:
            print("\n---- La base está vacía ----\n")
        else:
            miUsuario = input("\n - Ingrese nombre usuario: ")
            miPass = input("\n  -- Ingrese la contraseña: ")

            for key, value in datos.items():
                if key == miUsuario:
                    encontrado = True
                    passTemp = value
                    break

            if encontrado:
                if passTemp == miPass:
                        print("\n---- Login exitoso ----\n")
                else:
                        print("\n---- Contraseña incorrecta ----\n")
            else:
                print("\n----- El usuario no existe ----\n")

    except Exception as error:
        print("\n---- Ocurrio un error:", type(error).__name__) 
    finally:
        pausa()

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
    print("\n---- Ocurrio el error:", type(error).__name__) 
