#operadores numericos

a=10
b=3
print("suma:", a + b )
print("resta:", a - b)
print("multiplicación:", a * b)
print("potenciación:", a ** b)
print("división:", a / b)
print("Parte entera de la division:", a // b)
print("Módulo:", a % b)

a /= 2
print(a)

#PEMDAS
#P -> Paréntesis
#E -> Exponenciación
#M -> Multiplicación
#D -> División
#A -> Adición
#S -> Sustracción

operation_1  = 2 + 3 * 4
operation_2  = (2 + 3) * 4
print(operation_1)
print(operation_2)
operation_3 = (2+3) * (4**2)/ 8 - 1
print(operation_3)