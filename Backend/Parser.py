import Backend.AST as ast
"""
The parser is recursive: each method returns an AST node.

Nodes can contain other nodes (children).

When parsing an expression, the parser handles operator precedence by building a nested tree automatically.

Once the tree is built, LLVM IR generation just walks the tree, emitting instructions for each node.
"""

class Parser:

    LLVM_TYPE_MAP = {
        "int": "i32", 
        "Bool": "i1",
        "bool": "i1",
        "str": "i8*",   # pointer to chars
        "Obj": "i8*",   # generic object pointer, can refine later
        "null": "i8*"   # null pointer
    }

    #for expression parsing
    PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }


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
        
        #Get/consume tokens
        kw_token = self.getToken()  # 'var', 'let', or 'const'
        name_token = self.expect("IDENT")
        self.expect("SYM", "=")
        
        #Parse the expression assigned to the variable
        expr = self.parseExprs()
        self.expect("SYM", ":")
        
        # Consume the type identifier and map to LLVM type
        type_token = self.expect("IDENT")
        llvm_type = self.LLVM_TYPE_MAP.get(type_token[1])
        if llvm_type is None:
            raise SyntaxError(f"Unknown type: {type_token[1]}")
        
        #Consume the terminating semicolon
        self.expect("SYM", ";")
        
        #Return a VarDeclNode with LLVM-compatible info
        return ast.VarDeclNode(
            name=name_token[1],
            value=expr,
            typ=llvm_type,
            kind=kw_token[1]  # 'var' or 'const'
        )

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
    
    def expect(self, token_type, token_value=None):
        """
        Consume the next token and assert its type and optionally its value.
        Raises SyntaxError if the token doesn't match expectations.
        """
        token = self.getToken()  # consume the next token
        if token is None:
            raise SyntaxError(f"Unexpected end of input, expected {token_type} {token_value}")
        
        if token[0] != token_type:
            raise SyntaxError(f"Unexpected token {token}, expected type {token_type}")
        
        if token_value is not None and token[1] != token_value:
            raise SyntaxError(f"Unexpected token {token}, expected value '{token_value}'")
        
        return token

    def parseIf(self):
        raise NotImplemented

    def parseWhile(self):
        raise NotImplemented

    