import numpy as np

'''
NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, 
various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, 
logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types, with many operations being performed in 
compiled code for performance. There are several important differences between NumPy arrays and the standard Python sequences:

1. NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.
2. The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) 
   objects, thereby allowing for arrays of different sized elements.
3. NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than 
   is possible using Python’s built-in sequences.
'''

'''
As a simple example, consider the case of multiplying each element in a 1-D sequence with the corresponding element in another sequence of the same length. 
If the data are stored in two Python lists, a and b, we could iterate over each element:
'''
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

c = []
for i in range(len(a)):
    c.append(a[i]*b[i])

'''
This produces the correct answer, but if a and b each contain millions of numbers, 
we will pay the price for the inefficiencies of looping in Python.

for (i = 0; i < rows; i++) {
  c[i] = a[i]*b[i];
}
The example above in C is much faster due to being O(n) by only going over the entire length of data once.
However, C can get very ugly and inefficient when dealing with 2D arrays in a similar example.
Therefore, NumPy gives us the best of both worlds: element-by-element operations are the “default mode” when an ndarray is involved, but the element-by-element operation is 
speedily executed by pre-compiled C code. 
'''

c = a * b

'''
In NumPy c = a * b does what the earlier examples do, at near-C speeds, but with the code simplicity we expect from something based on Python.

Why is NumPy fast?
Vectorization describes the absence of any explicit looping, indexing, etc., in the code - these things are taking place, of course, just “behind the scenes” in optimized, 
pre-compiled C code. Vectorized code has many advantages, among which are:

vectorized code is more concise and easier to read
fewer lines of code generally means fewer bugs
the code more closely resembles standard mathematical notation (making it easier, typically, to correctly code mathematical constructs)
vectorization results in more “Pythonic” code. Without vectorization, our code would be littered with inefficient and difficult to read for loops.

Broadcasting is the term used to describe the implicit element-by-element behavior of operations; generally speaking, in NumPy all operations, not just arithmetic operations, 
but logical, bit-wise, functional, etc., behave in this implicit element-by-element fashion, i.e., they broadcast. Moreover, in the example above, a and b could be multidimensional 
arrays of the same shape, or a scalar and an array, or even two arrays with different shapes, provided that the smaller array is “expandable” to the shape of the larger in such a 
way that the resulting broadcast is unambiguous. 
----
NumPy fully supports an object-oriented approach, starting, once again, with ndarray. For example, ndarray is a class, possessing numerous methods and attributes. Many of its methods are 
mirrored by functions in the outer-most NumPy namespace, allowing the programmer to code in whichever paradigm they prefer. This flexibility has allowed the NumPy array dialect and NumPy 
ndarray class to become the de-facto language of multi-dimensional data interchange used in Python.

NumPy’s array class is called ndarray. It is also known by the alias array. Note that numpy.array is not the same as the Standard Python Library class array.array, 
which only handles one-dimensional arrays and offers less functionality. 

The more important attributes of an ndarray object are:

ndarray.ndim
the number of axes (dimensions) of the array.

ndarray.shape
the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). 
The length of the shape tuple is therefore the number of axes, ndim.

ndarray.size
the total number of elements of the array. This is equal to the product of the elements of shape.

ndarray.dtype
an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, 
and numpy.float64 are some examples.

ndarray.itemsize
the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). 
It is equivalent to ndarray.dtype.itemsize.

ndarray.data
the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.

Here are examples of ndarray's main attributes:
'''
a = np.arange(15).reshape(3, 5) # This is a clean way to go ahead and establish the dimensions of array a.
                                # And if we remove this line, then all of the below code still works.
                                # Do this when you want to go ahead and ensure that we don't mistype and
                                # create an array of incorrect dimensions when we type in the numberes below.
a = np.array([[ 0,  1,  2,  3,  4],
              [ 5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14]])
print(a.shape)         #  (3, 5)

print(a.ndim)          #  2

print(a.dtype.name)    # int64

print(a.itemsize)      # 8

print(a.size)          # 15

print(type(a))         # <class 'numpy.ndarray'>

b = np.array([6, 7, 8])
print(b)               # [6 7 8]

print(type(b))         # <class 'numpy.ndarray'>



