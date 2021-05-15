from os import stat
from ParsingData import ParsingData
from Math import Math
from const import RED, RESET

class Printer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def print_infinity():
        print("Infinity number of solutions")
        print('=' * 100)

    @staticmethod
    def print_no():
        print("No solution")
        print('=' * 100)
    
    @staticmethod
    def print_negative(x1, x2):
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(x1)
        print(x2)
        print('=' * 100)

    @staticmethod
    def print_positive(x1, x2):
        print("Discriminant is strictly positive, the two solutions are:")
        print(f'{x1:.6f}')
        print(f'{x2:.6f}')
        print('=' * 100)

    @staticmethod
    def print_zero(x1):
        print("The solution is:")
        print(f'{x1:.6f}')
        print('=' * 100)

    @staticmethod
    def print_reduced_form(data: ParsingData):
        print('Reduced form: ', end='')
        x2_val = f'{data.x2:.10f}'.rstrip('0').rstrip('.')
        print(f'{x2_val} * X^2', end = '')

        print(' + ' if data.x1 >= 0 else ' - ', end = '')
        x1_val= Math.abs(data.x1)
        x1_str = f'{x1_val:.10f}'.rstrip('0').rstrip('.')
        print(f'{x1_str} * X^1', end = '')
        
        print(' + ' if data.c >= 0 else ' - ', end = '')
        c_val = Math.abs(data.c)
        c_str = f'{c_val:.10f}'.rstrip('0').rstrip('.')
        print(f'{c_str} * X^0', end = '')
        print(' = 0')

    @staticmethod
    def print_error(text):
        print(f"{RED}Error: ", end='')
        print(text, RESET, end='')
        return False

        