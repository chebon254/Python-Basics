import random
import module_test # Naming a module as mx or any name
from traceback import print_tb

# First Python Line of Code
print ("Hello World")

# Indentation
if 5 > 2:
    print ("Five is greater than two")

# Comments
""" For Long comments that will take more than one line, hence we use three quotes on both sides """

print ("\n")
# Variables
x = 5
y = "Say Hi!"

print (x)
print (y)

print ("\n")

# Casting - to specify data type of a variable

a = int(3)
b = str(6)
c = float(3)
d = "Chebon Kibet"

# Get Type

print (type(c))
print (d)
print (type(d))

print ("\n")

# Multiple Value multiple variables

e, f, g = "Love", "Chebon", "Chebet"

print (e)
print (f)
print (g)

print ("\n")
 # Unpacking

fruits = ["Oranges", "Apples", "Bananas"];

i, j, k = fruits

print (i)
print (j)
print (k)


print ("How sweet are " + k + " compared to " + j + " and " + i)

print ("\n")

def test():
    print ("How sweet are " + k + " compared to " + j + " and " + i)

print ("Print Information from function test:")
test()


print ("\n")
print ("Random Number between 1,000 and 1000,000")
# Random Number
print (random.randrange(1000, 1000000))

print ("\n")

name = "Chebon Kibet"
print (name[2])
print ("\n")
for p in "Chebon":
    print (p)

print (len(name))

print ("\n")
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

print("expensive" not in txt)

print (txt[4:16])


print ("\n")

# String Formatting

year_of_birth = 1998
user_info = "Chebon Kibet Kelvin was born in the year: {}"

print (user_info.format(year_of_birth))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


print ("\n")
# Boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)

long_num = 100
short_num = 200

if short_num > long_num:
  print("Short number is greater than Long number")
else:
  print("Short number is not greater than Long number")

print ("\n")

class myclass():
  def __len__(self):
    return 10

myobj = myclass()
print(bool(myobj))

print (3 % 2 )


names_tupple = ("Chebon", "Mercy", "Nganga", "Kelvin", "Alan", "Koech", "kimosop", "Emmanuel", "Chepchieng");

print (type(fruits))
print (type(names_tupple))


print ("\n")
[print(x) for x in fruits]
[print(x) for x in names_tupple]

print ("\n")
# List Comprehension newlist = [expression for item in iterable if condition == True]
new_list = []

for x in names_tupple:
    if "e" in x:
        new_list.append(x)

print (new_list)

print ("\n")

new_lists = [x.upper() for x in names_tupple if "e" in x]

print (new_lists)

print ("\n")

# Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print (thisdict)
print (thisdict["brand"])

car_model = thisdict.get("model")
print (car_model)

print ("\n")
car = {
  "brand": "Corolla",
  "model": "Toyota",
  "year": 1982
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

print ("\n")



# IF loop
a_num = 200
b_num = 600
c_num = 500
if a_num > b_num and c_num > a_num:
  print("Not true")
elif a_num < b_num and c_num > a_num:
  print("Both conditions are True")
else:
  print("Its okay")

print ("\n")

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print ("\n")

def user_names(first_name):
  print("Welcome " + first_name + ", to our school.")

user_names("John Kibet")
user_names("Chebon Kelvin")
user_names("alan kimutai")

print ("\n")


# CLASSES & OBJECTS
class MyClass:
  x = 5

object_one = MyClass()

print(object_one.x)


print("\n")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greeting(self):
    print("Hello your name is " + self.name)

user_one = Person("Chebon", 23)


print(user_one.name)
print(user_one.age)

user_one.greeting()

print("\n")

# Inheritance

class Student(Person):
  pass

user_two = Student("Mercy", 19)
user_two.greeting()


class Use(Person):
  def __init__(self, name, age, year):
    super().__init__(name, age)
    self.gradyear = year

  def welcome(self):
    print("Welcome, ", self.name, " aged ", self.age, " to class of ", self.gradyear)

user_three = Use("Kibe", 23, 2024)
user_three.welcome()

print ("\n")

# Iterators

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print("\n")

# Modules

module_test.greeting("Kibet Kelvin Chebon")

get_info = module_test.personal_info["country"]
print(get_info)


print("\n")



import platform

plat = platform.system()
plat_directory = dir(platform)
print(plat)
print(plat_directory)

print("\n")

# Date

import datetime

date_time = datetime.datetime.now()
print(date_time)
print("\n")
print(date_time.year)
print(date_time.strftime("%A"))
print(date_time.strftime("%Z"))
print(date_time.strftime("%H"))
print(date_time.strftime("%M"))
print(date_time.strftime("%p"))


print("\n")

# MATH
#JSON
import json

# some JSON:
json_names =  '{ "name":"Chebon Kibet", "age":23, "city":"New York", "institution": "Africa Nazarene University"}'

# parse x: JSON Data to python
json_parsed_data = json.loads(json_names)

# the result is a Python dictionary:
print(json_parsed_data["name"])
print(json_parsed_data["age"])
print(json_parsed_data["city"])
print(json_parsed_data["institution"])

# Convert pytho data to JSON

data_to_json = json.dumps(json_parsed_data, indent=4)
print(data_to_json)

print("\n")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


print("\n")

# Regular Expressions RegEx

import re

regex_txt = "The rain in Spain was catastrofic"
txt_re = re.search("^The.*Spain$", regex_txt)

if txt_re:
  print("YES! We have a match!")
else:
  print("No match")
