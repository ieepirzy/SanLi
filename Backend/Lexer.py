
class Lexer:

    keywords = {"var", "let", "const", "if", "else", "while", "obj", "null", "true", "false", "Bool", "bool"}  # etc.
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

            elif ch in '"\'':  # string literals
                string = ch
                quote_type = ch  # remember whether it's " or '

                while (next_ch := self.peekNextChar()) is not None:
                    next_ch = self.getNextChar()
                    string += next_ch
                    if next_ch == quote_type:
                        break
                else:
                    raise ValueError("Unterminated string literal")

                tokens.append(("STR", string))


            elif (ch.isalpha()): #start of a keyword or identifier.
                start = self.position -1
                value = ch

                while (next_ch := self.peekNextChar()) and next_ch.isalnum():
                    value += self.getNextChar()
                
                if value in self.keywords:
                    tokens.append(("KWRD", value))
                else:
                    tokens.append(("IDENT", value))

            elif (ch.isdigit()): #number
                value = ch
                while (next_ch := self.peekNextChar()) and next_ch.isdigit(): #iterate until last digit
                    value += self.getNextChar()
                    
                tokens.append(("NUM", value))

            elif ch in "*<>+-/=;:!?)(":  # Operator
                operator = ch
                allowed_compounds = {"++", "--", "==", "!=", "+=", "-=", "*=", "/=", "<=", ">="}

                # Try to form a compound operator
                if (next_ch := self.peekNextChar()) and (operator + next_ch) in allowed_compounds:
                    operator += self.getNextChar()

                # After this, operator is either single-char or valid compound
                tokens.append(("SYM", operator))


            else:
                raise ValueError(f"Unexpected character: {ch}")
            
        return tokens

    def peekNextChar(self):
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
