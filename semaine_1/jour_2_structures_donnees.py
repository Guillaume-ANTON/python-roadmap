"""
maliste= ["Jaune", "Rouge", "Vert", "Rouge"]

print(len(maliste)) """

"""
mylist = ["apple", 43, "cherry"]
print(type(mylist)) """

"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-2]) """

"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) """

"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) """

"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) """

"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) """

"""
list= ["Guillaume", "Kevin", "Julie"]
if "Guillaume" in list:
    print("Guillaume est dans la liste") """

"""
thislist= ["pomme", "orange", "kiwi"]
thislist[1]= "poire"
print(thislist)"""

"""
thislist= ["pomme", "orange", "kiwi", "poire", "mangue"]
thislist[1:3]= ["cerise", "menthe"]
print(thislist) """

"""
thislist= ["pomme", "orange", "kiwi"]
thislist.insert(2,"poire")
print(thislist) """

"""
thislist=["pomme", "poire", "orange"]
thislist.append("jaune")
print(thislist) """

"""
thislist= ["pomme", "poire", "orange"]
couleurs= ["rouge", "jaune", "marron"]
thislist.extend(couleurs)
print(thislist) """

"""
thislist= ["pomme", "poire", "orange"]
thislist.remove("pomme")
print(thislist) """

"""
thislist= ["pomme", "poire", "orange"]
thislist.pop(1)
print(thislist) """

"""
thislist= ["pomme", "poire", "orange"]
del thislist
print(thislist) """

"""
thislist= ["pomme", "poire", "orange"]
thislist.clear()
print(thislist) """

"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) """

"""
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) """

"""
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 """

"""
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] """

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) """

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

print(newlist) """

"""
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) """

"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) """

"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) """

"""
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) """

"""
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)"""

"""
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print(type(x))"""

"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) """

"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red) """

"""
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) """

"""
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) """

"""
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) """

"""
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) """

"""
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) """

"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) """

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) """

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) """

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) """

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) """

"""
thisdict = {
  "marque": "Ford",
  "modele": "Mustang",
  "annee": 1964
}
print(thisdict) """

"""
thisdict = {
  "marque": "Ford",
  "modele": "Mustang",
  "annee": 1964
}
x= thisdict.get("modele")
print(x) """

"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print(car.get('color')) """

"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change """

"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) """


# Exercice : Filtrer les  nombres pairs d'une liste

mesnombres= [3, 12, 46, 50, 33, 109, 1200, 2]
mesnombrespairs= []

for x in mesnombres:
    if x % 2 ==0:
        mesnombrespairs.append(x)
    
mesnombrespairs.sort()
print(mesnombrespairs)