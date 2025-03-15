from lexer import Lexer
from token_type import TokenType


def main():

    # source_code = """
    #     PRINT "How many fibonacci numbers do you want?"
    #     INPUT nums

    #     LET a = 0
    #     LET b = 1
    #     WHILE nums > 0 REPEAT
    #         PRINT a
    #         LET c = a + b
    #         LET a = b
    #         LET b = c
    #         LET nums = nums - 1
    #     ENDWHILE
    #     """
    source_code = "IF + - 123 foo * THEN /"
    
    lexer_comp  = Lexer(source=source_code)


    token = lexer_comp.get_token()
    while True:
        print(token)
        if token.token_type == TokenType.EOF :
            break
        token = lexer_comp.get_token()

main()