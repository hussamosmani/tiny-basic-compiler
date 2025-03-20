# Tiny Compiler

## Introduction
This is my take on the tiny compiler by Austin Henley: https://austinhenley.com/index.html. I have attempted to make a compiler for the ting programming language. This compiler was made as an exercise into seeing how basic code compilation is done.

## Compiler Structure  

The compiler is divided into three main components:  

1. **Lexer (Tokenizer)** – This phase scans the source code and breaks it down into tokens, which are the smallest units of meaning (e.g., keywords, identifiers, numbers, operators).  

2. **Parser** – The parser takes the tokens produced by the lexer and organizes them into a structured representation, usually in the form of an Abstract Syntax Tree (AST). This helps in understanding the relationships between different parts of the code.  

3. **Emitter (Code Generator)** – The emitter takes the parsed structure and translates it into the target language, such as assembly or another high-level language. This step turns the structured representation into actual executable instructions.  

Each of these sections plays a crucial role in transforming raw code into something that can be executed.

## The Tiny Language  

This compiler supports a subset of the Tiny language with the following grammar:  

```ebnf
program     ::= { statement }

statement   ::= "PRINT" ( expression | string ) nl
             | "IF" comparison "THEN" nl { statement } "ENDIF" nl
             | "WHILE" comparison "REPEAT" nl { statement } "ENDWHILE" nl
             | "LET" ident "=" expression nl
