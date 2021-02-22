# A class packs together a set of variables and a set of functions
# All functions can access all variables

# 1. To encapsulate variables and functions in logical units such that
#    a larger program can be composed by combining such units (classes)

# In classes, functions are called 'methods', variables are called 'attributes'
# Here is a trivial class that has 01 variable 'a' and 01 function 'dump' that writes the contents of 'a':
class Trivial:
    def __init__(self, a):
        self.a = a
    
    def dump(self):
        print(self.a)

# HOW TO USE THIS CLASS:
# First, must make an 'instance' (object) of the class:
t = Trivial(a=4)
# Trivial(a=4) implies a call to the __init__ method (function) with 4 as the value of the argument 'a'
# Inside __init__, we store the value of 'a' as an attribute in the class: self.a
# If there were several methods in the class, all of them could then access self.a
#       (as if 'a' were some global variable in the class)
# the __init__ functions is called a constructor since it is used to construct an instance (object) of the class.

# Having an instance 't' of class 'Trivial', we can call the 'dump' method as follows:
t.dump()

# Even though both __init__ and 'dump' have 'self' as first argument, this argument is not used in a call
# The 'self' argument. It takes time and experience to understand the 'self' argument in class methods.
# 1. 'self' must always be the first argument.
# 2. 'self' is never used in calls.
# 3. 'self' is used to access attributes and methods inside methods.