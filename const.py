from enum import Enum

EPSILON = 0.000001
OPERATORS = r"\*\/\-\+\^"
DIGITS = "0123456789"

class TOKENS(Enum):
    NUMBER=1
    IMAGINARY=2
    VARIABLE=3
    OPERATOR=4