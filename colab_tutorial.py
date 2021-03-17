def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]      # Floor division
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

mysort = quicksort([3,6,8,10,1,2,1])
print('[%s]' % ','.join(map(str, mysort)))
print(quicksort([3,6,8,10,1,2,1]))

# Basic data types

# Numbers
x = 3
print(x, type(x))
print(x + 1)   # Addition
print(x - 1)   # Subtraction
print(x * 2)   # Multiplication
print(x ** 2)  # Exponentiation
x += 1
print(x)
x *= 2
print(x)
y = 2.5
print(type(y))
print(y, y + 1, y * 2, y ** 2)

# Booleans
t, f = True, False
print(type(t))
print(t and f) # Logical AND;
print(t or f)  # Logical OR;
print(not t)   # Logical NOT;
print(t != f)  # Logical XOR;

# Strings
hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes; it does not matter
print(hello, len(hello))
hw = hello + ' ' + world  # String concatenation
print(hw)
hw12 = '{} {} {}'.format(hello, world, 12)  # string formatting
print(hw12)

s = "hello"
print(s.capitalize())  # Capitalize a string
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces
print(s.center(7))     # Center a string, padding with spaces
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another
print('  world '.strip())  # Strip leading and trailing whitespace

xs = [3, 1, 2]      # Create a list
print(xs, xs[2])
print(xs[-1])       # Negative indices count from the end of the list; print "2"
ys = xs
ys[2] = 'aloha'     # Changes in 'ys' also change in 'xs', use .copy() to copy separate
print(xs)
print(ys)
xs.append('level')  # Add a new element to the end of the list
print(xs)
print(ys)

# Slicing
nums = list(range(5))       # range - a built-in function that creates a list of integers
print(nums)
print(nums[2:4])            # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])             # Get a slice from index 2 to end; prints "[2, 3, 4]"
print(nums[:2])             # Prints "[0, 1]"
print(nums[:])              # Get a slice of the whole list
print(nums[:-1])            # Get a slice except the last element
nums[2:4] = [8, 9]          # Assign a new sublist to a slice
print(nums)

# Loops
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

# Print element with index
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

# List comprehension
squares = [x ** 2 for x in nums]
print(squares)

# List comprehension can contain conditions
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)


# Dictionaries
d = {'cat': 'cute', 'dog': 'furry'}     # Create a new dictionary with some data
print(d['cat'])             # Get an entry from a dictionary; prints "cute"
print('cat' in d)           # Check if a dictionary has a given key; prints "True"

d['fish'] = 'wet'           # Set an entry in a dictionary
print(d['fish'])            # Prints "wet"
print(d)
#print(d['monkey'])  # KeyError: 'monkey' not a key of d

print(d.get('monkey', 'N/A'))   # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))     # Get an element with a default; prints "wet"
print(d)   

del d['fish']                   # Remove an element from a dictionary
print(d.get('fish', 'N/A'))     # "fish" is no longer a key; prints "N/A"

# Iterate over the keys in a dictionary
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A {} has {} legs'.format(animal, legs))

# Dictionary comprehension
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)


# Sets - an unordered collection of distinct elements
animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')      # Add an element to a set
print('fish' in animals)
print(len(animals))       # Number of elements in a set 
animals.add('cat')       # Adding an element that is already in the set does nothing
print(len(animals))       
animals.remove('cat')    # Remove an element from a set
print(len(animals))       

# Same syntax to iterate over a set as over a list. But a set is unordered, we can not
# make assumptions about the order in which you visit the elements of the set
# Each run will be a different order
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))

# Set comprehension
from math import sqrt
print({int(sqrt(x)) for x in range(30)})


# Tuples:
#    is an (immutable) ordered list of values. 
#    can be used as keys in dictionaries and as elements of sets, while lists cannot
d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)       # Create a tuple
print(type(t))
print(d[t])       
print(d[(1, 2)])
# t[0] = 1        # Error: as 'tuple' object does not support item assignment


# Functions
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

# Define functions to take optional keyword arguments:
for x in [-1, 0, 1]:
    print(sign(x))

def hello(name, loud=False):
    if loud:
        print('HELLO, {}'.format(name.upper()))
    else:
        print('Hello, {}!'.format(name))

hello('Bob')
hello('Fred', loud=True)


# Classes
class Greeter:

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
          print('HELLO, {}'.format(self.name.upper()))
        else:
          print('Hello, {}!'.format(self.name))

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"


### Numpy ###
import numpy as np

# Arrays
a = np.array([1, 2, 3])  # Create a rank 1 array
print(type(a), a.shape, a[0], a[1], a[2])
a[0] = 5                 # Change an element of the array
print(a) 
b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print(b)
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])
a = np.zeros((2,2))  # Create an array of all zeros
print(a)
b = np.ones((1,2))   # Create an array of all ones
print(b)
c = np.full((2,2), 7) # Create a constant array
print(c)
d = np.eye(2)        # Create a 2x2 identity matrix
print(d)
e = np.random.random((2,2)) # Create an array filled with random values
print(e)

# Array indexing
# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)

print(a[0, 1])
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1], updating b automatically updating a
print(a[0, 1])

# Create the following rank 2 array with shape (3, 4)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

### Important ###
# Mixing integer indexing with slices yields an array of lower rank, 
# while using only slices yields an array of the same rank as the original array
row_r1 = a[1, :]    # Rank 1 view of the second row of a  
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
row_r3 = a[[1], :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
print(row_r3, row_r3.shape)

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print()
print(col_r2, col_r2.shape)

# 
a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and 
print(a[[0, 1, 2], [0, 1, 0]])

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))

# When using integer array indexing, you can reuse the same element from the source array:
print(a[[0, 0], [1, 1]])

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))

# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"
print(np.arange(4))

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10
print(a)

# Boolean array indexing: 
# Boolean array indexing lets you pick out arbitrary elements of an array. 
# Frequently this type of indexing is used to select the elements of an array that satisfy some condition.

a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                    # this returns a numpy array of Booleans of the same
                    # shape as a, where each slot of bool_idx tells
                    # whether that element of a is > 2.
print(bool_idx)

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])

# We can do all of the above in a single concise statement:
print(a[a > 2])

# Data type
x = np.array([1, 2])  # Let numpy choose the datatype
y = np.array([1.0, 2.0])  # Let numpy choose the datatype
z = np.array([1, 2], dtype=np.int64)  # Force a particular datatype
print(x.dtype, y.dtype, z.dtype)

# Array math
# Basic mathematical functions operate elementwise on arrays, 
# available both as operator overloads and as functions in the numpy module
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

# Use the dot function to compute inner products of vectors, 
# to multiply a vector by a matrix, and to multiply matrices.
# 'dot' is available both as a function in the numpy module, 
# and as an instance method of array objects
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# the @ operator is equivalent to numpy's dot operator
print(v @ w)

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
print(x @ v)

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
print(x @ y)

# Useful function in Numpy
x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

# To transpose a matrix, simply use the T attribute of an array object
print(x)
print("transpose\n", x.T)

v = np.array([[1,2,3]])
print(v )
print("transpose\n", v.T)


# Broadcasting - a powerful mechanism that allows numpy 
# to work with arrays of different shapes when performing arithmetic operations
# Ex: 
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)

# When the matrix x is very large, computing an explicit loop in Python could be slow
# Can use stacking and summing:
vv = np.tile(v, (4, 1))  # Stack 4 copies of v on top of each other
print(vv)                # Prints "[[1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]]"

y = x + vv  # Add x and vv elementwise
print(y)

# Broadcasting: perform this computation without actually creating multiple copies of v
# Broadcasting typically makes your code more concise and faster, so you should strive to use it where possible.
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)

# Broadcasting two arrays together follows these rules:
# 1. If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
# 2. The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.
# 3. The arrays can be broadcast together if they are compatible in all dimensions.
# 4. After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
# 5. In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension

# Compute outer product of vectors
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
print(np.reshape(v, (3, 1)) * w)

# Add a vector to each row of a matrix
x = np.array([[1,2,3], [4,5,6]])
# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
# giving the following matrix:
print(x + v)

# Add a vector to each column of a matrix
# x has shape (2, 3) and w has shape (2,).
# If we transpose x then it has shape (3, 2) and can be broadcast
# against w to yield a result of shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column. Gives the following matrix:
print((x.T + w).T)


# Another solution is to reshape w to be a column vector of shape (2, 1);
# we can then broadcast it directly against x to produce the same
# output.
print(x + np.reshape(w, (2, 1)))

# Multiply a matrix by a constant:
# x has shape (2, 3). Numpy treats scalars as arrays of shape ();
# these can be broadcast together to shape (2, 3), producing the
# following array:
print(x * 2)


