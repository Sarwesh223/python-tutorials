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
#Ans-
matrix = np.random.rand(3,3)
print(matrix)

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

#8. Ways to convert array of string to array of floats ?
#Ans
def convert_strings_to_floats(input_array):
	output_array = []
	for element in input_array:
		converted_float = float(element)
		output_array.append(converted_float)
	return output_array
input_array = ['1.1', '1.5', '2.7', '8.9']
output_array = convert_strings_to_floats(input_array)
print(output_array)


#9. Get Random elements from Laplace distribution?
#Ans- 
random_value = np.random.laplace(loc=0, scale=1)  # Mean=0, Scale=1
print(random_value)

#10. Generate Random Numbers From The Uniform Distribution using NumPy?
#Ans-

# numpy.random.uniform() method 
r = np.random.uniform(size=4) 

# printing numbers 
print(r)
