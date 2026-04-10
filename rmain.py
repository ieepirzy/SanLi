from Backend.Lexer import Lexer
from Backend.Parser import Parser
import Backend.AST as ast
with open("source.san","r") as f:
    code = f.read()

def print_ast(node, indent=0):
    prefix = "  " * indent
    if isinstance(node, ast.ProgramNode):
        print(f"{prefix}Program:")
        for stmt in node.statements:
            print_ast(stmt, indent+1)
    elif isinstance(node, ast.VarDeclNode):
        print(f"{prefix}VarDecl: {node.kind} {node.name} : {node.type}")
        print_ast(node.value, indent+1)
    elif isinstance(node, ast.binaryExprNode):
        print(f"{prefix}BinaryExpr: {node.op}")
        print_ast(node.left, indent+1)
        print_ast(node.right, indent+1)
    elif isinstance(node, ast.NumNode):
        print(f"{prefix}Num: {node.value}")
    elif isinstance(node, ast.StrNode):
        print(f"{prefix}Str: {node.value}")
    elif isinstance(node, ast.BoolNode):
        print(f"{prefix}Bool: {node.value}")
    elif isinstance(node, ast.IdentifierNode):
        print(f"{prefix}Ident: {node.name}")

    elif isinstance(node, ast.IfNode):
        print(f"{prefix}If:")
        print(f"{prefix}  condition:")
        print_ast(node.condition, indent+2)
        print(f"{prefix}  body:")
        for stmt in node.body:
            print_ast(stmt, indent+2)

    elif isinstance(node, ast.WhileNode):
        print(f"{prefix}While:")
        print(f"{prefix}  condition:")
        print_ast(node.condition, indent+2)
        print(f"{prefix}  body:")
        for stmt in node.body:
            print_ast(stmt, indent+2)

lexer = Lexer(code)
tokens = lexer.getNextToken()

for token in tokens:
    print(token)

parser = Parser(tokens)
program = parser.parseProgram()

print_ast(program)

