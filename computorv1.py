from Printer import Printer
from UnexpectedSymbolError import UnexpectedSymbolError
import fileinput
from Parser import Parser
from Solver import Solver
import sys
import re


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
        try:
            f = open(filename)
            f.close()
        except FileNotFoundError:
            Printer.print_error(f"file {filename} not accessible")
            f.close()
            exit()

def print_polynomial_degree(line):
    degree = 0
    matches = re.findall(r"[xX]\^\d+", line)
    for match in matches:
        value = int(match.lstrip('Xx^'))
        print(match, line)
        if value > degree:
            degree = value
    if not matches:
        matches = re.findall(r"[xX]", line)
        if matches:
            degree = 1
    print(f'Polynomial degree: {degree}')

if __name__ == "__main__":
    check_input_source()
    for line in fileinput.input():
        line = do_replace(line)
        if not len(line):
            continue
        if line == 'exit':
            exit()
        parser = Parser()
        print_polynomial_degree(line)
        try:
            data = parser.parse(line)
            solver = Solver(data)
            solver.solve()
        except UnexpectedSymbolError as e:
            text = 'unexpected symbol(s) at position'
            Printer.print_error(f'{text} {e.position}: {e.symbol}')
        parser.data.clean()

