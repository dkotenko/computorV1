from const import EPSILON

class Math:
    @staticmethod
    def abs(n):
        if n < 0: n *= -1
        return n

    @staticmethod
    def is_equal(n, m):
        if Math.abs(m - n) < EPSILON:
            return True
        return False

    @staticmethod
    def division_protected(value, divider):
        if not divider:
            print("division by zero error")
        return value / divider

    @staticmethod
    def modulo_protected(value, divider):
        if not divider:
            print("modulo by zero error")
        return value % divider

    @staticmethod
    def div_wholenum_protected(value, divider):
        if not divider:
            print("modulo by zero error")
        return value // divider

    