# Demo class using 
# - dunder methods (incl. operator overloading)
# - type aliases
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-23



type Point = tuple[float, float]

class Rect:
    '''
    Defining a rectangle
    '''

    lb = 0
    rt = 0
    def __init__(self, lb: Point=0, rt: Point=0):
        '''
        Initialize
        
        :param self: 
        :param lb: left bottom point of rectangle
        :type lb: Point
        :param rt: right top point of rectangle
        :type rt: Point
        '''
        self.rt = rt
        self.lb = lb
        self.calc()

    def calc(self):
        self.w = self.rt[0] - self.lb[0]
        self.h = self.rt[1] - self.lb[1]
        self.a = self.h * self.w

    def __str__(self) -> str:
        return f'''
        left bottom: {self.lb[0]}, {self.lb[1]}
        right top: {self.rt[0]}, {self.rt[1]}
        width: {self.w}
        height: {self.h}
        area: {self.a}
        '''
    
    def __repr__(self) -> str:
        return self.__class__.__qualname__ + f'''
        lb: ({self.lb[0]}, {self.lb[1]})
        rt: ({self.rt[0]}, {self.rt[1]})
        w: {self.w}
        h: {self.h}
        a: {self.a}
        '''
    
    def __add__(self, other: Rect) -> float:
        '''
        Returning combined area
        
        :param self: this instance
        :param other: other instance
        :type other: Rect
        :rtype: float
        '''
        return self.a + other.a
    
    def __sub__(self, other: Rect) -> float:
        '''
        Returning difference between areas
        
        :param self: this instance
        :param other: other instance
        :type other: Rect
        :rtype: float
        '''
        return abs(self.a - other.a)
    
    def __gt__(self, other: Rect) -> bool:
        '''
        Check, if this instance's area is greater than other instance's area
        
        :param self: this instance
        :param other: other instance
        :type other: Rect
        :rtype: bool
        '''
        return self.a > other.a
    
    def __lt__(self, other: Rect) -> bool:
        '''
        Check, if this instance's area is less than other instance's area
        
        :param self: this instance
        :param other: other instance
        :type other: Rect
        :rtype: bool
        '''
        return self.a < other.a
    
    def __le__(self, other: Rect) -> bool:
        '''
        Check, if this instance's area is less than or equal other instance's area
        
        :param self: this instance
        :param other: other instance
        :type other: Rect
        :rtype: bool
        '''
        return self.a <= other.a
 
    def __ge__(self, other: Rect) -> bool:
        '''
        Check, if this instance's area is greater than or equal other instance's area
        
        :param self: this instance
        :param other: other instance
        :type other: Rect
        :rtype: bool
        '''
        return self.a >= other.a
 

        

if __name__ == '__main__':
    foo = Rect((2.3,8.1), (4.11,12.24))
    print(foo)
    print(repr(foo))
    print(foo.__class__.__name__)
    print(foo.__class__.__qualname__)