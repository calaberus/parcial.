class Persona:
    def _init_(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad

    # Método para establecer el nombre
    def establecer_nombre(self, nombre):
        self.nombre = nombre

    # Método para obtener el nombre
    def obtener_nombre(self):
        return self.nombre

    # Método para establecer la edad
    def establecer_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser negativa.")

    # Método para obtener la edad
    def obtener_edad(self):
        return self.edad