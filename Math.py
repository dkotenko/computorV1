from const import EPSILON
import re
from UnexpectedSymbolError import UnexpectedSymbolError

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

    @staticmethod
    def eval_value(value, expression):
        if re.sub(expression, '', value):
            a = re.sub(expression, '', value)
            position = value.find(a)
            raise UnexpectedSymbolError(a, position)
        

    @staticmethod
    def eval_float(value):
        if str(value).find('.') == -1:
            Math.eval_int(value)
        else:
            r = r'\-?\d+\.?\d+'
            Math.eval_value(value, r)
        return float(value)

    @staticmethod
    def eval_int(value):
        r = r'\-?\d+'
        Math.eval_value(value, r)
        return int(value)

    