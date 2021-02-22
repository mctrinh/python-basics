class Distance:
    def __init__(self, v0, a):
        self.v0 = v0
        self.a = a
    
    def __call__(self, t):
        v0, a = self.v0, self.a         # make local variables
        return v0*t + 0.5*a*t**2

# The class has 02 methods (functions).
# The name of a method can be freely chosen by the programmer.
# But here, we use 03 special names, starting and ending with double underscores,
#           which allows us to use special attractive syntax in the calls.
#           Such methods are known as special methods.
# The constructor __init__ has 01 purpose: storing data in class attributes (self.v0 and self.a) 
#           We can then access these data in class methods.
# The __call__ method is used to evaluate s(t). It has 01 argument ('self' does not count since it is never used in calls).
#           Allow us to view a class instance as if were a function.
s = Distance(v0=2, a=0.5)       # create instance
v = s(t=0.2)                    # runs s.__call__(t=0.2)
# Magic: 's' is a class instance, not a function, but still can write s(t=0.2) or s(0.2) as if s were a function.
#         This is the purpose of the special method __call__: to allow such syntax.
# Nice: 's' looks like a function, it takes 01 argument 't', as the mathematical function s(t),
#       but is also contains values of the 2 parameters 'v0' and 'a'

# In general, for a function f(x,y,z;p1,p2,...,pn) with 3 independent variables & n parameters p1,p2,...,pn
#             we can pack the function and the parameters together in a class:
class F:
    def __init__(self, p1, p2, ...):
        self.p1 = p1
        self.p2 = p2
        ...
    
    def __call__(self, x, y, z):
        # return formula involving x, y, z and self.p1, self.p2, ...

# The f function is initialized by
f = F(p1=..., p2=..., ...)
# And later called as f(x, y, z)