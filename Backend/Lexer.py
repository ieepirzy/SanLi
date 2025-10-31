
class Lexer:
    # Initialize the lexer with the source code
    def __init__(self, source):
        self.source = source
        self.position = 0

    # This method gets the next character from the source code
    def getNextChar(self):
        if self.position >= len(self.source):
            return None  # End of source
        current_char = self.source[self.position]
        self.position += 1
        return current_char  # Placeholder: return single characters as tokens

    # This method creates tokens from the output characters of the previous method
    def getNextToken(self):
        tokens = []
        while (ch := self.getNextChar()) is not None:
            if (ch.isspace()): #if whitespace, then skipped.
                continue
            elif (ch.isalpha()): #start of a keyword or identifier.
                start = self.position -1
                value = ch
                while (next_ch := self.peekNextChar()) and next_ch.isalnum():
                    value += self.getNextChar()
                tokens.append(("IDENT", value))
            elif (ch.isdigit()): #number
                value = ch
                while (next_ch := self.peekNextChar()) and next_ch.isdigit(): #iterate until last digit
                    value += self.getNextChar()
                tokens.append(("NUM", value))

            elif ch in "*+-/=;:": #Operator
                tokens.append(("SYM", ch))
            else:
                raise ValueError(f"Unexpected character: {ch}")
        return tokens

    def peekNextChar(self):
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
