import sys
from token_type import Token, TokenType
# Numerical variables
# LET a = 0
# Basic arithmetic
# LET c = a + b
# +, -, /, *, >, <
# If statements
# While loops
# WHILE nums > 0 REPEAT
# Print text and numbers
# PRINT "How many fibonacci numbers do you want?"
# Input numbers
# INPUT nums
# Labels and goto
# Comments

EMPTY_STRING = " "
NEWLINE = "\n"

class Lexer:

    def __init__(self,source):
        self.source = source + '\n'
        self.curr_char_index = 0
        pass

    def clear_whitespace(self):
        pntr = self.curr_char_index
        while self.source[pntr] == EMPTY_STRING:
            pntr+=1
        self.curr_char_index = pntr


    def get_token(self):
        
        self.clear_whitespace()

        
        token = ""

        if self.curr_char_index == len(self.source) - 1:
            token = "EOF"
            return Token(token_text=token, token_type=TokenType.EOF)

        if self.source[self.curr_char_index] == NEWLINE:
            self.curr_char_index+=1
            token = "EOL"
        
        pntr = self.curr_char_index

        if self.source[pntr] == '"':
            start_indx = pntr
            while self.source[pntr] != '"':
                if self.source[pntr] == '\r' or self.source[pntr] == '\n' or self.source[pntr] == '\t' or self.source[pntr] == '\\' or self.source[pntr] == '%':
                    self.abort("Illegal character in string.")
                pntr+=1
            pntr+=1
            token = '"' + self.source[start_indx:pntr] + '"'
        
        else:
            while self.source[pntr] != EMPTY_STRING and self.source[pntr] != NEWLINE:
                token+=self.source[pntr]
                pntr+=1
            self.curr_char_index = pntr
        

        if token == "+":
            return Token(token_text=token, token_type=TokenType.PLUS)
        elif token == "-":
            return Token(token_text=token, token_type=TokenType.MINUS)
        elif token == "*":
            return Token(token_text=token, token_type=TokenType.MULTIPLY)
        elif token == "/":
            return Token(token_text=token, token_type=TokenType.DIVIDE)
        elif token == "<":
            return Token(token_text=token, token_type=TokenType.LT)
        elif token == "<=":
            return Token(token_text=token, token_type=TokenType.LTEQ)
        elif token == ">":
            return Token(token_text=token, token_type=TokenType.GT)
        elif token == ">=":
            return Token(token_text=token, token_type=TokenType.GTEQ) 
        elif token == "=":
            return Token(token_text=token, token_type=TokenType.EQ)
        elif token == "==":
            return Token(token_text=token, token_type=TokenType.EQEQ)
        elif token == "!=":
            return Token(token_text=token, token_type=TokenType.NOTEQ)
        elif token == "PRINT":
            return Token(token_text=token, token_type=TokenType.PRINT)
        elif token == "INPUT":
            return Token(token_text=token, token_type=TokenType.INPUT)
        elif token == "LET":
            return Token(token_text=token, token_type=TokenType.LET)
        elif token == "WHILE":
            return Token(token_text=token, token_type=TokenType.WHILE)
        elif token == "ENDWHILE":
            return Token(token_text=token, token_type=TokenType.ENDWHILE)
        elif token == "REPEAT":
            return Token(token_text=token, token_type=TokenType.REPEAT)
        elif token == "IF":
            return Token(token_text=token, token_type=TokenType.IF)
        elif token == "ENDIF":
            return Token(token_text=token, token_type=TokenType.ENDIF)
        elif token == "THEN":
            return Token(token_text=token, token_type=TokenType.THEN)
        elif token == "LABEL":
            return Token(token_text=token, token_type=TokenType.LABEL)
        elif token == "GOTO":
            return Token(token_text=token, token_type=TokenType.GOTO)
        elif token == "EOF":
            return Token(token_text=token, token_type=TokenType.EOF)
        elif token == "EOL":
            return Token(token_text=token, token_type=TokenType.NEWLINE)
        elif token[0] == '"':
             return Token(token_text=token, token_type=TokenType.STRING)
        elif token.isdigit():
             return Token(token_text=token, token_type=TokenType.NUMBER)
        elif Lexer._is_identifier(token=token):
            return Token(token_text=token, token_type=TokenType.IDENT)
        else:
            self.abort("token not found: ", token)

        return token
    def abort(self, message):
        sys.exit("Lexing error. " + message)
        
    @staticmethod
    def _is_identifier(token: str):
        if not token[0].isalpha():  # First character must be a letter
            return None
        for char in token[1:]:  # Remaining characters must be alphanumeric
            if not char.isalnum():
                return None
        return token  # If all checks pass, it's a valid identifier
