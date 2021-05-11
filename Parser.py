import re
from Validator import Validator
from ParsingData import ParsingData
from const import DIGITS, TOKENS


class Parser():

    def Parser(self, data):
        self.data = ParsingData()

    def parse(self, line):
        validator = Validator()    
        if not validator.is_valid(line):
            return
        self.__parse_by_char(line)    

    def __is_digit(self, c):
        return c in DIGITS
    
     # "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

    def __parse_number(self, line, i):
        with self.data:
            i_start = i
            token_type = TOKENS.NUMBER
            
            while i < len(line):
                c = line[i]
                if not self.__is_digit(c) and c != '.':
                    break
                i += 1

            if i < len(line) and line[i] == 'i':
                i += 1
                token_type = TOKENS.IMAGINARY
            value = line[i_start : i]

        return Token(value, token_type), i

    @classmethod
    def __parse_by_char(self, line):
        data.i = 0
        data.line = line
        while data.i < len(line):
            if is_digit(data.line[data.i]):
                __parse_number(self)
            elif is_operator(data.line[data.i]):
                __parse_operator(self)
            data.i += 1
        
        #if not re.findall():
        