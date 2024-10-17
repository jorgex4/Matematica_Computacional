#Segunda clase matematica computacional
#Generar una lista aleatoria de 10 numeros entre 1 y 100
import random
num = [random.randint(1,100) for i in range(10)]
print(f"Los numeros generados en una lista de 10 son: {num}")

#Contar el numero de palabras de un texto
oracion= "Hola  buen dia querido compañero"
palabras = oracion.replace(",","").split()
cont=0
for i in palabras:
     cont +=1
print(f"El texto tiene {cont} palabras")
print(palabras)

#Ingresar un numero y si es par o impar 
numero = int(input("Usuario porfavor ingrese un numero "))
if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero,"es impar.") 

#Ingrese su edad y si es mayor de edad (+18), niño(-18), adulto mayor(+70)

edad = int(input("Usuario porfavor ingrese su edad: "))
if edad < 18:
    print("Eres un niño.")
elif 18 <= edad <= 69:
    print("Eres mayor de edad.")
else:
    print("Eres un adulto mayor.")