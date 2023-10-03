# 1 CONDICION IF-ELSE

"""
'SON LAS 7 DE LA NOCHE Y YA ME QUIERO IR'
SI ENCUENTRA EL NUMERO 7 Y ES MENOR A 8
IMPRIMIR EL NUMERO 7 CONVERTIDO A INT
Y EL TEXTO, ' ES HORA DE IRNOS SON LAS : '7'
"""
texto = "son las 7 de la noche y ya me quiero ir"
numero = "7"
if numero in texto and int(numero) < 8:
    print(f"Es hora de irnos, son las: {numero}")
else:
    print("No se cumple la condición")

#2 USO DE ESTRUCTURA DE DATOS
"""
#0 CREAR UNA LISTA : 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
#2. CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
#4.CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS
   NUMEROS UNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET 
   MAXIMO VALOR, MINIMO VALOR
#5. IMPRIMIR LAS ESTADISTICAS"""
#0.CREAR UNA LISTA: 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
numeros=[1,2,5,3,2,3,3,6,10,8,9]
print(numeros)
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
convertirSet=set(numeros)
print(convertirSet)
#2.CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
sumaLista=sum(numeros)
print(sumaLista)
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
sumaSet= sum(convertirSet)
print(sumaSet)
#4.CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS
#NUMEROS UNICOS, SUMA TOTAL LISTA,VALOR SUMA TOTAL SET
#MAXIMO , MINIMO VALOR
estadisticas = {
    "Numeros Unicos": len(convertirSet),
    "Suma Total Lista": sumaLista,
    "Suma Total Set": sumaSet,
    "Maximo Valor": max(numeros),
    "Minimo Valor": min(numeros)
}
# 4.Imprimir las estadísticas
for clave, valor in estadisticas.items():
    print(f"{clave}: {valor}")

#3 ENTRADA DE DATOS
#convertir el nombre ingresado empezando cada palabra por mayuscula, independientemente de como lo hayan ingresado
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


