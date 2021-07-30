### Session 12 - Iterables and Iterators - II

Google Colab implementation - [here](https://colab.research.google.com/drive/10Ou_lKkizRuKMmykHUsgkmjPh-ERqfgm?usp=sharing)

**Polygon**

A polygon class is formed with a input of edges and circum radius. 

```
@property
def edges(self) -> 'int':    
    return self._edges

@edges.setter
def edges(self, n) -> None:    
    self._edges = n

```
Edges are set using property decorator and setter. it helps us to call edges like a variable

```
@property
def area(self) -> 'int':
    """
    Calculates area lazyly
    :return int
    """
    if self._area is None:
        self._area = self._edges / 2 * self.side_length * self.apothem
    return self._area
```
We are calculating area with lazy properties once its calculated there is no need to caculate again for that instance and it can be used like a variable "object.area"

Same way we are calculating for polygon.interior_angle, polygon.side_length, polygon.apothem, polygon.perimeter


**Polygons**

Implemented iterables and lazy calculation without using list as storage


```
def __iter__(self) -> 'object':
    
    return self.PolygonIterator(self._m, self._R)

class PolygonIterator:
    def __next__(self) -> 'object':               
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
                self.max_eff_poly_id = self.curr_poly
            Polygons.eff = self.max_eff_poly_id
            self.curr_poly += 1              
            return Poly(item)

```

We are passing maxedges and circumradi to PolygonIterator. In polygon iterator __next__() we are using stop iteration if curr_poly is greater then length
for normaliteration we are using the curr_poly number and initalizing a object. Efficiency is also calculated. A polygon named tuple is returned. it is caculated with lazy properties

*reversed()*
For reversed iteration we are calculating in reverse manner with self.length-self.i as index and feeding to Polygon class. A polygon named tuple is returned.
it is done without list as a storage structure

```
@property
    def eff(self, n) -> 'int':
        """
        Setting efficiency property from PolygonIterator
        """
        self._max_eff = n 
        return self._max_eff

```

We are using eff as a variable and self._max_eff is set from PolygonIterator class










