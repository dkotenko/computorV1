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
                "negative power at position %d" % negative_power)
        
        invalid_power = re.findall(r"\^\D", line)
        if invalid_power:
            return Printer.print_error(
                f'invalid power: {invalid_power[0]}'
            )

        invalid_number_to_power = re.findall(r"[^x]\^", line)
        if invalid_number_to_power:
            return Printer.print_error(
                f'invalid number to power, only x allowed to power: {invalid_number_to_power[0]}'
            )

        invalid_mult_after = re.findall(r"\*[^x]", line)
        if invalid_mult_after:
            return Printer.print_error(
                f'only x allowed to be multiplicator: {invalid_mult_after[0]}'
            )

        invalid_mult_x_before = re.findall(r"x\*", line)
        if invalid_mult_x_before:
            return Printer.print_error(
                f'x not allowed to be multiplicant: {invalid_mult_x_before[0]}'
            )

        invalid_binary_op = re.findall(r"^[\^\*]", line) + re.findall(r"[\^\*]$", line)
        if invalid_binary_op:
            return Printer.print_error(
                f'invalid number of operands near the binary operator: {invalid_binary_op[0]}'
            )

        float_power = re.findall(r"\^\d+\.", line)
        if float_power:
            return Printer.print_error(
                f'float power not allowed: {float_power[0]}'
            )

        temp_re = re.findall(r"[*/\-+^]{2}", line)
        if temp_re:
            return Printer.print_error(
                "invalid operator order: %s" % temp_re[0])

        temp_re = re.findall(r"[*/\-+^]\=", line)
        if temp_re:
            return Printer.print_error(
                "invalid operator order: %s" % temp_re[0])
        return True
    
    def is_valid_variable(self, line):
        if re.findall(r"\dx", line):
            return Printer.print_error(
                "x variable and digits must be separated by * sign")
        invalid_symbol = re.findall(r"[^\dx\.\*\+\-\^\=]", line)
        if invalid_symbol:
            return Printer.print_error(
                f"invalid symbol: {invalid_symbol[0]}")
        return True

    def is_valid_float(self, line):
        invalid_float = re.findall(r"\d+\.\d+[^\+\-\*\=$]", line)
        if invalid_float:
            return Printer.print_error(
                f"invalid float: {invalid_float[0]}")
        return True
    
    def is_valid(self, line):
        self.curr_line = line
        if (
            not self.is_valid_equity_sign(line) or
            not self.is_valid_dots(line) or
            not self.is_valid_operators(line) or
            not self.is_valid_variable(line) or
            not self.is_valid_float(line)
        ):
            return False
        return True

