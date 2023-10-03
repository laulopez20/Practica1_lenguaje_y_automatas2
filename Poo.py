#CLASES Y OBJETOS
#Definimos la clase alumno
class Alumno:
    def __init__(self, nombre, edad, numero_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.numero_estudiante = numero_estudiante

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y mi número de estudiante es {self.numero_estudiante}.")

# Crear una instancia de la clase "Alumno"
alumno1 = Alumno("Emilio", 21, "L20230236")

# Acceder a los atributos y métodos de la instancia
print(alumno1.nombre)
print(alumno1.edad)
print(alumno1.numero_estudiante)
alumno1.presentarse()


# CLASES Y OBJETOS

# CREANDO LA CLASE
class Alumno:
    def __init__(self, numControl, nombre, edad):
        self.numControl = numControl
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.numControl}: {self.nombre}, edad: {self.edad}"


# CLEANDO EL OBJETO
alumnoEmir = Alumno("20232245", "emir", 20)
alumnoROXEL = Alumno("22230979", "ROXEL", 21)
alumnoVictor = Alumno("20230221", "VICTOR", 20)

print(alumnoEmir)
print(alumnoROXEL)
print(alumnoVictor)