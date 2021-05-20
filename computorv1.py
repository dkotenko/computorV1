from Printer import Printer
from UnexpectedSymbolError import UnexpectedSymbolError
import fileinput
from Parser import Parser
from Solver import Solver
from const import VALID_ARGS, VERBOSE_MODE, TEST_MODE
import sys
import re
from const import Mode
from Validator import Validator

def replace_spaces(line):
    for c in " \t\n":
        line = line.replace(c, "")
    return line

def replace_minus(line):
    while line.find("---") > -1:
        line = line.replace("---", "-")
    line = line.replace("--", "+")
    return line

def do_replace(line):
    line = replace_spaces(line)
    line = replace_minus(line)
    return line.lower()

def check_input_source():
    if len(sys.argv) == 1:
        return
    for filename in sys.argv[1:]:
        if filename in VALID_ARGS:
            if filename == "--test":
                Mode.TEST_MODE = True
            if filename == "--verbose":
                Mode.VERBOSE_MODE = True
            continue
        try:
            f = open(filename)
            f.close()
        except FileNotFoundError:
            Printer.print_error(f"file {filename} not accessible")
            f.close()
            exit()

def get_polynomial_degree(line):
    degree = 0
    matches = re.findall(r"[xX]\^\d+", line)
    for match in matches:
        value = int(match.lstrip('Xx^'))
        if value > degree:
            degree = value
    if not matches:
        matches = re.findall(r"[xX]", line)
        if matches:
            degree = 1
    return degree

def print_polynomial_degree(degree):
    print(f'Polynomial degree: {degree}')

def get_filenames():
    if len(sys.argv) == 1:
        return 0
    filenames = []
    for filename in sys.argv[1:]:
        if filename not in VALID_ARGS:
            filenames.append(filename)
    return filenames

if __name__ == "__main__":
    check_input_source()
    filenames = get_filenames()
    for line in fileinput.input(filenames):
        line = do_replace(line)
        if not len(line):
            continue
        if line == 'exit':
            exit()
        if Mode.VERBOSE_MODE:
            print(f'INPUT: {line}')
        validator = Validator()    
        if not validator.is_valid(line):
            continue
        Printer.print_reduced_form(line)
        polynominal_degree = get_polynomial_degree(line)
        print_polynomial_degree(polynominal_degree)
        if polynominal_degree > 2:
            Printer.print_greater_degree()
            continue
        parser = Parser()
        try:
            data = parser.parse(line)
            if not data:
                continue
            solver = Solver(data)
            solved =  solver.solve()
            if Mode.TEST_MODE:
                pass
        except UnexpectedSymbolError as e:
            text = 'unexpected symbol(s) at position'
            Printer.print_error(f'{text} {e.position}: {e.symbol}')
        parser.data.clean()

