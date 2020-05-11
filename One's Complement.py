from __future__ import annotations
from typing import Union
from typeguard import typechecked

from numpy import uint8
from numbers import Integral, Number

@typechecked
class OneComp(Number):  # (Integral): # Tooo many to implement

    def __init__(self, number: Union[Integral, OneComp]):
        if isinstance(number, Integral):
            if number < 0:
                self.number = uint8(255 + number)
            else:
                self.number = uint8(number)
        elif isinstance(number, OneComp):
            self.number = number.number
        else:
            raise NotImplementedError()

    def __neg__(self) -> OneComp:
        if isinstance(self, OneComp):
            return OneComp(~self.number)
        else:
            raise NotImplementedError()

    def __add__(self, other: OneComp) -> OneComp:
        if isinstance(other, OneComp):
            sum = uint8(int(self.number) + int(other.number))
            if sum < 128:
                if self.number < 128 and other.number < 128:
                    return OneComp(sum)
                else:
                    return OneComp(sum + 1)
            else:
                if self.number >= 128 and other.number >= 128:
                    return -OneComp(-(sum + 1))
                else:
                    return -OneComp(-int(sum))
        else:
            raise NotImplementedError()

    def __sub__(self, other: OneComp) -> OneComp:
        if isinstance(other, OneComp):
            return self + (-other)
        else:
            raise NotImplementedError()

    def __mul__(self, other: OneComp) -> OneComp:
        if self.number >= 128 and other.number >= 128:
            return OneComp((255 - self.number) * (255 - other.number))
        elif self.number >= 128 and other.number < 128:
            return -OneComp((255 - self.number) * other.number)
        elif self.number < 128 and other.number >= 128:
            return -OneComp(self.number * (255 - other.number))
        else:
            return OneComp(self.number * other.number)

    def __floordiv__(self, other: OneComp) -> OneComp:
        if isinstance(other, OneComp):
            if self.number >= 128 and other.number >= 128:
                return OneComp((255 - self.number) // (255 - other.number))
            elif self.number >= 128 and other.number < 128:
                return -OneComp((255 - self.number) // other.number)
            elif self.number < 128 and other.number >= 128:
                return -OneComp(self.number // (255 - other.number))
            else:
                return OneComp(self.number // other.number)
        else:
            raise NotImplementedError()

    def __str__(self) -> str:
        if self.number >= 128:
            return '-' + str(255 - self.number)
        else:
            return str(self.number)

    def __repr__(self) -> str:
        if self.number >= 128:
            return bin(self.number)[2:]
        else:
            return '0'*(8-len(bin(self.number)[2:])) + bin(self.number)[2:]


def test():
    v1t1 = OneComp(20) + OneComp(5)
    v1t2 = OneComp(20) - OneComp(5)
    v1t3 = OneComp(20) * OneComp(5)
    v1t4 = OneComp(20) // OneComp(5)

    v2t1 = OneComp(-20) + OneComp(5)
    v2t2 = OneComp(-20) - OneComp(5)
    v2t3 = OneComp(-20) * OneComp(5)
    v2t4 = OneComp(-20) // OneComp(5)

    v3t1 = OneComp(20) + OneComp(-5)
    v3t2 = OneComp(20) - OneComp(-5)
    v3t3 = OneComp(20) * OneComp(-5)
    v3t4 = OneComp(20) // OneComp(-5)

    v4t1 = OneComp(-20) + OneComp(-5)
    v4t2 = OneComp(-20) - OneComp(-5)
    v4t3 = OneComp(-20) * OneComp(-5)
    v4t4 = OneComp(-20) // OneComp(-5)

    print(v1t1, repr(v1t1))
    print(v1t2, repr(v1t2))
    print(v1t3, repr(v1t3))
    print(v1t4, repr(v1t4), '\n')

    print(v2t1, repr(v2t1))
    print(v2t2, repr(v2t2))
    print(v2t3, repr(v2t3))
    print(v2t4, repr(v2t4), '\n')

    print(v3t1, repr(v3t1))
    print(v3t2, repr(v3t2))
    print(v3t3, repr(v3t3))
    print(v3t4, repr(v3t4), '\n')

    print(v4t1, repr(v4t1))
    print(v4t2, repr(v4t2))
    print(v4t3, repr(v4t3))
    print(v4t4, repr(v4t4), '\n')


if __name__ == '__main__':
    v1 = OneComp(-20)
    v2 = OneComp(-5)
    v3 = v1 + v2
    v4 = v1 - v2
    v5 = v1 * v2
    v6 = v1 // v2
    print(v1, v2, v3, v4, v5, v6)
    print(repr(v1), repr(v2), repr(v3), repr(v4), repr(v5), repr(v6), '\n')

test()
