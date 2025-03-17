# print("Hello, World!")

"""
if 5 > 2:
    print("Is greater")
""" 
"""
if 5>2:
    print("Is greater")
if 5>2:
    print("Five is greater than two") """

"""
x= 5
y= "Hello World"

print(x)
print(y) """

"""
x= 5
y= "Toto"

print(type(x))
print(type(y)) """

"""
x, y, z= "Orange", "Banane", "Cherry"

print(x)
print(y)
print(z) """

"""
x= y= z= "Glue"

print(x)
print(y)
print(z) """

"""
fruits = ["apple", "banana", "kiwi"]
x, y, z= fruits

print(x)
print(y)
print(z) """

"""
x= "Python"
y= "c'est"
z= "cool!"

print(x, y, z) """

"""
x= 5
y= 10

print(x+y) """

"""
x= 10
y= "Guillaume"

print(x, y) """

"""
x= "incroyable!"

def myfunc():
    print("Python est " + x)

myfunc() """

"""
x= "incroyable!"

def myfunc():
    x= "super!"
    print("Python est " + x)

myfunc()

print("Python est " + x) """

"""
x= "incroyable!"

def myfunc():
    global x
    x= "super!"

myfunc()

print("Python est " + x) """

"""
x= True

print(type(x)) """


"""
x= 1

a= float(x)

print(a)
print(type(a)) """

"""
import random

print(random.randrange(1, 10)) """

"""
a = "Hello comment ça va ?"

print(a[2]) """

"""
for x in "cherry":
    print(x) """

"""
x= "Bonjour"

print(len(x)) """

"""
texte= "Je suis Guillaume et j'adore le padel"

print("Guillaume" in texte)"""

"""
texte= "Voici un texte pour l'exemple"

if "pour" in texte:
    print("Oui, 'pour' est présent") """

"""
texte= "Il fait pas beau aujourd'hui"

if "neige" not in texte:
    print("'neige' n est pas présent") """

"""
x= "Guillaume"

print(x[4:]) """

"""
x = "Fromage"
print(x[-5:-2]) """

"""
x= "toto"

print(x.upper()) """

"""
x= "Ce soir je vais manger des pates"

print(x.replace("e", "z")) """

"""
x= "Je me sens bien"

print(x.split(" ")) """

"""
x= 25
texte= f"Je viens d'avoir {x} ans"

print(texte) """

"""
x= 40
y= 2
texte= f"Le prix de une \"pomme\" est de {x} euros mais pour deux pommes c'est {x*y} euros"

print(texte) """

"""
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") """

"""
x = 200
print(isinstance(x, int)) """



#Convertiseur Celsius/Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) +32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) (5/9)

print("Celsius ou Fahrenheit :")
unite= input().lower()

print("Entrez la température à convertir :")
temperature= float(input())

if unite == "celsius":
    result= celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {result}°F")
elif unite == "fahrenheit":
    result= fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F = {result}°C")
else:
    print("Unité invalide")