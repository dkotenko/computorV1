from UnexpectedSymbolError import UnexpectedSymbolError
import re


from ParsingData import ParsingData
from const import DIGITS, TOKENS

REGEX_X2 = r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)(\^2)"
REGEX_X0 = r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)(\^0)"
REGEX_X1 = r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)(\^1)?"
REGEX_C = r"([\+\-])?((\d+(\.\d+)?)(\*)?)?([\+\-])?(x)?(\^1)?"


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

    

    
        