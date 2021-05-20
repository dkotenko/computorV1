from re import VERBOSE
from Printer import Printer
from const import EPSILON, Mode
from Math import Math

class Solver():
    def __init__(self, data) -> None:
        self.data = data

    def ft_abs(self, n):
        if n < 0: n *= -1
        return n

    def squareRoot(self, n) :
        x = n
        count = 0 
    
        while (1) :
            count += 1 
            root = 0.5 * (x + (n / x)) 
            if (self.ft_abs(root - x) < EPSILON) :
                break
            x = root
        return root
    pass
    

    def __solve_quadratic(self):
        a = self.data.x2
        b = self.data.x1
        c = self.data.c
        d = b ** 2 - 4 * a * c
        if Mode.VERBOSE_MODE:
            print("Discriminant calculation:")
            print(f"\tD = b ^ 2 - 4ac = {b ** 2} - {4 * a * c} = {d}")
        if d > 0:
            x1 = (-b + self.squareRoot(d)) / (2 * a)
            x2 = (-b - self.squareRoot(d)) / (2 * a)
            if Mode.VERBOSE_MODE:
                print('Roots calculation:')
                print(f'\tx1 = (-b + squareRoot(d)) / (2 * a) = \
                    ({-b} + {self.squareRoot(d)}) / {2 * a}')
                print(f'\tx2 = (-b - squareRoot(d)) / (2 * a) = \
                    ({-b} - {self.squareRoot(d)}) / {2 * a}')
            Printer.print_positive(x1, x2)
        elif d == 0:
            x1 = (-b / (2 * a))
            if Mode.VERBOSE_MODE:
                print('Root calculation:')
                print(f'\tx1 = -b / (2 * a) = {-b} / {2 * a}')
            Printer.print_zero(x1)
        elif d < 0:
            b_float = -b / (2 * a)
            d_str = Printer.get_float_string(
                Math.abs(self.squareRoot(-d) / (2 * a)))
            if not Math.is_equal(b_float, 0):
                b_str = Printer.get_float_string(b_float)
                x1 = f'{b_str} + {d_str} * i'
                x2 = f'{b_str} - {d_str} * i'
            else:
                x1 = f'{d_str} * i'
                x2 = f'-{d_str} * i'
            if Mode.VERBOSE_MODE:
                print('Roots calculation:')
                print(f'\tx1 = -b / (2 * a) + squareRoot(-d) / (2 * a) * i = ', end='')
                print(f'{-b} / ({2*a}) + ', end='')
                print(f'{Printer.get_float_string(self.squareRoot(-d))} / ({2*a}) * i')
                print(f'\tx2 = -b / (2 * a) - squareRoot(-d) / (2 * a) * i = ', end='')
                print(f'{-b} / ({2*a}) - ', end='')
                print(f'{Printer.get_float_string(self.squareRoot(-d))} / ({2*a}) * i')
            Printer.print_negative(x1, x2)

    def solve(self):
        if self.data.x1 == 0 and self.data.x2 == 0:
            if self.data.c == 0:
                Printer.print_infinity() 
            else:
                Printer.print_no()
        elif self.data.x2 == 0:
            Printer.print_zero(- self.data.c / self.data.x1)
        else:
            self.__solve_quadratic()
        return