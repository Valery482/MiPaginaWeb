print("¡Hola, este es mi primer programa en Python!")

x = 10
y = 3.5
nombre = "Valerie"
print(x + y)
print("Mi nombre es " + nombre)

# Paso 2: Condicionales y bucles
num = int(input("Ingresa un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

for i in [1, 2, 3, 4, 5]:
    print(f"El cuadrado de {i} es {i**2}")

estudiantes = ["Ana", "Luis", "Juan"]
for e in estudiantes:
    print("Estudiante:", e)

contacto = {"nombre": "Ana", "correo": "ana@mail.com"}
for clave, valor in contacto.items():
    print(clave, ":", valor)

# Paso 4: Calculadora básica
print("Calculadora básica")
a = int(input("Número 1: "))
b = int(input("Número 2: "))
print("Suma:", a+b)
print("Resta:", a-b)
print("Multiplicación:", a*b)
if b == 0:
    print("Division entre cero no es posible")
else:
    print("División:", a/b)

import random
secreto = random.randint(1, 10)
intento = 0
while intento != secreto:
    intento = int(input("Adivina el número (1-10): "))
    if intento < secreto:
        print("Es mayor")
    elif intento > secreto:
        print("Es menor")
print("¡Correcto!")
