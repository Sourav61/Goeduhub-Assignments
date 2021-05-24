# ID: GO_STP_13420

# Q1) We are having 3 list like this

# Colors = [“Yellow”,”Green”,”White”,”Black”]

# Fruits=[“Apple”,”Papaya”,”Mango”,”Orange”]

# Q1)Animals=[“Tiger”,”Lion”,”Deer”,”Zebra”]

# i. Write a program that asks user to enter a Color/Fruit/Animal name and it should tell which category belongs to , like its is a fruit or color or Animal

# ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter yellow and Black, it will print "Both are colors" but if I enter yellow and Tiger it should print "They don't belong to same category"

Colors = ["Yellow", "Green","White","Black"]

Fruits=["Apple","Papaya","Mango","Orange"]

Animals=["Tiger","Lion","Deer","Zebra"]

inp = input("Enter a Color/Fruit/Animal: ").title()

if inp in Colors:
  print(f"{inp} is a Color") 
elif inp in Fruits:
  print(f"{inp} is a Fruit")
elif inp in Animals:
  print(f"{inp} is an Animal")
else:
  print(f"{inp} is not present in any of the above lists")

inp1 = input("Enter the first category: ").title()
inp2 = input("Enter the second category: ").title()

if inp1 in Colors and inp2 in Colors:
  print(f"{inp1} and {inp2} both are present in Colors")

if inp1 in Fruits and inp2 in Fruits:
  print(f"{inp1} and {inp2} both are present in Fruits")

if inp1 in Animals and inp2 in Animals:
  print(f"{inp1} and {inp2} both are present in Animals")

# Q2)  Write a python program that can tell you if your grade score good or not . Normal Score range is 40 to 60.

#   i. Ask user to enter his score.

#   ii. If it is below 40 to 60 range then print that score is low

#   iii. If it is above 60 then print that it is good otherwise print that it is normal

score = float(input("Enter your score"))

if score<=40:
  print(f"The Score {score} is low")

elif 40<score<60:
  print(f"The Score {score} is normal")

else:
  print(f"The Score {score} is good")

""" Q3) After appearing in exam 10 times you got this result,

result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]

Using for loop figure out how many times you got Pass
"""

result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]
sum=0

for i in range(len(result)):
  if result[i] == "Pass":
    sum += 1

print(f"You have passed {sum} times")

""" Q4) Write a program that prints following shape

*

* *

* * *

* * * *

* * * * *

* * * *

* * *

* *

*
"""

for i in range(0,6,1):
  for j in range(i):
    print("*",end="")
  print("\n")

for i in range(4,0,-1):
  for j in range(i):
    print("*",end="")
  print("\n")

""" Q5) Lets say you are running a 50 km race. Write a program that,

Upon completing each 10 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
 If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 50 km then it should print congratulations message
"""

final = 0
for i in range(0,50,10):
  res = input("Are You Tired: Yes or No? ")
  if res.title() == "Yes":
    print("You didn't finish the race")
    final += 1
    break
  elif res.title() == "No":
    print("Keep Going, You can and you will do it")
    continue
  else:
    print("Please enter Yes or NO")
    final += 1
    break

if(final == 0):
  print("Congratulations, You have Successfully Completed the race")

""" Q6) Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)."""

for num in range(1500,2701):
  if num%5 == 0 and num%7 == 0:
    print(num)

""" Q7) Print square of all numbers between 10 to 20 except even numbers"""

for num in range(10,21):
  if num % 2 == 0:
    pass
  else:
    print(num**2)

""" Q8) Your Marks for five Test(test1 to test5) looks like this,

marks_list = [65, 75, 2100, 95, 83]

Write a program that asks you to enter marks and program should tell you in which test that marks occurred. If marks is not found then it should print that as well.
"""

marks_list = [65, 75, 2100, 95, 83]

query = int(input("Enter your marks obtained: "))
for num in range(len(marks_list)):
  if query in marks_list:
    print(f"You obtained {query} marks in test!")
    break
  else:
    print(f"Marks {query} entered is not present in list")
    break
