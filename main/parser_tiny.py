import sys
from main.emitter import Emitter
from main.lexer import Lexer
from main.token_type import TokenType


class Parser:

    def __init__(self, lexer: Lexer, emitter: Emitter):
        self.lexer = lexer
        self.emitter = emitter
        self.token = None
        self.ident_set = set()

    def program(self):
        print("BEGIN PROGRAM")

        self.emitter.emit_header("#include <stdio.h>")
        self.emitter.emit_header("int main(void){")

        self.get_next_token()
        while self.token.token_type != TokenType.EOF:
            self.statement()
        self.emitter.emit_line("return 0;")
        self.emitter.emit_line("}")
        print("END PARSING")

    def statement(self):
        print("STATEMENT")
        if self.token.token_type == TokenType.PRINT:
            print("PRINT")

            self.get_next_token()

            if self.token.token_type == TokenType.STRING:
                self.emitter.emit_line('printf("' + self.token.token_text + '\\n");')
                self.get_next_token()
            else:
                self.expression()

        elif self.token.token_type == TokenType.LET:
            print("LET")

            self.get_next_token()

            # possible error here
            if self.token.token_text not in self.ident_set:
                self.ident_set.add(self.token.token_text)
                self.emitter.emit_header("float " + self.token.token_text + ";")

            self.emitter.emit(self.token.token_text)
            self.check_if_token_is(TokenType.IDENT)
            self.check_if_token_is(TokenType.EQ)
            self.emitter.emit(" =")

            self.expression()
            self.emitter.emit_line(";")

        elif self.token.token_type == TokenType.IF:
            print("IF")
            self.emitter.emit("if (")

            self.get_next_token()
            self.comparison()
            self.check_if_token_is(TokenType.THEN)

            self.emitter.emit_line("){")
            self.nl()

            while self.token.token_type != TokenType.ENDIF:
                self.statement()
            self.check_if_token_is(TokenType.ENDIF)
            self.emitter.emit_line("}")

        elif self.token.token_type == TokenType.WHILE:
            print("WHILE")

            self.emitter.emit("while(")

            self.get_next_token()
            self.comparison()
            self.emitter.emit_line("){")
            self.check_if_token_is(TokenType.REPEAT)
            self.nl()
            while self.token.token_type != TokenType.ENDWHILE:
                self.statement()
            self.check_if_token_is(TokenType.ENDWHILE)
            self.emitter.emit_line("}")

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
            self.emitter.emit(self.token.token_text)
            self.get_next_token()
            self.expression()

    def expression(self):
        print("EXPRESSION")
        self.term()

        while (
            self.token.token_type == TokenType.PLUS
            or self.token.token_type == TokenType.MINUS
        ):
            self.emitter.emit(self.token.token_text)
            self.get_next_token()
            self.term()

    def term(self):
        print("TERM")
        self.unrary()

        while (
            self.token.token_type == TokenType.DIVIDE
            or self.token.token_type == TokenType.MULTIPLY
        ):
            self.emitter.emit(self.token.token_text)
            self.get_next_token()
            self.unrary()

    def unrary(self):
        print("UNRARY")
        if (
            self.token.token_type == TokenType.PLUS
            or self.token.token_type == TokenType.MINUS
        ):
            self.emitter.emit(self.token.token_text)
            self.get_next_token()
        self.primary()

    def primary(self):
        print("PRIMARY")
        if (
            self.token.token_type == TokenType.NUMBER
            or self.token.token_type == TokenType.IDENT
        ):
            self.emitter.emit(self.token.token_text)
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
