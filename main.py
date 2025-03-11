from lexer import Lexer


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
    source_code = """PRINT jjj  """
    
    lexer_comp  = Lexer(source=source_code)


    token = lexer_comp.get_token()
    while True:
        if token == "\0":
            break
        print(token)
        token = lexer_comp.get_token()

main()