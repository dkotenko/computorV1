from os import stat
from ParsingData import ParsingData
from Math import Math
from const import RED, RESET
from const import Mode
import re

class Printer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def print_endline():
        if Mode.VERBOSE_MODE:
            print('=' * 100)

    @staticmethod
    def print_infinity():
        print("Infinity number of solutions")
        Printer.print_endline()

    @staticmethod
    def print_no():
        print("No solution")
        Printer.print_endline()
    
    @staticmethod
    def print_negative(x1, x2):
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(x1)
        print(x2)
        Printer.print_endline()

    @staticmethod
    def print_positive(x1, x2):
        print("Discriminant is strictly positive, the two solutions are:")
        print(Printer.get_float_string(x1))
        print(Printer.get_float_string(x2))
        Printer.print_endline()

    @staticmethod
    def print_zero(x1):
        print("The solution is:")
        print(Printer.get_float_string(x1))
        Printer.print_endline()

    @staticmethod
    def print_reduced_form(line: str):

        def get_values(part, sign, d):

            def add_to_dict(d, value, degree, sign):
                if degree in d:
                    d[degree] += (value * sign)
                else:
                    d[degree] = (value * sign)

            def add_number(d, token, sign):
                value = float(token)
                degree = 0
                add_to_dict(d, value, degree, sign)

            def add_var(d, token, sign):
                if token.find('*') > -1:
                        value = float(token.split('*')[0])
                else:
                    value = 1
                if token.find('^') > -1:
                    degree = int(token.split('^')[1])
                else:
                    degree = 1
                add_to_dict(d, value, degree, sign)

            splitted_by_plus_minus = re.split(r"\+|\-", part)
            for token in splitted_by_plus_minus:
                if not token:
                    continue
                if token.find('x') > -1:
                    add_var(d, token, sign)    
                else:
                    add_number(d, token, sign)

        by_equity_sign = line.split('=')
        left, right = by_equity_sign
        d = {}
        get_values(left, 1, d)
        get_values(right, -1, d)
        i = 0

        print('Reduced form: ', end='')
        for key in sorted(list(d.keys())):
            if d[key] == 0:
                continue
            if i:
                sign_symbol = '+' if d[key] > -1 else '-'
                print(f' {sign_symbol} ', end='')
            value_str = Printer.get_float_string(Math.abs(d[key]))
            print(f'{value_str} * X^{key}',end='')
            i += 1
        print(' = 0')

   
    @staticmethod
    def print_greater_degree():
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        Printer.print_endline()

    @staticmethod
    def print_error(text):
        print(f"{RED}Error: ", end='')
        print(text, RESET)
        Printer.print_endline()
        return False

    @staticmethod
    def get_float_string(value):
        return f'{value:.6f}'.rstrip('0').rstrip('.')

        