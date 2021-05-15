import re
from const import OPERATORS
from Printer import Printer

class Validator:

    def __init__(self):
        return

    def is_valid_equity_sign(self, line):
        error = "invalid expression: "
        if line.find("=") == -1:
            return Printer.print_error(error + " no equal sign")
        if len(re.findall("=", line)) > 1:
            return Printer.print_error("more than 1 equity sign")
        if line[0] == "=": 
            return Printer.print_error(error + " no left part")
        if line[-1] == "=": 
            return Printer.print_error(error + " no right part")
        return True

        
    def is_valid_dots(self, line):
        if line.find('.') == -1:
            return True
        double_dots = line.find("..")
        if double_dots != -1:
            return Printer.print_error(
                "invalid input: double dot at position %d" % double_dots)
        temp_re = re.findall(r"\.\D", line)
        if temp_re:
            return Printer.print_error(
                "invalid decimal: no digit after dot in %s" % temp_re[0])
        temp_re = re.findall(r"\D\.", line)
        if temp_re:
            return Printer.print_error(
                "invalid decimal: no digit before dot in %s" % temp_re[0])
        return True


    def is_operator(char):
        return True if char in "*/+-" else False


    def is_valid_operators(self, line):
        negative_power = line.find("^-")
        if negative_power > -1:
            return Printer.print_error(
                "Negative power at position %d" % negative_power)
        temp_re = re.findall(r"[*/\-+^]{2}", line)
        if temp_re:
            return Printer.print_error(
                "invalid operator order: %s" % temp_re[0])
        temp_re = re.findall(r"[*/\-+^]\=", line)
        if temp_re:
            return Printer.print_error(
                "invalid operator order: %s" % temp_re[0])
        return True
    
    
    def is_valid(self, line):
        self.curr_line = line
        if (
            not self.is_valid_equity_sign(line) or
            not self.is_valid_dots(line) or
            not self.is_valid_operators(line)
        ):
            return False
        return True

