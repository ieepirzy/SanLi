class AstNode: #Base class, all nodes inherit from this.
    pass 

class ProgramNode(AstNode): #The "root" of the AST. 
    def __init__(self):
        self.statements = []

class varDeclNode(AstNode): #LLVM IR can allocate memory and store the initial value.
    def __init__(self,name,value, typ=None):
        self.name = name
        self.value = value
        self.type = typ

class binaryExprNode(AstNode): #Contains structure to represent a binary expression: 
    def __init__(self,left,op,right):
        self.left = left
        self.right = right
        self.op = op
        #note: left/right can themselves be expressions.

# Next, this file is going to contain the "leaf" nodes of the AST, aka the representation of specific as defined by the languages syntax, operations and supported types.

class NumNode(AstNode):
    def __init__(self, value):
        self.value = value
        self.type = "int"

class StrNode(AstNode):
    def __init__(self, value):
        self.value = value
        self.type = "str"

class BoolNode(AstNode):
    def __init__(self, value):
        self.value = value
        self.type = "bool"

class IdentifierNode(AstNode):
    def __init__(self, name):
        self.name = name
