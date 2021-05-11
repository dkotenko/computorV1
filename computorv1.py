import fileinput
from Parser import Parser
import sys


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
    return line


if __name__ == "__main__":

    for line in fileinput.input():
        line = do_replace(line)

        if not len(line):
            continue
        if line == 'exit':
            exit()
        parser = Parser()
        parser.parse(line)

