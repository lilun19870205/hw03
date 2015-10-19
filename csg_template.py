import numpy as np
import matplotlib.pyplot as plt

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
    def __init__(self,x,y):
        self.x,self.y = x,y
    
    def contains(self, p) :
        if self.x == p.x and self.y == p.y:
            print "true,it is contained"
        else:
            print "false, it is not contained"
            
        """Does the node contain the point?"""
#        raise NotImplementedError

    def intersections(self, r) :
        norm=np.sqrt((self.x-r.origin.x)**2+(self.y-r.origin.y)**2)
        if (norm==0):
            result=1
        elif (self.x-r.origin.x)/norm==r.direction.x and \
        (self.y-r.origin.y)/norm==r.direction.y:
            result=1
        else:
            result=0
        return result
            
            
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
class Union()
        
class Surface(object) :
    
    def f(self, p) :
        raise NotImplementedError
        
    def intersections(self, r) :
        raise NotImplementedError
        
        
class QuadraticSurface(Surface) :
    
    def __init__(self, A=0.0, B=0.0, C=0.0, D=0.0, E=0.0, F=0.0) :
        pass
    
    def intersections(self, r) :
        pass
        
    def f(self, p) :
        pass
               

               
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
        
