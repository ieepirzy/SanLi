from Backend.Lexer import Lexer

with open("source.san","r") as f:
    code = f.read()

lexer = Lexer(code)
tokens = lexer.getNextToken()

for token in tokens:
    print(token)
