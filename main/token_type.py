import enum


class TokenType(enum.Enum):
    EOF = -1,
    NEWLINE = 0,
    NUMBER = 1,
    STRING = 2
    IDENT = 3,
    #Keywords
    PRINT = 4,
    INPUT = 5,
    LET = 6,
    WHILE = 7,
    ENDWHILE = 8,
    REPEAT = 9,
    IF = 10,
    ENDIF = 11,
    THEN = 12,
    LABEL = 13,
    GOTO = 14,
    #Operators
    PLUS = 15,
    MINUS = 16,
    MULTIPLY = 17,
    DIVIDE = 18,
    LT = 19,
    LTEQ = 20,
    GT = 21,
    GTEQ = 22,
    EQ = 23,
    EQEQ = 24,
    NOTEQ = 25


class Token:
    def __init__(self, token_text: str, token_type: TokenType):
        self.token_text = token_text
        self.token_type = token_type
    
    def __str__(self):  # Defines string conversion
        return f"{self.token_type}, {self.token_text}"
    