# Funciones:
x = 1
#Funciones con parametros finitos y keywords
def saludar(nombre,edad):
    print("Hola " + nombre + ", EDAD: " + str(edad))

saludar("Emilio",21)
saludar("Francisco",21)

if x==1:
    saludar("Daniel",16)

while x<=6:
    saludar("Carolina",16)
    x+=1
# Funciones con N parametros
def asistencia(*alumnos):
    for alumno in alumnos:
        print("Asistio: " + alumno)

asistencia("Emilio", "Francisco")
saludar(nombre = "Luis", edad = 16)
saludar(edad = 16, nombre = "Luis")

#