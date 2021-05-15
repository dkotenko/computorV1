from Printer import Printer
from const import EPSILON

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
        if d > 0:
            x1 = (-b + self.squareRoot(d)) / (2 * a)
            x2 = (-b - self.squareRoot(d)) / (2 * a)
            Printer.print_positive(x1, x2)
        elif d == 0 or d < 0:
            x1 = (-b / (2 * a))
            Printer.print_zero(x1)
        elif d < 0:
            b_calc = f'{(-b / (2 * a)):.6f}'
            x1 = f'{b_calc} + {self.squareRoot(d)} * i'
            x2 = f'{b_calc} - {self.squareRoot(d)} * i'
            Printer.print_negative(x1, x2)

    def solve(self):
        Printer.print_reduced_form(self.data)
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