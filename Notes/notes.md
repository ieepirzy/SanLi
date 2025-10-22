# Flow recap
SanLi code (text)
      ↓
Lexer → Tokens
      ↓
Parser → AST (tree of Node objects)
      ↓
AST traversal → LLVM IR (or bytecode, or interpreter execution)
      ↓
LLVM → Machine code → CPU executes


# AST example
    Assign
   /     \
 x       Add
        /   \
      5      3

