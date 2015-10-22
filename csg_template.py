import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math
from sympy.solvers.polysys import solve_triangulated
from sympy.abc import x, y, z

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
        def equations(p):
            x,y=p
            return (self.A*x**2+self.B*y**2+self.C*x*y+self.D*x +self.E*y+self.F, (x-r.origin.x)*r.direction.y-(y-r.origin.y)*r.direction.x)
        x,y= fsolve(equations,(0,0))

        return equations((x,y))
            
            
        """Where does the node intersect the ray?"""
        raise NotImplementedError

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
        
    def intersections(self, r) :
        def equations(p):
            x,y=p
            return (self.A*x**2+self.B*y**2+self.C*x*y+self.D*x +self.E*y+self.F, (x-r.origin.x)*r.direction.y-(y-r.origin.y)*r.direction.x)
        x,y= fsolve(equations,(0,0))

        return x,y
#    def intersections(self, r) :

        
        
class QuadraticSurface(Surface) :
    
    def __init__(self, A, B, C, D, E, F) :
        self.A,self.B,self.C,self.D,self.E,self.F=A,B,C,D,E,F
    
    def intersections(self, r) :
        pass
        
    def f(self, p) :
        function=self.A*p.x**2+self.B*p.y**2+self.C*p.x*p.y+self.D*p.x +self.E*p.y+self.F
        return function

class PlaneV(object):
    def __init__(self, a):
        self.a=a
        
    def f(self,p):
        function=self.a-p.x
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
          
    def intersections(self, r) :
        pass
        
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
        
