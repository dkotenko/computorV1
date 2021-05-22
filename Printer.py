from const import GREEN, RED, RESET, YELLOW
from const import Mode

class Printer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def print_endline():
        if Mode.VERBOSE_MODE:
            print(GREEN, '=' * 100, RESET)


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
    def print_reduced_form(line):
        print(f'{YELLOW}Reduced form: {line}{RESET}')

   
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
        if value == -0.0:
            value = 0.0
        return f'{value:.6f}'.rstrip('0').rstrip('.')

        