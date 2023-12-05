# AIM: Use NumPy to create and manipulate arrays. Implement a Python program to perform matrix multiplication.

import numpy as np

mat1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

mat2 = np.array([3,2,65,324,12,4,43,23,76]).reshape(3,3)
print(mat1)
print(mat2)
print(mat1.shape)
print("------Multiply")
print(np.dot(mat1, mat2))


print("------Multiply")
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(10, 19).reshape(3, 3)
print(arr1)
print(arr2)
print(np.dot(arr1, arr2))