class Vehiculo:

    def __init__(self, tipo, marca, modelo, precio, correo, contrasena):
        self._tipo = tipo
        self._marca = marca
        self._modelo = modelo
        self._precio = precio
        self._correo = correo
        self._contrasena = contrasena

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    def registrar_vehiculo(self):
        correo = input("Ingrese el correo del usuario:")
        contrasena = input("Ingrese la contraseña del usuario: ")
        tipo = input("Ingrese el tipo del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        precio = input(f"Ingrese el precio del vehiculo: ")

    def imprimir_registro(self):
        print(f"Tipo: {self._tipo} Marca: {self._marca} Modelo: {self._modelo} Precio: {self._precio} Correo: {self._correo} Contraseña: {self._contrasena}")
