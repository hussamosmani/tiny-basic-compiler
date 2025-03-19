from lexer import Lexer
from parser_tiny import Parser
from token_type import TokenType


def main():

    source_code = """PRINT "How many fibonacci numbers do you want?"
        INPUT nums

        LET a = 0
        LET b = 1
        WHILE nums > 0 REPEAT
            PRINT a
            LET c = a + b
            LET a = b
            LET b = c
            LET nums = nums - 1
        ENDWHILE
        """
    lexer_comp = Lexer(source=source_code)

    parser = Parser(lexer=lexer_comp)
    parser.program()


main()
