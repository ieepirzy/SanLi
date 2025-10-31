# SanLi
A self-made toy programming language

# Overview
SanLi is a self-made toy programming language, meant to be a hobby+learning project for me to understand programming languages better through hands-on work.
The goal is to create a basic and functional language.

## Features
SanLi is to be a strongly typed case sensitive langauge, and implement basic datatypes such as integers, floats, booleans, chars, strings, and basic conditionals (if-else) and loops (for, while)

## Implementation
The workflow for running SanLi will look like the following:

SanLi -> AST -> LLVM IR -> LLVM compiler generates machine code -> CPU runs the code.

As such, this project mainly consists of creating the LLVM IR compatible AST.

The intermediary language chosen for the AST is Python due to the existing llvmlite package and the ease of prototyping which Python brings.

