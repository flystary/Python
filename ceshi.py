#!/usr/bin/env python
#!coding=utf-8
"""
def myfunc():
     global x
     x = "fantastic"

myfunc()
print("Python is" + x)
"""
"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"  #函数内部更改全局变量，请使用 global 关键字

myfunc()

print("Python is " + x)

"""
"""
x = 10
print(type(x) #获取数据类型
)
"""
"""
import random
print(random.randrange(1,20))
"""
"""
a='''Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code.'''
print(a)
"""
#b="hello,world!"
#print(b[0:12])
#print(b[-6:-1])
#print(len(b))

"""
a="  Hello,World!  "
print(a)
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("World","liql"))
print(a.split(","))
"""
"""
txt = "China is a great country"
#x= "eat" in txt
x = "aet" not in txt
print(x)
#print(txt.split(" "))
#print(txt.split("s"))
"""
"""
a = "Hello"
b = "World"
c = a + b
c = a + "," +b +"!"
print(c)
"""
"""
quantity = 4
itemno = 234
price = 90.43
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))
x = myorder.find("ant")
print(x)
"""
"""
thistuple = ("apple","banana","cherry")
for x in thistuple:
    print(x)
"""
"""

tule1 = ("a","b","c")
tule2 = (1,2,4,5)
tule3 = tule1 + tule2
print(tule3)
"""
"""
thisdict =    {
    "brand":"Porsche",
    "model":"911",
    "year":"2020-04-14"
}
thisdict.pop("model")
print(thisdict)
"""
"""
i=1
while i<10:
    print(i)
    c=i+(i+1)
    if i == 5:
       break
    i += 1 
"""
"""
i = 0
while i < 10:
     i +=  1
     if i >= 7:
         continue
     print(i)
"""
"""
y = range(2,14)
for x in y:
   if x == 10:
       print(len(y))
    
"""
"""
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "cherry":
        break
    print(x)
"""
"""
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "cherry":
        continue
    print(x)
"""
"""
print("Enter your name:")
x = input()
print("Hello", x)
print("Enter your name:")
ssl = input()
ssl = open("ssl.txt","x")
"""
"""
import os, sys
def Mkdir():
    #print("Enter your file name:")
    #path = input()
    #file_name = path
    file_name = x
    os.mkdir(file_name)
    os.chdir(file_name)
    f = open("demofile2.txt", "w")
    f.write("Now the file has more content!")
    f.close()

def my_function(food):
    global x
    for x in food:
        Mkdir()
        format(x)
        #print(x)
fruits = ("baidu","ali","tenc","ucloud")
Mkdir(my_function(fruits))

#my_function(fruits)
"""
#name(fruits)
"""
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
"""
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("liql", 23)

print(p1.name)
print(p1.age)
"""
"""
class Person:
    def __init__(are,name,age):
        are.name = name 

        are.age = age
    def my_function(asx):
        print("hello myname is "+ asx.name)

p1 = Person("duhongw",24)
print(p1.name)
print(p1.age)
p1.my_function()
"""
class Person:
    def __init__(are,fname,lname):
        are.firstname = fname
        are.lastname = lname

    def printname(are):
        print(are.firstname,are.lastname)
"""
class student(Person):
    def __init__(are,fname,lname):
        #Person.__init__(are.fname,lname)
        super().__init__(fname,lname)
        are.graduationyear = 2019
"""
"""
class Student(Person):
    def __init__(are,fname,lname,year):
        super().__init__(fname,lname)
        are.graduationyear = year

#x = student("bill","Gates")
    def welcome(are):
        print("Walcome",are.firstname,are.lastname,"to the class of",are.graduationyear )
#print(x.graduationyear)
x = Student("Elon","Musk",2019)
x.welcome()
"""
"""
x = 100
def myfunc():
    x = 200
    print(x)

myfunc()
print(x)
"""
"""
import json

x = {
    "name": "Bill",
    "age" : 62,
    "married" : True,
    "divorced": False,
    "children" : ("Jennifer","Rory","Phoebe"),
    "pets" : None,
    "cars" : [
         {"model": "Porsche", "mpg": 38.2},
         {"model": "BMW M5", "mpg": 26.9}
    ]
}

#print(json.dumps(x))
print(json.dumps(x,indent=4))
"""
import re
txt = "China is a great country"
#x = re.sub("China","Hangzhou", txt)
#str = "China is a great country"
#x = re.sub("\s", "9", txt, 3)
x = re.search("ani",txt)

print(x)

"""
if (x):
  print("YES! We have a match!")
else:
  print("No match")
"""