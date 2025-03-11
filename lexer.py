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
    
    def get_token(self):

        pntr = self.curr_char_index
        while self.source[pntr] == EMPTY_STRING:
            pntr+=1
        
        token = ""
        while self.source[pntr] != EMPTY_STRING:
            if pntr == len(self.source) - 1:
                return "\0"
            if self.source[pntr] == NEWLINE:
                break
            token+=self.source[pntr]
            pntr+=1
        
        self.curr_char_index = pntr
        
        return token