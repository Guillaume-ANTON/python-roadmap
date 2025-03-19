"""
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") """

"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") """

"""
i = 1
while i < 6:
  print(i)
  i += 1 """

"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 """

"""
for x in "banana":
  print(x) """

"""
for x in range(6):
  if x == 6: break
  print(x)
else:
  print("Finally finished!") """

"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) """

"""
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits) """

"""
cars= ["Toyota", "Renault", "Nissan", "BMW"]

for x in cars:
  print(x) """

"""
class Myclass:
    x= 5

p1= Myclass()

print(p1.x) """

"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) """

"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) """

"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome() """

# Créer un classe Voiture avec des méthodes : 

class Voiture:
    def __init__(self, marque, modele, annee, vitessemax):
        self.marque= marque
        self.modele= modele
        self.annee= annee
        self.vitesseactuel= 160
        self.vitessemax= vitessemax
    
    def Afficher_infos(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Vitesse actuelle: {self.vitesseactuel} km/h, Vitesse max: {self.vitessemax} km/h")

    def Accelerer(self, valeur):
        if self.vitesseactuel + valeur > self.vitessemax:
            self.vitesseactuel = self.vitessemax
        else:
            self.vitesseactuel += valeur
        print(f"La voiture accélère à {self.vitesseactuel} km/h")
    
    def Freiner(self, valeur):
        if self.vitesseactuel + valeur < 0:
            self.vitesseactuel = 0
        else:
            self.vitesseactuel -= valeur
        print(f"La voiture ralentit à {self.vitesseactuel} km/h")

    def Klaxon(self):
        print("bip, bip")

voiture1= Voiture("Honda", "Civic", 2020, 200)
voiture1.Afficher_infos()
voiture1.Accelerer(50)
voiture1.Freiner(20)
voiture1.Klaxon()