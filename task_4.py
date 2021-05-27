# -*- coding: utf-8 -*-
"""Task-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12eOM7Jgm9BHVl7601zoJdR2N6RHX9E4o

Author <a href = "https://github.com/Sourav61">Sourav Pahwa</a>
<br>ID: GO_STP_13420

<b> Assignment/Task 4
 <br> Question on Numpy</b>

<b>Q1)</b> Import the numpy package under the name np and Print the numpy version and the configuration?
"""

import numpy as np
print(np.__version__)
np.show_config()

"""<b>Q2)</b> Create a null vector of size 10"""

print(np.zeros(10))

"""<b>Q3)</b> Create Simple 1-D array and check type and check data types in array"""

a = np.array([1, 2, 3, 4, 5])

print(a)

print(type(a))

print(a.dtype)

"""<b>Q4)</b> How to find number of dimensions, bytes per element and bytes of memory used?"""

x = np.array([[10, 20, 30],
              [40, 50, 60]])

print("The number of the given numpy array is: ",np.ndim)  

print("Size of the array: ", x.size)

print("Memory size of an element in bytes: ", x.itemsize)

print("Memory size used by numpy array in bytes:", x.size * x.itemsize)

"""<b>Q5)</b> Create a null vector of size 10 but the fifth value which is 1"""

a = np.zeros(10)
print(a)
a[4]=1
print("After updating the 5th postion of original array with 1,now our nupy array becomes: \n",a)

"""<b>Q6)</b> Create a vector with values ranging from 10 to 49"""

a = np.arange(10,50)
print(a)

"""<b>Q7)</b> Reverse a vector (first element becomes last)"""

a = np.arange(20)

print("The Numpy array created is: ",a)

print("The reversed vector(1-d numpy array) is: ",a[::-1])

"""<b>Q8)</b> Create a 3x3 matrix with values ranging from 0 to 8"""

a = np.arange(9)
print(a.reshape(3,3))

"""<b>Q9)</b> Find indices of non-zero elements from [1,2,0,0,4,0]"""

nums = np.array([1,2,0,0,4,0])
print("Original array:")
print(nums)
print("Indices of elements equal to zero of the said array:")
for i in range(nums.size):
  if nums[i] != 0:
    print(nums[i], end=" ")

"""<b>Q10)</b> Create a 3x3 identity matrix"""

print(np.ones(9).reshape(3,3))

"""<b>Q11)</b> Create a 3x3x3 array with random values"""

a = np.random.random((3,3,3))
print(a)

"""<b>Q12)</b> Create a 10x10 array with random values and find the minimum and maximum values"""

a = np.random.random((10,10))
print("The random numpy array generated is: \n",a)
print("The minimum value of random array generated is: ",a.min())
print("The maximum value of random array generated is: ",a.max())

"""<b>Q13)</b> Create a random vector of size 30 and find the mean value"""

a = np.random.random(30)
a.mean()

"""<b>Q14)</b> Create a 2d array with 1 on the border and 0 inside"""

a = np.ones((10,10))
a[1:-1,1:-1] = 0
print(a)

"""<b>Q15)</b> How to add a border (filled with 0's) around an existing array? """

x = np.ones((3,3))
print("Original array is: \n",x,"\n")

x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print("The required array is: \n",x)

"""<b>Q16)</b> How to Accessing/Changing specific elements, rows, columns, etc in Numpy array?

Example -
[[ 1 2 3 4 5 6 7] [ 8 9 10 11 12 13 14]]

Get 13, get first row only, get 3rd column only, get [2, 4, 6], replace 13 by 20
"""

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a[1,5],"\n")

print(a[0,:],"\n")

print(a[:,2],"\n")

print(a[0,:][1:6:2],"\n")

a[1,5]=20
print(a)

"""<b>Q17)</b> How to Convert a 1D array to a 2D array with 2 rows"""

a = np.zeros(4)
print("The one dimensional array used here is: ",a,"\n")
arr = a.reshape(2, 2)
print("The 2-D array produced from 1D array is: \n")
print(arr)

"""<b>Q18)</b> Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

<b>Input:</b>

a = np.array([1,2,3])`

<b>Desired Output:</b>

# array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
"""

a=np.array([1,2,3])
print("The given array is: \n",a,"\n")
print("The required output is: \n",np.r_[np.repeat(a, 3), np.tile(a, 3)])

"""<b>Q19) Write a program to show how Numpy taking less memory compared to Python List?</b>

Ans) A nd-array in Numpy has faster computational speed and less memory required to complete a specific programs whereas a list takes a lot more memory in pyhton.
"""

l = range(10000)

import sys

a = 10
print(sys.getsizeof(a))

print(sys.getsizeof(a)*len(l))

a1 = np.arange(1000)
print(a1.size*a1.itemsize)

"""<b>Q20) Write a program to show how Numpy taking less time compared to Python List? </b>

Ans) A nd-array in Numpy has faster computational speed and less memory required to complete a specific programs whereas a list takes a lot more memory in pyhton.
"""

import time 
import sys

size = 1000000

a = range(size)
b = range(size)

#For pytho Lists
start = time.time()
result=  [(x+y) for x,y in zip(a,b)]
print((time.time()-start)*1000)

#For Numpy
start = time.time()
print((time.time()-start)*1000)