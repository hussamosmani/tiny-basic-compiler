import sys
from lexer import Lexer
from token_type import TokenType


class Parser:

    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.token = None

    def program(self):
        print("BEGIN PROGRAM")

        self.get_next_token()
        while self.token.token_type != TokenType.EOF:
            self.statement()

        print("END PARSING")

    def statement(self):
        print("STATEMENT")
        if self.token.token_type == TokenType.PRINT:
            print("PRINT")

            self.get_next_token()

            if self.token.token_type == TokenType.STRING:
                self.get_next_token()
            else:
                self.expression()

        elif self.token.token_type == TokenType.LET:
            print("LET")

            self.get_next_token()

            self.check_if_token_is(TokenType.IDENT)
            self.check_if_token_is(TokenType.EQ)

            self.expression()

        elif self.token.token_type == TokenType.IF:
            print("IF")

            self.get_next_token()
            self.check_if_token_is(TokenType.THEN)

            while self.token.token_type != TokenType.ENDIF:
                self.statement()
            self.check_if_token_is(TokenType.ENDIF)

        elif self.token.token_type == TokenType.INPUT:
            print("INPUT")

            self.get_next_token()
            self.check_if_token_is(TokenType.IDENT)

        elif self.token.token_type == TokenType.WHILE:
            print("WHILE")

            self.get_next_token()
            self.comparison()
            self.check_if_token_is(TokenType.REPEAT)
            self.nl()
            while self.token.token_type != TokenType.ENDWHILE:
                self.statement()
            self.check_if_token_is(TokenType.ENDWHILE)

        elif self.token.token_type == TokenType.LABEL:
            print("LABEL")
            self.get_next_token()

        elif self.token.token_type == TokenType.GOTO:
            print("GOTO")
            self.get_next_token()

        else:
            self.abort(f"Unrecognised token: {self.token}")

        self.nl()

    def comparison(self):
        self.expression()

        while (
            self.token.token_type == TokenType.GT
            or self.token.token_type == TokenType.GTEQ
            or self.token.token_type == TokenType.LT
            or self.token.token_type == TokenType.LTEQ
            or self.token.token_type == TokenType.EQEQ
        ):
            self.get_next_token()
            self.expression()

    def expression(self):
        print("EXPRESSION")
        self.term()

        while (
            self.token.token_type == TokenType.PLUS
            or self.token.token_type == TokenType.MINUS
        ):
            self.get_next_token()
            self.term()

    def term(self):
        print("TERM")
        self.unrary()

        while (
            self.token.token_type == TokenType.DIVIDE
            or self.token.token_type == TokenType.MULTIPLY
        ):
            self.get_next_token()
            self.unrary()

    def unrary(self):
        print("UNRARY")
        if (
            self.token.token_type == TokenType.PLUS
            or self.token.token_type == TokenType.MINUS
        ):
            self.get_next_token()
        self.primary()

    def primary(self):
        print("PRIMARY")
        if (
            self.token.token_type == TokenType.NUMBER
            or self.token.token_type == TokenType.IDENT
        ):
            self.get_next_token()
        else:
            self.abort(f"Invalid token at: {self.token}")

    def check_if_token_is(self, token_type: TokenType):
        if self.token.token_type != token_type:
            self.abort(f"Expected {token_type} got: {self.token.token_type}")
        self.get_next_token()
        return True

    def get_next_token(self):
        self.token = self.lexer.get_token()

    def abort(self, exit_message: str):
        sys.exit(exit_message)

    def nl(self):
        while self.token.token_type == TokenType.NEWLINE:
            self.get_next_token()
