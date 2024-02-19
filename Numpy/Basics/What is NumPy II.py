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
