from lexer import Lexer


def basic_lexer_split():
    source_code = """
    INPUTS nums
    """
    
    testing_list = []
    lexer_comp  = Lexer(source=source_code)


    token = lexer_comp.get_token()
    while True:
        testing_list.append(token)
        if token == "EOF":
            break
        token = lexer_comp.get_token()
    
    assert testing_list == ["EOL","INPUTS","nums","EOL","EOF"]
