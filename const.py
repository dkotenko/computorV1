from enum import Enum

EPSILON = 0.000001
OPERATORS = r"\*\/\-\+\^"
DIGITS = "0123456789"
VALID_ARGS = ["--test", "--verbose"]

VERBOSE_MODE = False
TEST_MODE = False

class Mode:
    VERBOSE_MODE = False
    TEST_MODE = False


BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

class TOKENS(Enum):
    NUMBER=1
    IMAGINARY=2
    VARIABLE=3
    OPERATOR=4

class EQTYPE(Enum):
    QUAD_POSITIVE=1
    QUAD_ZERO=2
    QUAD_NEGATIVE=3
    INFINITY=4
    NO_SOLUTION=5

