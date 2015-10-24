import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

class Point(object) :

    def __init__(self, x, y) :
        self.x, self.y = x, y
    
    def __str__(self) :
        return "Point(%.6F, %.6f) " % (self.x, self.y)

    def __add__(self,other):
        return "Point(%.6F, %.6f) " % (self.x + other.x, self.y + other.y)
    
    def __mul__(self,other):
        return "Point(%.6F, %.6f) " % (self.x * other, self.y * other)
        

      
class Ray(object) :
    
    def __init__(self, origin, direction) :
        self.origin = origin
        # ensure the direction is normalized to unity, i.e., cos^2 + sin^2 = 1
        norm = np.sqrt(direction.x**2 + direction.y**2)
        self.direction = Point(direction.x/norm, direction.y/norm)
            
    def __str__(self) :
        return "Ray: r_0(%10.6f, %10.6f), d(%.6f %.6f) " % \
               (self.origin.x, self.origin.y, self.direction.x, self.direction.y)

class Node(object) :
    def __init__(self,x):
        self.x=x
    
    def contains(self, p) :
        if (self.x.f(p))<=0:
            result=1
        else:
            result=0
        return result
            
        """Does the node contain the point?"""
#        raise NotImplementedError



    def intersections(self, r) :
        if (self.x.intersections(r))>=0:
            print "true"
            result=1
        else:
            print "false"
            result=0
        return result

            

class Primitive(Node) :
    
    def __init__(self, surface, sense) :
        self.surface, self.sense = surface, sense
        
    def contains(self, p) :
        return (self.surface.f(p) < 0) == self.sense
        
    def intersections(self, r) :
        return self.surface.intersections(r)
        

class Operator(Node) :
    
    def __init__(self, L, R) :
        self.L, self.R = L, R
        
    def contains(self, p) :
        raise NotImplementedError

    def intersections(self, r) :
        # get intersections with left and right nodes
        pointsL = self.L.intersections(r)
        pointsR = self.R.intersections(r)
        # return the concatenated result
        return pointsL + pointsR
      
# INSERT UNION AND INTERSECTION CLASSES
class Union(Node):
    def __init__(self,L,R):
        self.L,self.R=L,R
    def contains(self,p):
        pointsL = self.L.contains(p)
        pointsR = self.R.contains(p)
        if (pointsL + pointsR)>=1:
            print "true"
            result=1
        else:
            print "false"
            result=0
        return result
        
class Intersection(Node):
    def __init__(self,L,R):
        self.L,self.R=L,R
    def contains(self,p):
        pointsL = self.L.contains(p)
        pointsR = self.R.contains(p)
        if (pointsL + pointsR)==2:
            print "true"
            result=1
        else:
            print "false"
            result=0
        return result


class Surface(object) :
    def __init__(self, A, B, C, D, E, F):
        self.A,self.B,self.C,self.D,self.E,self.F=A,B,C,D,E,F
    
    def f(self, p) :
        function=self.A*p.x**2+self.B*p.y**2+self.C*p.x*p.y+self.D*p.x +self.E*p.y+self.F
        return function
    
    def string(self):
        string='self.A*x**2+self.B*y**2+self.C*x*y+self.D*x +self.E*y+self.F'
        return string
        
    def contains(self,p):
        if self.f(p)<=0:
            result=1
        else:
            result=0
        return result
            
        
    def intersections(self, r) :
        M=np.array([[2*self.A,self.C,self.D],[self.C,2*self.B,self.E],[self.D,self.E,2*self.F]])
        r0t=np.array([r.origin.x,r.origin.y,1.])
        r0=r0t.transpose()
        dt=np.array([r.direction.x,r.direction.y,1.])
        d=dt.transpose()
        
        a=dt.dot(M).dot(d)
        b=2*r0t.dot(M).dot(d)
        c=r0t.dot(M).dot(r0)
        print a, b, c
        

        return b**2-4*a*c
#    def intersections(self, r) :

        
        
class QuadraticSurface(Surface) :
    
    def __init__(self, A, B, C, D, E, F) :
        self.A,self.B,self.C,self.D,self.E,self.F=A,B,C,D,E,F
    
    def f(self, p) :
        function=self.A*p.x**2+self.B*p.y**2+self.C*p.x*p.y+self.D*p.x +self.E*p.y+self.F
        return function
    
        
    def intersections(self, r) :
        M=np.array([[2*self.A,self.C,self.D],[self.C,2*self.B,self.E],[self.D,self.E,2*self.F]])
        r0t=np.array([r.origin.x,r.origin.y,1.])
        r0=r0t.transpose()
        dt=np.array([r.direction.x,r.direction.y,1.])
        d=dt.transpose()
        
        a=dt.dot(M).dot(d)
        b=2*r0t.dot(M).dot(d)
        c=r0t.dot(M).dot(r0)
        print a, b, c
        
        if (b**2-4*a*c)>=0:
            print "intersection is true"
            result=1
        else:
            print "intersection is false"
            result=0
        
        return result

class PlaneV(object):
    def __init__(self, a):
        self.a=a
        
    def f(self,p):
        function=p.x-self.a
        return function
        
class PlaneH(object):
    def __init__(self,a):
        self.a=a
        
    def f(self,p):
        function=p.y-self.a
        return function

class Plane(object):
    def __init__(self,m,b):
        self.m,self.b=m,b
    def f(self,p):
        function=self.m*p.x-p.y+self.b
        return function

class Circle(object):
    def __init__(self,r,a=.0,b=.0):
        super(Circle,self).__init__(A=0,B=0,C=0,D=0,E=0,F=0)
        self.r=r
        self.a=a
        self.b=b
        self.A=1.0
        self.B=1.0
        
    def f(self,p):
        function=(p.x-self.a)**2+(p.y-self.b)**2-self.r**2
        return function

               
class Region(object) :
    
    def __init__(self) :
        self.node = None
    
    def append(self, node=None, surface=None, operation="U", sense=False) :
        assert((node and not surface) or (surface and not node))
        if isinstance(surface, Surface) :
            node = Primitive(surface, sense)
        if self.node is None :
            self.node = node
        else :
            O = Union if operation == "U" else Intersection
            self.node = O(self.node, node)
            
    def contains(self,p):
        if self.node.contains(p)==1:
            result=1
        else:
            result=0
        return result
          
    
    def intersections(self, r) :
        ints=self.node.intersections(r)
        ints.sort(key= lambda p: p.x)
        return ints
        
class Geometry(object) :
    
    # Attributes can be defined in the body of a class.  However, these
    # become "static" values that are the same for every object of the class.
    # Hence, they can be accessed either through object.attribute or 
    # classname.attribute.
    noregion = -1    
    
    def __init__(self,  xmin, xmax, ymin, ymax) :
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.regions = []
        
    def add_region(self, r) :
        self.regions.append(r)

    def find_region(self, p) :
        region = Geometry.noregion
        # look for the region containing p.
        return region
        
    def plot(self, nx, ny) :
        pass
        
