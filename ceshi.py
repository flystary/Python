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
print("Enter your name:")
x = input()
print("Hello", x)

