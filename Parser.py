from UnexpectedSymbolError import UnexpectedSymbolError
import re
from Printer import Printer
from Math import Math
from ParsingData import ParsingData

REGEX_X2 = r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)(\^2)"
REGEX_X0 = r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)(\^0)"
REGEX_X1 = r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)(\^1)?"
REGEX_C =  r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)?(\^1)?"


class Parser():

    def __init__(self):
        self.data = ParsingData()

    def parse(self, line):
        
        splitted = line.split('=')
        l = [[splitted[0], 1], [splitted[1], -1]]
        for part, sign in l:
            self.data.line = part
            self.__parse(REGEX_X2, sign)
            self.__parse(REGEX_X0, sign)
            self.__parse(REGEX_X1, sign)
            self.__parse(REGEX_C, sign)
            if self.data.line:
                raise UnexpectedSymbolError(self.data.line[0], self.data.position[0])
        return self.data

    def __delete_added(self, match):
        sign_str, _, number_str, _, \
            asterix_str, x_sign_str, var_str, var_exp = match

        to_replace = sign_str + number_str + asterix_str \
             + x_sign_str + var_str + var_exp
        line = self.data.line
        position = self.data.position
        f = line.find(to_replace)
        self.data.line = line[:f] + line[f + len(to_replace):]
        self.data.position = position[:f] + position[f + len(to_replace):]
        return

    def __add_value(self, value, regex_str):
        if regex_str == REGEX_X2:
            self.data.x2 += value
        elif regex_str == REGEX_X1:
            self.data.x1 += value
        elif (
            regex_str == REGEX_X0 or
            regex_str == REGEX_C
            ):
            self.data.c += value

    def __parse(self, regex_str, sign_base):

        matches = re.findall(regex_str, self.data.line)
        for match in matches:
            sign_str = match[0]
            number_str = match[2]
            sign = 1 if sign_str != '-' else -1
            if number_str:
                value = float(number_str)
            elif match[6]:
                value = 1
            else:
                value = 0
            self.__add_value(value * sign * sign_base, regex_str)
            self.__delete_added(match)
        return

    def get_reduced_form(line: str):

        def get_values(part, sign, d):

            def add_to_dict(d, value, degree, sign):
                if degree in d:
                    d[degree] += (value * sign)
                else:
                    d[degree] = (value * sign)

            def add_number(d, token, sign):
                value = Math.eval_float(token)
                degree = 0
                add_to_dict(d, value, degree, sign)

            def add_var(d, token, sign):
                if token.find('*') > -1:
                    value = Math.eval_float(token.split('*')[0])
                else:
                    value = 1
                if token.find('^') > -1:
                    degree = Math.eval_int(token.split('^')[1])
                else:
                    degree = 1
                add_to_dict(d, value, degree, sign)

            

            splitted_by_plus = part.split("+")
            for token_plus in splitted_by_plus:
                if not token_plus:
                    continue
                token_first_sign = 1 if token_plus[0] != '-' else -1
                splitted_by_minus = token_plus.split("-")
                i = 0
                for token_minus in splitted_by_minus:
                    if not token_minus:
                        continue
                    token_sign = -1
                    if not i and token_first_sign == 1:
                        token_sign = 1
                    i += 1
                    if token_minus.find('x') > -1:
                        add_var(d, token_minus, sign * token_sign)    
                    else:
                        add_number(d, token_minus, sign * token_sign)
                

        by_equity_sign = line.split('=')
        left, right = by_equity_sign
        d = {}
        get_values(left, 1, d)
        get_values(right, -1, d)
        i = 0
        str_reduced = ''
        for key in sorted(list(d.keys())):
            if d[key] == 0:
                continue
            if i or d[key] < 0:
                sign_symbol = '+' if d[key] >= 0 else '-'
                space = ' ' if i else ''
                str_reduced += f'{space}{sign_symbol}{space}'
            value_str = Printer.get_float_string(Math.abs(d[key]))
            str_reduced += f'{value_str} * X^{key}'
            i += 1
        if not str_reduced:
            str_reduced = '0'
        str_reduced += ' = 0'
        return str_reduced

    

    
        