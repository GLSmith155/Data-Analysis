'''
Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:
def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
       
b[2, 3]
23

b[0:5, 1]  # each row in the second column of b
array([ 1, 11, 21, 31, 41])

b[:, 1]    # equivalent to the previous example
array([ 1, 11, 21, 31, 41])

b[1:3, :]  # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])

The expression within brackets in b[i] is treated as an i followed by as many instances of : as needed to represent the remaining axes. NumPy also allows you to write this using dots as b[i, ...].

The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is an array with 5 axes, then

x[1, 2, ...] is equivalent to x[1, 2, :, :, :],

x[..., 3] to x[:, :, :, :, 3] and

x[4, ..., 5, :] to x[4, :, :, 5, :].

c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
c.shape
(2, 2, 3)
c[1, ...]  # same as c[1, :, :] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
c[..., 2]  # same as c[:, :, 2]
array([[  2,  13],
       [102, 113]])

Iterating over multidimensional arrays is done with respect to the first axis:

for row in b:
    print(row)

[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]   

However, if one wants to perform an operation on each element in the array, one can use the flat attribute which is an iterator over all the elements of the array:
for element in b.flat:
    print(element)
'''

'''
Shape manipulation-
Changing the shape of an array
An array has a shape given by the number of elements along each axis:
'''
a = np.floor(10 * rg.random((3, 4)))
a
# array([[3., 7., 3., 4.],
#       [1., 4., 2., 2.],
#       [7., 2., 4., 9.]])
a.shape
#(3, 4)
'''
The shape of an array can be changed with various commands. Note that the following three commands all return a modified array, but do not change the original array:
'''
a.ravel()  # returns the array, flattened
# array([3., 7., 3., 4., 1., 4., 2., 2., 7., 2., 4., 9.])
a.reshape(6, 2)  # returns the array with a modified shape
# array([[3., 7.],
#       [3., 4.],
#       [1., 4.],
#       [2., 2.],
#       [7., 2.],
#       [4., 9.]])
a.T  # returns the array, transposed
# array([[3., 1., 7.],
#       [7., 4., 2.],
#       [3., 2., 4.],
#       [4., 2., 9.]])
a.T.shape
# (4, 3)
a.shape
# (3, 4)
