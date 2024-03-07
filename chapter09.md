# Chapter 09 - High-Level Programming

## 09.01 - High-Level Programming Overview

- Assembly language and machine code writing is time-consuming and prone to errors, difficult to maintain, and tied to specific CPU architectures.
- High-level programming languages were developed to address these issues, allowing programming in a language independent from CPU architecture and closer to human language.
- High-level languages require compilers to convert program statements into machine code for specific processors.
- Using high-level languages, developers can write programs once and compile them for multiple types of processors with minimal changes to the source code.
- Compilers output object files containing machine code for a specific processor.
- Object files need to be linked to create an executable file that the operating system can run; this is done by a linker, which can also bring in other necessary libraries of compiled code.
- The process of compiling and linking is essential for building software.
- In common usage, "compiling" often refers to the entire process of compiling, linking, and any other steps needed to finalize the code.
- Compilers typically automate the linking step, making it less apparent to developers.

![](/images/09-01-01.png)

## 09.02 - Introduction to C and Python

- Learning high-level programming involves examining programming languages and writing programs in them.
- This chapter focuses on two high-level languages: C and Python, which offer similar functionalities in different ways.
- C originated in the 1970s and is closely tied to machine code, making it suitable for hardware interfacing and operating system development.
- C++ is an updated version of C and is also powerful but complex, lacking safeguards against errors.
- Python, released in the 1990s, is known for readability and simplicity, making it suitable for beginners and complex projects.
- Python follows a "batteries included" philosophy, providing a comprehensive standard library for developers.
- High-level programming languages abstract CPU instructions for memory access, mathematical operations, and program flow control.
- The chapter aims to familiarize readers with common programming language concepts rather than teaching a specific language.

## 09.03 - Comments

- Comments in programming languages don't execute any commands but provide insights into the code.
- Nearly all programming languages offer a way to include comments.
- Comments are meant for other developers and are ignored by the compiler.
- In C, comments are specified with `/* */` for multiline and `//` for single-line comments.
- Python uses the hash character `#` for comments.
- Python doesn't have specific multiline comment support; multiple single-line comments can be used instead.

```c
/*
This is a C- style comment.
It can span multiple lines.
*/
// This is a single- line C comment, originally introduced in C++.
```

```python
# This is a comment in Python.
```

## 09.04 - Variables

- Memory access is a crucial feature in processors and high-level languages.
- Variables serve as named storage locations in memory.
- They enable programmers to assign names to memory addresses for data access.
- Most programming languages associate variables with a specific data type (e.g., integer, string).
- Variables hold a value, which represents the data stored in memory.
- Every variable has an address, denoting the memory location of its value.
- Variables have scope, defining the parts of the program where they can be accessed ("in scope").

### 09.04.01 - Variables in C

- Variables in C are declared using a specific type, such as int for integers.
- Example: `int points = 27;` declares a variable named points with a value of 27.
- The size of the variable in memory depends on its type, with int typically being 32 bits (4 bytes).
- Multiple variables can be declared one after another, each requiring their own memory allocation.
- Memory addresses vary depending on hardware, OS, compiler, etc., typically incrementing by the size of the variable.
- Variable values can be changed later in the program by assigning new values, such as `points = 31;`.
- Once a variable is declared with a type, only values of that type can be assigned to it.
- Attempting to assign a different type will result in a compilation failure.

```c
// Declare a variable and assign it a value in C.
int points = 27;

// Two variables in C
int points = 27;
int year = 2020;
```

![](/images/09-04-01.png)

```c
// Setting a new points value in C
points = 31;
```

### 09.04.02 - Variables in Python

- Python allows variables to be declared and assigned without specifying a type.
- Unlike languages like C, Python recognizes the type of data without the need for explicit declaration.
- Variables in Python can change their type over time.
- In Python, the type is associated with the value, not the variable itself.
- A Python variable can refer to a value of any type.
- When a variable is assigned a new value in Python, it's actually binding to a value of a different type.
- In contrast to Python, in C, variables have a fixed type and can only hold values of that type.
- This distinction between Python and C explains why Python variables can be assigned values of different types while C variables cannot.

```python
# Python allows new variables without specifying a type.
age = 22
# Assigning a variable a value of a different type is valid in Python.
age = 'twenty-two'
```

## 09.05 - Stack and Heap Memory

- High-level languages abstract memory management details from programmers.
- Python abstracts memory allocation details, making them nearly invisible.
- C programming language exposes some memory management mechanisms.
- Regardless of visibility, programs typically use two types of memory: stack and heap.
- Stack memory is used for static memory allocation and is managed automatically.
- Heap memory is dynamically allocated and managed by the programmer.
- Understanding memory management is crucial for optimizing performance and preventing memory leaks in programs.
- Different programming languages handle memory management differently, affecting programmer control and performance.

### 09.05.01 - The Stack

- The stack operates on a last-in-first-out (LIFO) model.
- Memory stack is akin to a stack of plates, where adding a plate puts it on top and removing a plate takes the top one first.
- Items on the stack can be read or modified in any order, but removal happens in LIFO order.
- The stack pointer, a processor register, stores the memory address of the top value on the stack.
- Compiler-generated code uses the stack to track program execution and store local variables.
- Each thread of execution in a program has its own separate stack.
- Stack memory is fast and suitable for small memory allocations with limited scope.
- Stack has a limited memory allocation; excessive values cause a stack overflow failure.

![](/images/09-05-01.png)

### 09.05.02 - The Heap

- The heap is a memory pool suitable for large or long-lasting memory allocations.
- Unlike the stack, heap memory allocation doesn't follow a Last In First Out (LIFO) model.
- Heap memory can be accessed by any thread in a program, unlike stack memory which is specific to a thread.
- Memory allocated from the heap persists until it's explicitly freed by the program or the program terminates.
- Garbage collection is a common approach used by some programming languages to automatically free heap memory.
- In languages like C, programmers need to manually free heap memory using pointers to track allocations.
- A pointer in C is a variable holding a memory address, often used to reference memory allocations on the heap.
- Pointers can be stored in local stack variables and used to access memory on the heap.
- Example code in C illustrates the allocation of heap memory using the `malloc` function, storing the allocated memory's address in a pointer variable.

```c
// Declare a pointer variable
void * data;
// Allocate from heap and
// store address in variable
data = malloc(512);
```

![](/images/09-05-02.png)

## 09.06 - Math

- High-level programming languages simplify mathematical operations by providing symbols for common operations like addition, subtraction, multiplication, and division.
- Common mathematical operators include `+` for addition, `-` for subtraction, `*` for multiplication, and `/` for division.
- Assignment in programming languages is typically represented by the equals sign `=`, where `x = 5` sets the value of `x` to `5`.
- Programming languages like C and Python support both integer and floating-point arithmetic.
- Floating-point arithmetic allows representation of fractions, with floating-point variables declared using types like float or double in C and inferred in Python.
- Integer division in C can yield unexpected results, such as truncating fractions, while Python automatically handles types to allow for fractional results.
- Some languages offer shorthand mathematical operators, like increment `++` and decrement `--` in C, and `+=` and `-=` in both C and Python.
- C++ signifies its improvement upon the C language, which includes more features like shorthand operators.

![](/images/09-06-01.png)

```c
// Addition is easy in C.
cost = price + tax;

// Declaring a floating- point variable in C
double price = 1.99;

// Dividing integers in C
int x = 5;
int y = 2;
int z = x / y; // z is 2 not 2.5

// Dividing integers in C, result stored in a float
int x = 5;
int y = 2;
float z = x / y; // but both are integer so z is 2.0 not 2.5

// In C, we can add one to a variable the long way,
x = x + 1;
// or we can use this shortcut to increment x.
x++;
// On the other hand, this will decrement x.
x--;
```

```python
# Addition is easy in Python too.
cost = price + tax

# Declaring integer and floating- point variables in Python
year = 2020 # year is an int
price = 1.99 # price is a float

# In Python, we can add 3 to a variable like this...
cats = cats + 3
# Or we can do the same thing with this shortcut...
cats += 3
```

## 09.07 - Logic

- Processors excel at logical operations due to the digital circuit foundation.
- Programming languages offer logic-handling capabilities.
- High-level languages typically feature two types of operators: bitwise and Boolean.
- Bitwise operators manipulate integer bits, while Boolean operators handle true/false values.
- Terminology varies across languages: Python uses "bitwise" and "Boolean," C uses "bitwise" and "logical."
- Consistency with "bitwise" and "Boolean" terminology is suggested for clarity.

### 09.07.01 - Bitwise Operators

- Bitwise operators manipulate individual bits of integer values
- They perform logical operations such as AND, OR, XOR, and complement (~)
- Commonly used in languages like C and Python
- Example:
  - Python code snippet demonstrating bitwise `AND` `&` and OR `|`
  - Variables x and y are assigned values
  - Resulting values of a and b are calculated
- Bitwise `AND` operation explained:
  - Result is 1 when both inputs are 1
  - Bits are analyzed column-wise
  - Rightmost bit is 1 for both inputs, resulting in 0001 (decimal 1)
  - Therefore, variable a is assigned a value of 1
- Bitwise `OR` operation explained:
  - Result is 1 if either input (or both) is 1
  - Rightmost three bits are all 1 in one input or the other
  - Result is 0111 (decimal 7)
  - Therefore, variable b is assigned a value of 7

![](/images/09-07-01.png)

```python
# Python does bitwise logic.
x = 5
y = 3

# Bitwise AND : both bits are 1 => 1 otherwise 0
# x = 101
# y = 011
# a = 001
# a = 1
a = x & y

# Bitwise OR : either bits are 1 => 1 otherwise 0
# x = 101
# y = 011
# b = 111
# b = 7
b = x | y
```

![](/images/09-07-02.png)

#### Exercise 9-1: Bitwise Operators

Consider the following Python statements. What will be the values of a, b, and
c after this code executes?

```python
x = 11
# 11 in Binary is 1011

y = 5
# 5 in Binary is 0101

# Bitwise AND : both bits are 1 => 1 otherwise 0
a = x & y
# x = 1011
# y = 0101
# a = 0001
# a = 1

# Bitwise OR : either bits are 1 => 1 otherwise 0
b = x | y
# x = 1011
# y = 0101
# b = 1111
# b = 15

# Bitwise XOR : both bits MUST be different => 1 otherwise 0
c = x ^ y
# x = 1011
# y = 0101
# c = 1110
# c = 14
```

![](/images/09-07-03.png)

### 09.07.02 - Boolean Operators

- Boolean operators in high-level programming languages operate on Boolean values and yield Boolean results.
- Boolean values are either true or false, represented differently across programming languages.
- Boolean variables are a named memory address that hold a Boolean value true or false, such as `item_on_sale = True`.
- Expressions can evaluate to true or false without storing the result in a variable, like `item_cost > 5`.
- Boolean operators like AND, OR, and NOT allow logical operations on Boolean values.
- Example: Python's Boolean AND operator is `and`, while C uses `&&`.
- Comparison operators compare values and return true or false based on the comparison result.
- Examples of comparison operators include EQUALITY `==`, NOT EQUAL `!=`, GREATER THAN `>`, LESS THAN `<`, etc.
- Pay attention to the equality operator `==` for comparison and the assignment operator `=` for assigning values.
- Example: `x == 5` compares if `x` is equal to `5`, while `x = 5` assigns the value `5` to `x`.

![](/images/09-07-04.png)

![](/images/09-07-05.png)

## 09.08 - Program Flow

- Program flow, also known as control flow, determines the order in which statements are executed in a program.
- Boolean and comparison operators are used to evaluate expressions and conditions within the program.
- Program flow statements enable altering the behavior of a program based on conditions.
- Common program flow constructs include:
  - Conditional statements such as if, else, and switch, which execute certain blocks of code based on specified conditions.
  - Looping statements like for, while, and do-while, which repeat a block of code until a condition is met.
  - Control flow statements like break and continue, which affect the flow of execution within loops and switch statements.
- These constructs are fundamental in various programming languages for implementing decision-making and repetitive tasks.

### 09.08.01 - If Statements

- If statements are used in programming to execute code based on certain conditions.
- An if statement is followed by a condition that, if true, executes the code within the block.
- If the condition is false, the code within the else block executes.
- In Python, indentation is used to define code blocks, while in C, curly braces are used.
- Python also has elif statements, which are evaluated if the preceding if or elif statement is false.
- elif statements allow for multiple conditional checks in a structured manner.
- Both Python and C allow for the combination of if and else statements to create more complex conditional logic.

```python
# Age check in Python
if age < 18:
    print("You are a youngster!")
else:
    print("You are an adult.")

# A better age check in Python
if age < 13:
    print("You are a youngster!")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are older than a teen.")
```

```c
// Age check in C
if (age < 18)
{
  printf("You are a youngster!");
}
else
{
  printf("You are an adult.");
}

// A better age check in C
if (age < 13)
  printf("You are a youngster!");
else if (age < 20)
  printf("You are a teenager!");
else
  printf("You are older than a teen.");
```

### 09.08.02 - Looping

- Looping in Programming:
  - Allows repetitive actions until certain conditions are met.
  - Utilizes constructs like `while` and `for` loops.
- `while` Loop:
  - Runs code repeatedly until a condition is no longer met.
  - Example in Python and C to print numbers from 1 to 20.
  - Variable `n` initialized to 1, incremented until it reaches 21.
- `for` Loop:
  - Iterates over a range of values or collection of items.
  - Cleaner alternative for incrementing values.
  - Example in C printing numbers from 1 to 10, and Python printing animal names from a list.
- Python `for` Loop:
  - Allows iteration over a collection of values.
  - Example: Printing each animal name in a list.
  - Uses `for animal in animal_list:` syntax to iterate over `animal_list`.
- C `for` Loop:
  - Declares loop conditions in a single line.
  - Example: Printing numbers from 1 to 10.
  - Uses `for(int x = 1; x <= 10; x++)` syntax to control loop conditions and increments.

```python
# Count to 20 in Python.
n = 1
while n <= 20:
  print(n)
  n = n + 1

# Python uses a for loop to iterate over a collection.
# This will print each animal name in animal_list.
animal_list = ['cat', 'dog', 'mouse']
for animal in animal_list:
  print(animal)
```

```c
// Count to 20 in C.
int n = 1;
while(n <= 20)
{
  printf("%d\n", n);
  n++;
}

// C uses a for loop to iterate over a numeric range.
// This will print 1 through 10.
for(int x = 1; x <= 10; x++)
{
  printf("%d\n", x);
}
```

## 09.09 - Functions

- Looping allows for repetitive execution of instructions
- Functions are used to encapsulate sets of instructions for reuse
- Functions can be called from different parts of a program with varying inputs and outputs
- They optionally take inputs (parameters) and return outputs (return values)
- Different languages may use different terms for functions (subroutine, procedure, method)
- Functions help avoid duplicative code and adhere to the principle of "don't repeat yourself" (DRY)
- They encapsulate internal details while providing a clear interface for use
- Examples of functions include converting strings to lowercase, printing text, and downloading files from the internet

### 09.09.01 - Defining Functions

- Functions must be defined before they are used.
- Function definition includes: name, input parameters, body of the function, return value type (in some languages).
- Sample C function calculates area of a circle, returns a double.
- Function name: areaOfCircle, parameter: radius (double).
- Function body calculates area as π × radius^2 and returns it.
- Local variable 'area' is declared and used in the function body.
- Scope of 'area' variable is limited to the function.
- Python function for calculating area of a circle provided.
- Similar to C version, Python function calculates area and returns it.
- Both functions take one input parameter named 'radius'.
- C version explicitly defines return type and parameter type as double.
- Python function definition starts with 'def' keyword.

```c
// C function to calculate the area of a circle
double areaOfCircle(double radius)
{
  double area = 3.14 * radius * radius;
  return area;
}
```

```py
# Python function to calculate the area of a circle
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area
```

### 09.09.02 - Calling Functions

- Defining a function doesn't guarantee its execution; it requires a function call.
- Function call passes parameters and control to the function.
- After execution, the function returns control and possibly output to the caller.
- Example function calls in C and Python for calculating the area of a circle.
- Return values from function calls can be stored in variables.
- Ignoring the returned value is possible but often not useful.
- Illustration of function call process in Figure 9-5.
- Explanation of Python code calling the `area_of_circle` function with a radius of 2.0.
- The function computes the area based on the radius and returns it.
- Illustration of the call and return process in Figure 9-5 with radius = 2.0 and area = 12.56.

![](/images/09-09-01.png)

### 09.09.03 - Using Libraries

- Functions written by programmers for their own use are important, but leveraging functions from existing libraries is also crucial in programming.
- Programming languages typically have a standard library containing a wide range of functions.
- Libraries are collections of code meant to be used by other software.
- Both C and Python include standard libraries, covering tasks like printing, file manipulation, and text processing.
- Python's standard library is extensive and highly regarded.
- Many programming languages have additional libraries beyond the standard ones.
- Developers create libraries for others to use, often shared in the form of source code or compiled files.
- These libraries are sometimes informally shared, but some languages have established mechanisms for publishing and sharing them.
- A shared collection of libraries is called a package, and systems for managing and distributing these packages are known as package managers.
- While several package managers exist for C, none has achieved universal acceptance.
- Python's package manager is called pip, which facilitates easy installation of community-developed libraries and is widely used by Python developers.

## 09.10 - Object-Oriented Programming

- Object-Oriented Programming (OOP) is a programming paradigm where code and data are grouped into objects.
- Objects represent a logical grouping of data and functionality, modeling real-world concepts.
- OOP commonly uses a class-based approach.
- A class serves as a blueprint for objects, with methods (functions) and fields (variables).
- In Python, instance variables have different values for each object instance, while class variables have the same value across all instances.
- An example of a class is a BankAccount, with fields for balance and holder's name, and methods for withdrawing and depositing money.
- Objects are instances of classes; specific instances of bank accounts are created from the BankAccount class.
- Each object can have its own unique data, like name and balance.
- Methods can be used to modify object data, like depositing money into a bank account.

![](/images/09-10-01.png)

```py
# An example of a class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


# Creating instances of BankAccount class
harriet_account = BankAccount("Harriet Smith", 10)
emma_account = BankAccount("Emma Woodhouse", 100000)

# Depositing money into accounts
harriet_account.deposit(25)
emma_account.deposit(100)

print("Harriet's balance:", harriet_account.balance)  # 35
print("Emma's balance:", emma_account.balance)  # 100100
```

## 09.11 - Compiled or Interpreted

- Source code must be either compiled or interpreted for execution by CPUs.
- Compiled languages, like C, convert source code into machine instructions executable by the processor.
- Compiled code is delivered as binaries to end users, runs fast, but is architecture-specific.
- Interpreted languages, like Python, rely on an interpreter to read and execute source code at runtime.
- Interpreted code can be distributed as source code, making it platform-independent.
- Interpreted code runs slower due to interpretation overhead.
- Distribution of interpreted code requires users to have the necessary interpreter installed.
- Some languages use an intermediate language or bytecode, a hybrid approach between compilation and interpretation.
- Bytecode targets a virtual machine, providing platform independence while retaining performance gains.
- Examples include Java bytecode running on the Java Virtual Machine and C# bytecode on the .NET Common Language Runtime.

![](/images/09-11-01.png)

![](/images/09-11-02.png)

![](/images/09-11-03.png)

## 09.12 - Calculating a Factorial in C

- Introduction to implementing factorial algorithm in C for comparison with ARM assembly
- Example C code provided for calculating factorial of a number
- Explanation of how the function works internally using a while loop
- Mention of the flexibility of calling the function with different parameters
- Comparison between C and ARM assembly versions in terms of readability and processor specificity
- Highlighting the role of compilers in translating high-level code to machine code
- Demonstration of disassembling compiled C code into assembly language
- Noting the accessibility of examining assembly code of compiled programs
- Discussion on the adaptability of C code across different processors and operating systems
- Example provided with the same C code compiled for a 32-bit x86 processor on Windows
- Emphasis on the ease of understanding and portability offered by high-level languages like C compared to assembly

```c
// Calculate the factorial of n.
int factorial(int n)
{
  int result = n;
  while(--n > 0)
  {
    result = result * n;
  }
  return result;
}
```

ARM

```assembly
Address   Assembly
0001051c  sub r3, r0, #1
00010520  cmp r3, #0
00010524  bxle lr
00010528  mul r0, r3, r0
0001052c  subs r3, r3, #1
00010530  bne 00010528
00010534  bx lr
```

x86 32-bit Windows

```assembly
Address   Assembly
00406c35  mov ecx,dword ptr [esp+4]
00406c39  mov eax,ecx
00406c3b  jmp 00406c40
00406c3d  imul eax,ecx
00406c40  dec ecx
00406c41  test ecx,ecx
00406c43  jg 00406c3d
00406c45  ret
```

## 09.13 Summary

- High-level programming languages discussed
- Independent from specific CPU
- Closer to human language syntactically
- Covered common elements like comments, variables, functions, looping
- Examples shown in C and Python
- Example program in C examined
- Disassembled machine code shown from compiling high-level code

## Project #14 : Examine Variables

see `/projects/09-14/`

## Project #15 : Change The Type Of Value Referenced By A Variable In Python

## Project #16 : Stack Or Heap

## Project #17 : Write A Guessing Game

## Project #18 : Use A Bank Account Class In Python

## Project #19: Factorial In C
