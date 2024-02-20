import numpy as np
'''
A frequent error consists in calling array with multiple arguments, rather than providing a single sequence as an argument.

a = np.array(1, 2, 3, 4)    # WRONG
Traceback (most recent call last):
TypeError: array() takes from 1 to 2 positional arguments but 4 were given
'''
a = np.array([1, 2, 3, 4])  # RIGHT

'''
np.array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.
'''
b = np.array([(1.5, 2, 3), (4, 5, 6)])       # 2-dimensional  
c = np.array([ [(1.5, 2, 3), (4, 5, 6)],     # 3-dimensional
               [(4, 1, 1), (2, 3, 4)]         
            ]) 
print(c.shape) # (2, 2, 3) '2 by 2 by 3'
print(c.ndim) # 3 '3 dimensions'  #-dimensional

# The type of the array can also be explicitly specified at creation time:
d = np.array([[1, 2], [3, 4]], dtype=complex)
#  d = ([[1.+0.j, 2.+0.j],
#       [3.+0.j, 4.+0.j]])

'''
Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several functions to create arrays with initial 
placeholder content. These minimize the necessity of growing arrays, an expensive operation.

The function zeros creates an array full of zeros, the function ones creates an array full of ones, and the function empty creates an array whose initial content 
is random and depends on the state of the memory. By default, the dtype of the created array is float64, but it can be specified via the key word argument dtype.
'''
np.zeros((3, 4))
#array([[0., 0., 0., 0.],
#       [0., 0., 0., 0.],
#       [0., 0., 0., 0.]])
np.ones((2, 3, 4), dtype=np.int16)
#array([[[1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]],

#        [[1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]]], dtype=int16)
np.empty((2, 3)) 
#array([[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # may vary
#       [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]])
'''
To create sequences of numbers, NumPy provides the arange function which is analogous to the Python built-in range, but returns an array.
'''
np.arange(10, 30, 5) # Generate an array of of numbers from 10 to 30 counting by 5's. The first number is inclusive, while the high number is not.
#array([10, 15, 20, 25])
np.arange(0, 2, 0.3)  # It accepts float arguments.
#array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
'''
When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite 
floating point precision. For this reason, it is usually better to use the function linspace that receives as an argument the number of elements 
that we want, instead of the step:
"Finite precision is decimal representation of a number which has been rounded or truncated. There many cases where this may be necessary or appropriate. For example 1/3 and the transcendental 
numbers e and π all have infinite decimal representations."
'''
np.linspace(0, 2, 9)   # array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])          Creates an array with 9 elements between 0 and 2 - inclusive 0 and 2.
'''
Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
a = np.array([20, 30, 40, 50])
10 * np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
a < 35
array([ True,  True, False, False])
'''

'''
Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays. 
The matrix product can be performed using the @ operator (in python >=3.5) or the dot function or method:

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
              
A * B     # elementwise product, as in the first element 1 just multiples the first element 2, so not matrix multiplication.
array([[2, 0],
       [0, 4]])
       
A @ B     # matrix product
array([[5, 4],
       [3, 4]])
       
A.dot(B)  # another matrix product
array([[5, 4],
       [3, 4]])

'''
