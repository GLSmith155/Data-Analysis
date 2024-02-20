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

*= Multiply an existing array.
+= Add to an existing array.

When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).

  a = np.ones(3, dtype=np.int32)
  b = np.linspace(0, pi, 3)
  b.dtype.name
# 'float64'
  c = a + b
  c
# array([1.        , 2.57079633, 4.14159265])
  c.dtype.name
# 'float64'

Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class:
'''
rg = np.random.default_rng(1)  # create instance of default random number generator
z = rg.random((2, 3))
z
# array([[0.82770259, 0.40919914, 0.54959369],
#       [0.02755911, 0.75351311, 0.53814331]])
a.sum()
# 3.1057109529998157
z.min()
# 0.027559113243068367
z.max()
# 0.8277025938204418

'''
b = np.arange(12).reshape(3, 4)
b
# array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])

b.sum(axis=0)     # sum of each column
# array([12, 15, 18, 21])

b.min(axis=1)     # min of each row
# array([0, 4, 8])

b.cumsum(axis=1)  # cumulative sum along each row
# array([[ 0,  1,  3,  6],
#       [ 4,  9, 15, 22],
#       [ 8, 17, 27, 38]])


NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, 
these are called “universal functions” (ufunc). Within NumPy, these functions operate elementwise on an array, producing an array as output.
'''
H = np.arange(5)
print(np.cos(H))
H
# [ 1.          0.54030231 -0.41614684 -0.9899925  -0.65364362]
# array([0, 1, 2, 3, 4])

'''
Indexing, slicing and iterating
One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.
'''
F = np.arange(10)**3    # Creates an array 0 to 9 but with each number exponentially raised to the 3rd power.
F
# array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
F[2]
# 8
F[2:5]    # The 2 is inclusive, the 5 is not, and is just the index we just go up to.
# array([ 8, 27, 64])

J = np.arange(10)**3
print(J)       # [ 0   1   8  27  64 125 216 343 512 729]
print(J[::-1]) # [729 512 343 216 125  64  27   8   1   0]       Reverses NumPy array
