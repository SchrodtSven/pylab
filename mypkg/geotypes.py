# Demo class using
#   - dunder methods (incl. operator overloading)
#   - type aliases
#   - @property decorators
# AUTHOR Sven Schrodt
# SINCE 2026-01-23


type Point = tuple[float, float]  # type alias for a 2d point (x, y)


class Rect:
    """
    Defining a rectangle, allowing operations
    - calculating width, height, area
    - defining dunder functions for usage of operators
        - +,-,>,<,>=,<=
    """

    _lb = (0, 0)
    _rt = (0, 0)
    w = 0
    h = 0
    a = 0

    def __init__(self, lb: Point = 0, rt: Point = 0):
        """
        Initialize

        :param self:
        :param lb: left bottom point of rectangle
        :type lb: Point
        :param rt: right top point of rectangle
        :type rt: Point
        """

        # FIXME ->implement Rect.sanitize()
        self.rt = rt
        self.lb = lb
        self.calc()

    def calc(self):
        '''
        Calculationg width, height and area of rectangle basing on let bottom and right top egdes' coordinates
        
        :param self: Beschreibung
        '''
        self.w = self.rt[0] - self.lb[0]
        self.h = self.rt[1] - self.lb[1]
        self.a = self.h * self.w

    def __str__(self) -> str:
        return f"""
        left bottom: {self.lb[0]}, {self.lb[1]}
        right top: {self.rt[0]}, {self.rt[1]}
        width: {self.w}
        height: {self.h}
        area: {self.a}
        """

    def __repr__(self) -> str:
        return (
            self.__class__.__qualname__
            + f"""
        lb: ({self.lb[0]}, {self.lb[1]})
        rt: ({self.rt[0]}, {self.rt[1]})
        w: {self.w}
        h: {self.h}
        a: {self.a}
        """
        )

    def __add__(self, other: Rect) -> float:
        """
        Returning combined area

        :param self: self
        :param other: other instance
        :type other: Rect
        :rtype: float
        """
        return self.a + other.a

    def __sub__(self, other: Rect) -> float:
        """
        Returning difference between areas

        :param self: self
        :param other: other instance
        :type other: Rect
        :rtype: float
        """
        return abs(self.a - other.a)

    def __gt__(self, other: Rect) -> bool:
        """
        Check, if this instance's area is greater than other instance's area

        :param self: self
        :param other: other instance
        :type other: Rect
        :rtype: bool
        """
        return self.a > other.a

    def __lt__(self, other: Rect) -> bool:
        """
        Check, if this instance's area is less than other instance's area

        :param self: self
        :param other: other instance
        :type other: Rect
        :rtype: bool
        """
        return self.a < other.a

    def __le__(self, other: Rect) -> bool:
        """
        Check, if this instance's area is less than or equal other instance's area

        :param self: self
        :param other: other instance
        :type other: Rect
        :rtype: bool
        """
        return self.a <= other.a

    def __ge__(self, other: Rect) -> bool:
        """
        Check, if this instance's area is greater than or equal other instance's area

        :param self: self
        :param other: other instance
        :type other: Rect
        :rtype: bool
        """
        return self.a >= other.a



    # Property decorators assurring, that depending attribute will be re-claculated 

    @property
    def lb(self):
        return self._lb

    @lb.setter
    def lb(self, value):
        self._lb = value
        self.calc()


    @property
    def rt(self):
        return self._rt

    @rt.setter
    def rt(self, value):
        self._rt = value
        self.calc()



if __name__ == "__main__":
    foo = Rect((2.3, 8.1), (4.11, 12.24))
    print(foo)
    print(repr(foo))
    print(foo.__class__.__name__)
    print(foo.__class__.__qualname__)
