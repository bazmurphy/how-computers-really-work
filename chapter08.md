# Chapter 08 - Machine Code and Assembly Language

## 08.01 - Software Terms Defined

- Software is a set of instructions that tell a computer what to do, distinct from hardware.
- Programs are ordered sets of software instructions that accomplish tasks.
- Programming is the act of writing programs.
- Applications are programs that interact directly with humans and may consist of multiple programs.
- The term "app" became popular around 2008, with additional connotations covered in Chapter 13.
- Computer code or code refers to sets of software instructions.
- CPUs execute machine code, while developers write source code in high-level programming languages.
- Source code is the original text of a program written by developers.
- Machine code is software in binary machine language instructions.
- CPU architecture determines which instructions a CPU understands.
- Machine language instructions are like vocabulary words forming sentences to convey meaning.
- All programs, regardless of their origin or programming language, eventually execute as a series of 0s and 1s on a CPU.
- Diagnosing software failures often involves analyzing code written by other companies.
- Despite complexities, failing software ultimately consists of 1s and 0s that a CPU interprets as instructions.

## 08.02 - An Example Machine Instruction

- Example machine instruction for ARM processors: move the number 4 into register r7
- Binary representation: `11100011101000000111000000000100`
- Decoding the instruction:
  - Condition: `1110` (always execute)
  - Immediate: `1` (value is in the last 8 bits of instruction)
  - Opcode: `1101` (move value)
  - Destination register: `0111` `(r7)`
  - Immediate value: `0000 0100` `(4 decimal)`
- The instruction is represented in hexadecimal as `e3a07004`
- Assembly language representation: `mov r7, #4`
- Assembly language provides human-readable mnemonics for opcodes
- CPU only deals with binary, but assembly language makes it easier for programmers
- Assembly language statements need to be translated into machine code using an assembler

```
11100011101000000111000000000100
```

```
e3a07004
```

```assembly
mov r7, #4
```

![](/images/08-01-01.png)

![](/images/08-01-02.png)

## 08.03 - Calculating a Factorial in Machine Code

- ARM machine code is capable of performing useful tasks by combining multiple instructions.
- The example focuses on calculating the factorial of an integer using ARM machine code.
- Factorial (n!) is the product of positive integers less than or equal to n.
- The code assumes the initial value of 'n' is stored in register r0, with the result also stored in r0.
- Machine code must be loaded into memory before the CPU can access it.
- The provided hexadecimal values represent ARM instructions at specific memory addresses.
- Instructions are decoded into assembly language mnemonics for better understanding.
- The CPU executes instructions sequentially until it encounters a branching instruction, which may redirect program flow.
- The end of the factorial logic is marked by a specific memory address.
- Registers and their values play a crucial role in executing instructions and storing results.
- Understanding ARM instructions and their effects on registers is essential for interpreting the program's behavior.
- Branch instructions in ARM processors rely on status flags in a dedicated register to determine program flow.
- The status register contains flags indicating conditions such as negative results or zero outcomes from instructions.

```
4! = 4 × 3 × 2 × 1 = 24
```

```
Address Data
0001007c e2503001
00010080 da000002
00010084 e0000093
00010088 e2533001
0001008c 1afffffc
```

```
Address Data Assembly
0001007c e2503001 subs r3, r0, #1
00010080 da000002 ble 0x10090
00010084 e0000093 mul r0, r3, r0
00010088 e2533001 subs r3, r3, #1
0001008c 1afffffc bne 0x10084
00010090 ---
```

![](/images/08-02-01.png)

## 08.04 - Summary

- Machine code: CPU-specific instructions stored as bytes in memory
- Example ARM processor instruction encoding discussed
- Assembly language: human-readable form of machine code
- Assembly language as source code, allowing for combination of statements for useful operations
- Next chapter: High-level programming languages
- High-level languages provide abstraction from CPU instruction set
- Easier to understand and portable across different hardware platforms

## 08.05 - Project 12: Factorial in Assembly

## 08.06 - Project 13: Examining Machine Code
