from const import EPSILON

class Math:
    @staticmethod
    def abs(n):
        if n < 0: n *= -1
        return n

    