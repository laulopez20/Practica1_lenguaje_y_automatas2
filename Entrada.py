
#ENTRADA DE DATOS

"""
print("INGRESA TU NOMBRE: ")
nombre =input()
print(type(nombre))
palabras=nombre.split(" ")
nombre=nombre.capitalize()
nombre= nombre.replace(" ","-")

for palabra in palabras:
    print(palabra.capitalize())

#nombre = nombre.lower()  # Convertir todo a minúsculas
#nombre = nombre.title()  # Capitalizar cada palabra


#print("HOLA: " + nombre)
"""
#Ingresa tu nombre y convierte la primera letra en mayuscula de cada nombre
print("INGRESA TU NOMBRE: ")
nombre =input()
texto = ' '.join(word.capitalize() for word in nombre.split())
print("HOLA: ",texto)



