# 1.how to create an empty and a full NumPy array?
#Ans-

#empty NumPy array
import numpy as np

empty_array_nd = np.empty(())
print(empty_array_nd) 

#full NumPy array
full_array_3d = np.full((4,5),6)
print(full_array_3d)


#2. Creat a NumPy array filled with all zeros ?
#Ans-
array_nd =np.zeros(5)
print(array_nd)

#3. Create a NumPy array filled with all ones ?
#Ans-
ones_array_3d = np.ones((3,3))
print(ones_array_3d)

#4.  Combining a one and two-dimensional NumPy array ?
#Ans-
one_d_arr = np.array([9,6,7])
two_d_arr = np.array([[2,3,4],[5,6,7]])
combined_arr = np.vstack([one_d_arr,two_d_arr])
print(combined_arr)

#5. Create a NumPy array with random values ?
#Ans-
three_d_arr = np.random.rand(3,4,5)
print(three_d_arr) 

#6. Return amatrix of random values from a Gaussian distribution ?



#7. How to convert a list and tuple into NumPy array ?
#list

#Ans-
li = [1,2,5,6,3]
arr = np.array(li)
print(li)

#Tuple
li = (20,30,40,12,45)
arr = np.array(li)
print(type(li))