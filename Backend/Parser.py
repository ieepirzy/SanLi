import Backend.AST as ast
"""
The parser is recursive: each method returns an AST node.

Nodes can contain other nodes (children).

When parsing an expression, the parser handles operator precedence by building a nested tree automatically.

Once the tree is built, LLVM IR generation just walks the tree, emitting instructions for each node.
"""

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    

    def parseProgram(self):
        program = ast.ProgramNode()
        while self.peekToken() is not None:
            stmt = self.parseStatement()
            if stmt:
                program.statements.append(stmt)
        return program
    
    def parseStatement(self):
        token = self.peekToken()
        if token[0] == "KWRD" and token[1] in ("var","const","let"):
            if token[1] == "let":
                raise NotImplementedError
            return self.parseVarDec()
        
        elif token[0] == "KWRD" and token[1] == "if":
            return self.parseIf()
        
        elif token[0] == "KWRD" and token[1] == "while":
            return self.parseWhile()
        else:
            raise SyntaxError(f"Unexpected token in statement: {token}")
        
    
    def parseFactor(self):
        token = self.getToken()
        if token[0] == "NUM":
            return ast.NumNode(int(token[1]))
        elif token[0] == "STR":
            return ast.StrNode(token[1])
        elif token[0] == "KWRD" and token[1] in ("true", "false"):
            return ast.BoolNode(token[1] == "true") #hacky way to evaluate true/false
        elif token[0] == "IDENT":
            return ast.IdentifierNode(token[1])
        elif token[0] == "SYM" and token[1] == "(":
            expr = self.parseExprs()
            self.expect("SYM", ")")
            return expr
        else:
            raise SyntaxError(f"Unexpected token in expression: {token}")        

    def parseVarDec(self):
        #to parse a variable declaration, we need to generate a base node with the children of the declaration. 

        kw = self.getToken() #this stores the keyword and also advances the tokens list, i.e consumes the token
        name_token = self.expect("IDENT")
    

    #for expression parsing
    PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    def parseExprs(self, min_prededence=0):
        left = self.parseFactor()

    
    def getToken(self):
        token = self.peekToken()
        if token:
            self.pos += 1
        return token
        
    def peekToken(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    
    def parseIf(self):
        raise NotImplemented

    def parseWhile(self):
        raise NotImplemented

    