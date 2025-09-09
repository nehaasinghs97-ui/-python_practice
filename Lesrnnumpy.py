
# data=np.array([[1.5,-0.1,3],[0,-3,6.5]])
# print(data)
# print(data*10)
# print(data+data)
 
# # Key features of NumPy is its N dimensional Array object, or ndarray, which is a fast,
# #  flexible container for large datasets in python
 
# #Creating Array
 
# #   np.array() = Conert Python list to NumPy array
# data1=np.array([[1.5,-0.1,3],[0,-3,6.5]])
# print(data1)
# #   np.zeros() = Convert array of all Zeros
# data2=np.zeros((2,3))   # (rows,column)
# print(data2)
# # np.ones() = create array of all ones
# data3=np.ones((2,3))
# print(data3)
#np.eye() - Identity Matrix
# data4=np.eye(4)     # rows = columns
# print(data4)
# #   np.arange() - range(),but return array
# data5=np.arange(0,10,2)     #start,stop,step
# print(data5)
# #   np.linspace() - Evenly Space Numbers
# data6=np.linspace(0,2,5)    #start, stop, number of values
# print(data6)

import numpy as np

# # ✅ 1. Create a 1D array with values from 1 to 10
# arr1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
# print(arr1)
# arr2= np.arange(10)
# print(arr2)

# # ✅ 2. Create a 2D array with shape (3, 3) filled with zeros
# arr2a= np.zeros((3,3))
# print(arr2a)

# # ✅ 3. Create a 2D array with shape (2, 4) filled with ones
# arr3 = np.ones((2,4))
# print(arr3) 

# # ✅ 4. Create a 3x3 array filled with a specific number, say 7
# arr3 = np.ones((3,3))*7
# print(arr3) 

# # ✅ 5. Create an array with values from 10 to 50 with step of 5
# arr4 = np.arange(10,50,5)
# print(arr4) 

#  # ✅ 6. Create an array with 5 values evenly spaced between 0 and 1
# arr5= np.linspace(0,1,5)
# print(arr5)

# # ✅ 7. Create a 3x3 identity matrix
# arr6= np.eye(3)
# print(arr6)

# # ✅ 8. Create a 2x3x4 array with random values between 0 and 1
# arr7=np.random.rand(2,3,4)
# print(arr7)

# # ✅ 9. Create a 1D array of 10 random integers between 50 and 100
# arr8=np.random.randint(50,100,10)
# print(arr8)

# # ✅ 10. Create an empty 4x2 array (uninitialized values)
# arr9= np.empty((4,2))
# print(arr9)

# 1. Create a NumPy array with integer values and print its data type.
# arr = np.array([1,2,3,4,5,6])
# print(arr.dtype)

# 2. Create a NumPy array with float values and change its data type to integers using astype().
# arr1= np.array([1.0, 2.5, 6.4,4.5])
# arr2= arr1.astype(int)
# print(arr2)

# # 3. Check the data type of an existing ndarray using dtype attribute.
# arr=np.array([10,20,30])
# print(arr.dtype)
# arr=np.array([[10,20,30],
#              [40,50.0,60],
#              [70,80,90]])
# print(arr.dtype)

# # 4. Create an array with a specific data type (e.g., int16, float32).
# arr=np.array([10,20,30],dtype=np.int16)
# print(arr.dtype)
# arr=np.array([10,20,30],dtype='int32')
# print(arr)

# # 5. Convert a list of strings into a NumPy array and check its dtype.
# arr4= np.array(['neha', 'miku', 'riya'])
# print(arr4.dtype)

# # 6. Create a boolean array from a list of numbers using a condition (e.g., greater than 5).
# arr5= np.array([1,2,3,4,5,6])
# arr6= arr5>5
# print(arr6)

# 7. Create a NumPy array with complex numbers and print its dtype.
# arr7 = np.array([1+2j,2+3j,4+5j])
# print(arr7,arr7.dtype)

 # 8. Write a program to change the data type of an integer array into float.
# arr1= np.array([1,2,6,4])
# arr2= arr1.astype(float)
# print(arr2)

# 9. Use np.array() with dtype argument to force a certain type (e.g., 'int64').
# arr1= np.array([45,55,66,76], dtype=np.int64)
# arr1= np.array([45,55,66,76], dtype='int64')
# print(arr1)

# 10. Create a structured array with different data types for different fields (e.g., name as string, age as int).
# data=np.array([
#     ('Ishan',10),
#     ('Neha',10)
# ], dtype=[('name','U10'),('age','i4')])
# print(data)

'''
int8 : i1
int16: i2
int32: i4
# int64 : i8

# '''

# # 1. Create two NumPy arrays and perform element-wise addition.
# # arr= np.array([45,76,98])
# # arr1 = np.array([88, 20,100])
# # print(arr+arr1)

# # 2. Subtract one array from another.
# # arr= np.array([45,76,98])
# # arr1 = np.array([88, 20,100])
# # print(arr-arr1)

# # 3. Multiply two arrays element-wise.
# # arr= np.array([45,76,98])
# # arr1 = np.array([88, 20,100])
# # print(arr*arr1)

# # 4. Divide one array by another and handle divide-by-zero errors.


# # 5. Square each element in a NumPy array.
# a=np.array([1,2,3,4,5,6])
# print(a**2)

# # 6. Add a scalar value (like 10) to each element of an array.
# a=np.array([1,2,3,4,5,6])
# print(a+10)

# # 7. Multiply an array by a scalar value.
# a=np.array([1,2,3,4,5,6])
# print(a*7)

# # 8. Calculate the square root of each element in an array.
# a=np.array([1,2,3,4,5,6])
# print(np.sqrt(a))

# 9. Find the sum, mean, max, and min of a NumPy array.
import numpy as np

# a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
#               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
#               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

# print(a.sum())   # 4.8595784
# # print(a.min())   # 0.05093587
# # print(a.max())   # 0.82485143
# # print(a.mean())  # Average: ~0.404965
# # print(a.std())   # Standard deviation
# # print(a.prod())  # Product of all values

# # 10. Use a boolean mask to add 5 only to elements greater than 10.
# # arr6= np.array([1,2,3,4,5,6,90,67,88,54,32,12])
# # arr6[arr6>10]+=5

# # print(arr6)

# # arr6[arr6>10]+=5

# # mask=arr6>10

# # mask= arr>10  :  Create a boolean mask
# #arr[mask]      : access only elements where mask is True
# #arr[mask]+=5   : modifies only those element

# # 1. Create a 1D array of numbers from 10 to 50 and access the 5th element.
# arr= np.arange(10,51)
# print(arr[4])

# # 2. Slice the first 5 elements from a 1D array.
# print(arr[0:5])

# # 3. Reverse a NumPy array using slicing.
# print(arr[::-1])

# # 4. Create a 2D array (3x3) and access the element at row 1, column 2.
# arr2= np.array([[1,2,3] ,
#                [4,5,6],
#                [7,8,9]])
# print(arr2[1,2])

# # 5. Slice the first two rows of a 2D array.
# print(arr2[0:2])
 
# 6. Slice the last column from a 2D array.
# print(arr2[:,-1])
 
# # 7. Replace a slice of a 1D array with new values.
# arr3= np.array([1,2,3,4,5,6,])
# arr3[1:3]=[10,20]
# print(arr3)

# # 8. Extract a submatrix from a 4x4 array (middle 2x2 block).
# array=np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])
# submatrix=array[1:3,1:3]
# print(submatrix)
 
# 9. Use negative indexing to get the last two elements of a 1D array.
# arr3= np.array([1,2,3,4,5,6,])
# print(arr3[-2:])

# 10. Create a 3x3 array and flatten it using slicing.
# array=np.array([[1,2,3],
#                 [5,6,7],
#                 [9,10,11]])
# print(array.reshape(-1))
# print(array.flatten())

# 1. Create an array and filter out all elements greater than 10.
# arr1= np.array([44,56,76,88,12])
# arr11= arr1>10
# print(arr11)

# 2. Given an array, replace all negative values with 0 using boolean indexing.
# arr1= np.array([-44,56,-76,88,-12])
# arr1[arr1<0]=0
# print(arr1)

# 3. Extract only even numbers from a NumPy array.
# arr= np.array([1,2,33,44,5,567,89])
# arr1= arr[arr%2 == 0]
# print(arr1)

# 4. Count how many elements in an array are greater than a specific value.
# arr= np.array([1,2,33,44,5,567,89])
# count=np.sum(arr>33)
# #sum[0 0  0 1 0 1 1]
# print(count)

# 5. Given two arrays, filter values in one that are also present in the second array.
# arr= np.array([1,2,33,44,5,567,89])
# arr1 = np.array([1,2,55,44,6,33])
# print(arr[np.isin(arr,arr1)])

# # 6. Create a boolean array based on a condition (like arr % 2 == 0).
# arr=np.arange(1,53,3)
# print(arr[arr%2==0])

# 7. Set all values in an array greater than a threshold (e.g. 50) to 100.
# arr2= np.arange(1,150)
# arr2[arr2>50] = 100
# print(arr2)

# 8. Filter all elements between 10 and 30 (inclusive) from a NumPy array.
# arr3 = np.arange(10,31)
# print(arr3)

# arr4=np.arange(1,100)
# print(arr4)
# print(arr4[(arr4>=10) & (arr4<=30)])

# 9. Use a boolean mask to extract rows from a 2D array based on a condition.
# arr3= np.array([[2,3,4],
#                [4,5,6]])
# # print(arr3[0,1])
# print(arr3[arr3[:,1]>4])

# # 10. Use boolean indexing to filter out NaN values from an array.
# arr = np.array([1, np.nan, 3, np.nan])
# mask = np.isnan(arr)
# print(mask)         # [False  True False  True]
# print(arr[~mask])

#NaN Stand for "Not a Number"  its a special floating point value
#It is used to represent missing, undefined, or invalid value
#or sometimes some entries are empty

# Detect NaN        np.isnan(arr)
# Count NaNs        np.sum(np.isnam(arr))
# Remove NaNs       arr[~np.isnan(arr)]
# RePlace Nan       np.nan_to_num(arr,nan=0)
# ignore NaNs calulation    np.nanmean(), np.nansum()


# 1. Create a NumPy array and print elements at positions 1, 3, and 4 using fancy indexing.
# arr=np.arange(2,50,2)

# print(arr[[1,3,4]])
# # 2. Given an array, extract elements at positions stored in another array of indices.
# arr1=np.array([10,20,30,40,50,60,70,80,90])
# indices=np.array([0,2,4,6])
# print(arr1[indices])

# 3. Create a 5x5 2D array and access the diagonal elements using fancy indexing.
# arr= np.array([[1,2,3,4,5], 
#               [6,7,8,9,10],
#               [11,12,13,14,15],
#               [16,17,18,19,20],
#               [21,22,23,24,25]])
# print(arr[[0,1,2,3,4], [0,1,2,3,4]])

# # 4. Replace values at specific indices (e.g., index 0 and 2) in a 1D array.
# arr1= np.array([1,2,3,4,5,6,7,8])
# arr1[[0,1]] = [10,20]
# print(arr1)

# # 5. Use fancy indexing to extract specific rows from a 2D array.
# mat=np.arange(1,13).reshape(4,3)
# print(mat)
# print(mat[[0,1]])

# 6. Use fancy indexing to extract specific columns from a 2D array.
# mat1= np.arange(11,23).reshape(3,3)
# print(mat1)

mat1=np.arange(11,23).reshape(3,4)
print(mat1)
print(mat1[1,1]) 

# 7. Use fancy indexing to extract elements at row 0, col 1 and row 1, col 2 and row 2, col 3.
print(mat1[[0,1,2],[1,2,3]])

# 8. Create a 1D array and reverse it using fancy indexing (not slicing).
arr2= np.array([1,2,3,4,5])
print(arr2[[4,3,2,1,0]])

# 9. Use fancy indexing to shuffle an array.
 
# 10. Use fancy indexing to sort an array based on the values of another array (indirect sorting).