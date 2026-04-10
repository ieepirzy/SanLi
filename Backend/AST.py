class AstNode: #Base class, all nodes inherit from this.
    pass 

class ProgramNode(AstNode): #The "root" of the AST. 
    def __init__(self):
        self.statements = []

class VarDeclNode(AstNode):
    def __init__(self, name, value, typ=None, kind="var"):
        self.name = name            # variable name
        self.value = value          # expression node
        self.type = typ             # LLVM type string
        self.kind = kind            # 'var' or 'const'
    

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

# Control flow nodes need structure like: KWRD (condition (like binaryExprNode)) {body}
class IfNode(AstNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body  # list of statements

class WhileNode(AstNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body