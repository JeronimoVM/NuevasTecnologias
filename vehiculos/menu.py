from Vehiculo import Vehiculo
from Marca import Marca

marca = Marca(tipo=None,
              marca=None,
              modelo=None,
              precio=None,
              correo=None, 
              contrasena=None,
              seguridad=None)

def menuApp():
    print("Inicialice con 1: ")

    init = int(input("Escriba 1: "))

    while init != 0:

        print(
            "\n Seleccione 1 para registrar vehículo\n",
            "Seleccione 2 para Iniciar sesión\n",
            "Seleccion 3 para salir\n",
        )

        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            marca.registrar_vehiculo()
        elif opc == 2:
            marca.appMarca()
        elif opc == 3:
            print("Salir")
            init = 0

menuApp()
