#!/usr/bin/env python
# coding: utf-8

# In[7]:


#QUESTION 1 NUMPY


import numpy as np

# Create random vector of size 15 with integers in the range 1-20
ran_vec = np.random.randint(1, 21, size=15)
print("Vector:", random_vec)

# Reshape the array to 3 by 5
reshaped_array = ran_vec.reshape((3, 5))
print("Reshaped array:\n", reshaped_array)

# Print array shape
print("Array shape:", reshaped_array.shape)

# Replace the max in each row by 0
reshaped_array[np.arange(len(reshaped_array)), np.argmax(reshaped_array, axis=1)] = 0
print("Array after replacing max in each row with 0:\n", reshaped_array)

# Create 2-dimensional array of size 4 x 3
arr_2d = np.zeros((4, 3), dtype=np.int32)
print("2-dimensional array:\n", arr_2d)
print("Array shape:", arr_2d.shape)
print("Array type:", type(arr_2d))
print("Array data type:", arr_2d.dtype)


# In[2]:


# Given square array for question b
arr = np.array([[3, -2], [1, 0]])

# Computing eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(arr)

# Print the eigenvalues and right eigenvectors
print("Eigenvalues:", eigenvalues)
print("Right eigenvectors:\n", eigenvectors)


# In[3]:


# Given array in question c
arr1 = np.array([[0, 1, 2], [3, 4, 5]])

# Compute the sum of diagonal elements
sum_diagonal_ele = np.trace(arr1)

# Print the sum of diagonal elements
print("Sum of diagonal elements:", sum_diagonal_ele)


# In[4]:


# Given array in question d
original_array = np.array([[1, 2], [3, 4], [5, 6]])

# Reshape the array to 2x3 without changing data
array_reshape_2x3 = original_array.reshape((2, 3))

# Print the original array and the reshaped array
print("Original array:\n", original_array)
print("Reshaped array (2x3):\n", array_reshape_2x3)


# In[5]:


#QUESTION 2 MATPLOTLIB

import matplotlib.pyplot as plt

# Define the data
Programming_languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

explode = [0.1, 0, 0, 0, 0, 0]

# Create the pie chart
plt.pie(popularity, labels=Programming_languages, explode=explode, shadow=True,
        wedgeprops={'edgecolor': 'black'},autopct='%1.1f%%')

# Add a title
plt.title("Popularity of Programming Languages")

# Display the pie chart
plt.show()


# In[ ]:




