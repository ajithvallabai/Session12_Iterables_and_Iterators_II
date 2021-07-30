import math
from typing import NamedTuple

class Polygon:
    """
    A polygon class is formed with a input of edges and circum radius. 
    """
    def __init__(self, n, R):
        """
        :param edges: edges of a polygon
        :type edges: int
        :param circum_radius: circum radi of polygon
        :type circum_radius: int
        :return func: 
        """
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self.edges = n
        self.circumradius = R
        
    def __repr__(self) -> 'str':
        """
        Gives a name to class
        :return str: 
        """
        return f'Polygon(n={self._edges}, R={self._circumradius})'
   
    @property
    def edges(self) -> 'int':
        """
        Edges of polygon
        :return int
        """
        return self._edges

    @edges.setter
    def edges(self, n) -> None:
        """
        Sets edges and initates None for other properties
        """
        self._edges = n
        self._area = None
        self._count_vertices = None
        self._count_edges = None 
        self._interior_angle = None
        self._side_length = None
        self._apothem = None 
        self._perimeter = None 
    
    @property
    def circumradius(self) -> 'int':
        """
        Circumradius is returned
        :return int
        """
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self, R) -> None:
        """
        Circumradius is set
        :return int
        """
        self._circumradius = R

    @property
    def area(self) -> 'int':
        """
        Calculates area lazyly
        :return int
        """
        if self._area is None:
            self._area = self._edges / 2 * self.side_length * self.apothem
        return self._area
    
    
    @property
    def count_vertices(self) -> 'int':
        """
        Calculates vertices lazyly and returns
        :return int
        """
        if self._count_vertices is None:
           self._count_vertices =  self._edges
        return self._count_vertices
    
    @property
    def count_edges(self) -> 'int':
        """
        Calculates edges lazyly and returns
        :return int
        """
        if self._count_edges is None:
           self._count_edges =  self._edges
        return self._count_edges

    @property
    def interior_angle(self) -> 'int':
        """
        Calculates interior_angle lazyly and returns
        :return int
        """
        if self._interior_angle is None:
            self._interior_angle = (self._edges - 2) * 180 / self._edges
        return self._interior_angle
        
    @property
    def side_length(self) -> 'int':
        """
        Calculates side_length lazyly and returns
        :return int
        """
        if self._side_length is None:
            self._side_length = 2 * self._circumradius * math.sin(math.pi / self._edges)
        return self._side_length
        
    @property
    def apothem(self) -> 'int':
        """
        Calculates apothem lazyly and returns
        :return int
        """
        if self._apothem is None:
            self._apothem = self._circumradius * math.cos(math.pi / self._edges)
        return self._apothem
            
    
    @property
    def perimeter(self) -> 'int':
        """
        Calculates perimeter lazyly and returns
        :return int
        """
        if self._perimeter is None:
            self._perimeter = self._edges * self.side_length
        return self._perimeter
            
    def __eq__(self, other):
        """
        Checks equalvalance of latter object
        :return bool
        """
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        """
        Checks if input is greater than current
        :return bool
        """
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented

from collections import namedtuple
Poly = namedtuple('PolygonTuples','Polys')



class Polygons:
    """
    Implemented iteratables and lazy calculation without using list as storage
    """
    def __init__(self, m, R):
        """
        Initalizing variables
        """
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R        
        self._length = None
        self._max_eff = 0

    def __len__(self) -> 'int':
        """
        Setting properties
        """
        if self._length is None:
           self._length =  self._m - 2
        return self._length
        
    def __repr__(self) -> 'str':
        """
        String representation of class
        :return str
        """
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __iter__(self) -> 'object':
        """
        iterable for a class
        :return object
        """
        return self.PolygonIterator(self._m, self._R)

    def __reversed__(self) -> 'object':
        """
        Reverse and iterate
        :return object
        """
        return self.PolygonIterator(self._m, self._R, reverse=True)
        
    @property
    def eff(self, n) -> 'int':
        """
        Setting efficiency property from PolygonIterator
        """
        self._max_eff = n 
        return self._max_eff


    class PolygonIterator:
        """
        PolygonIterator class helps in behaviour of iteratable and iterator
        """
        def __init__(self, ed, Radi, *, reverse=False) -> None:            
            self.ed = ed
            self.Radi = Radi
            self.reverse = reverse 
            self.length = ed
            self.i = 0
            self.curr_poly = 3
            self.max_efficient = 0 
        
        def __iter__(self) -> 'object':
            """
            Iterator
            :return self
            """            
            return self 
        

        def __next__(self) -> 'object':
            """
            Helps to iterate
            :return iterables
            """            
            if self.curr_poly > self.ed:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - self.i
                    self.i += 1                    
                else:
                    index = self.curr_poly
                item = Polygon(index, self.Radi)
                curr_efficiency = item.area/item.perimeter
                if curr_efficiency > self.max_efficient:
                    self.max_efficient = curr_efficiency
                    self.max_eff_poly_id = index
                Polygons.eff = self.max_eff_poly_id
                self.curr_poly += 1              
                return Poly(item)