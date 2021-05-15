class UnexpectedSymbolError(Exception):
    def __init__(self, symbol, position) -> None:
        self.symbol = symbol
        self.position = position