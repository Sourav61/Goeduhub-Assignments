# -*- coding: utf-8 -*-
"""Task_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Sourav61/Goeduhub-Assignments/blob/main/Task_03.ipynb

Author: <b><a href="https://github.com/Sourav61">Sourav Pahwa</a></b>

ID: GO_STP_13420
"""

from google.colab import drive
drive.mount('/content/drive')

"""<b>Q.1 Write a Python Program to sort (ascending and descending) a dictionary by value. </b>"""

x={'c':30,'d':40,'a':10,'b':20,'f':50,'g':60} 
                                         
l=list(x.items())   
l.sort()            

Dicta=dict(l)
print("Dictionary in ascending order",Dicta)

l=list(x.items())
l.sort(reverse=True)

Dictd = dict(l)
print("Dictionary in discending order",Dictd)

"""<b>Q.2 Write a Python Program to add a key to a dictionary.<br />
Sample Dictionary : {0: 10, 1: 20}<br />
Expected Result : {0: 10, 1: 20, 2: 30}
</b>
  
"""

d={0:10,1:20}
d.update({2:30})
print(d)

"""<b>Q.3 Write a  program asks for City name and Temperature and builds a dictionary using that Later on you can input City name and it will tell you the Temperature of that City.</b>"""

city1 = input("Enter the name of 1st City: ")
temp1 = input("Enter the temperature of 1st City in Celcius: ")
city2 = input("Enter the name of 2nd City: ")
temp2 = input("Enter the temperature of 2nd City in Celcius: ")

city = [city1,city2]
temp = [temp1,temp2]

Dict = dict(zip(city,temp))

print(Dict)

query = input("Enter the city for which you want to check temperature? ")
print(f"The temperature of {query} is: ", Dict[f"{query}"])

"""<b>Q. 4 Write a Python program to convert list to list of dictionaries.

Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]

Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

</b>
"""

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': a, 'color_code': b} for a, b in zip(color_name, color_code)])

"""<b>Q. 5 We have following information on Employees and their Salary (Salary is in lakhs),

Employee	Salary </br>
John	14</br>
Smith	13</br>
Alice	32</br>
Daneil	21</br>
</b>
1)Using above create a dictionary of Employees and their Salary

2)Write a program that asks user for three type of inputs,

  <b>a) print</b>: if user enter print then it should print all Employees with  
  their Salary in this format,</br>
  John ==>14</br>
  Smith ==>13</br>
  Alice ==>32</br>
  Daneil ==>21</br>
  <b>b) add</b>: if user input adds then it should further ask for an Employee 
  name to add. If Employee already exists in our dataset then it should print 
  that it exists and do nothing. If it doesn't then it asks for Salary and add 
  that new Employee/Salary in our dictionary and print it</br>
  <b>c) remove</b>: when user inputs remove it should ask for an Employee to 
  remove. If an Employee exists in our dictionary then remove it and print a 
  new dictionary using format shown above in (a). Else print that Employee 
  doesn't exist!</br>
  <b>d) query</b>: on this again ask the user for which Employee he or she 
  wants to query. When a user inputs that Employee it will print the Salary of 
  that Employee.
"""

empl = ['John','Smith','Alice','Daniel']
sal = [14, 13, 32, 21]

inp= input("Enter your choice :print or add or remove or query: ")
if inp == 'print':
  Dict = dict(zip(empl, sal))
  for a in Dict:
    print(a,"==>",Dict[f"{a}"])

elif inp == 'add':
  emp= input("Enter the name of the Employee to be added: ")
  if emp.title() in Dict.keys():
    print(f"{emp} name is already existing!")
  else:
    salr = input(f"Enter the salary of the {emp} ")
    Dict.update({emp : salr})
    print(Dict)

elif inp == 'remove':
  name = input("Enter the name of the employee to be removed? ")
  if name in Dict:
    Dict.pop(name)
    print(Dict)

  else:
    print(f"Sorry!!, {name} doesn't exist in the data!")
  
elif inp == 'query':
  emp= input("Enter the name of the employee you want to query: ").title()
  if emp in Dict.keys():
    print(f"The salary of {emp} is {Dict[emp]}")
  else:
    print(f"The employee named {emp} doesn't exist!!")

else:
  print("Enter a valid choice")

"""# <h1><b> Questions on Sets-</b></h1>

<b>Q.1 What is the difference between a set and a frozenset? Create any set and try to use frozenset(setname).

Ans) A Set is an unordered collection of items.Main feature of a set is that every element in a set is unique.A Set is created by placing all the items (elements) inside curly braces {} and separated by comma.

A Frozenset can be made from a set by using frozenset() keyword. It is basically an immutable type of set just like tuple.</b>


"""

a = set("Set and FrozenSet")
print(a)
print(type(a))

a.remove(" ")
print(a)

a = frozenset(a)

print(type(a))

a.discard(" ")

"""<b>Q.2 Find the elements in a given set that are not in another set</b>

    set1 = {10,20,30,40,50}

    set2 = {40,50,60,70,80}

 Difference between set1 and set2 is {10,20,30}
"""

set1 = {10,20,30,40,50}
set2 = {40,50,60,70,80}
print("Original sets given:")
print(set1)
print(set2)
print("Elements present in set1 but not in set2 using difference() method:")
print(set1.difference(set2))
print("Elements present in set2 but not in set1 using difference() method:")
print(set2.difference(set1))