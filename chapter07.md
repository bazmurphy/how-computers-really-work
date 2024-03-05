# Chapter 07 - Computer Hardware

## 07.01 - Computer Hardware Overview

- Computers differ from other electronic devices due to their programmability
- Programmability allows computers to execute new tasks without changing hardware
- Computer hardware comprises physical elements, distinct from software
- Hardware includes memory, CPU, and input/output devices
- Main memory, also known as RAM, is volatile and allows random access
- CPU, or processor, executes instructions specified in software
- Most CPUs are microprocessors (single integrated circuits) offering cost efficiency, reliability and performance
- Input/output devices (I/O) facilitate interaction between the computer and the outside world

![](/images/07-01-01.png)

## 07.02 - Main Memory

- Computer hardware requires storage for program instructions and data
- Main memory is used to store bits for CPU access
- Two common types of memory: SRAM (Static Random Access Memory) and DRAM (Dynamic Random Access Memory)
- SRAM is static and faster, DRAM is dynamic and cheaper
- A memory cell is the basic unit of memory (a circuit that can store a single bit)
- Imagine RAM as grids of memory cells, each single-bit cell can be identified using two-dimensional coordinates
- Memory addresses (numeric values) identify locations in memory
- Computers assign numeric addresses to bytes of memory and the CPU can read or write to those addresses
- Memory is byte-addressable, with each address representing 8 bits
- Main memory access involves reading or writing multiple bits in parallel
- Memory address layout requires consideration of bits needed for addressing
- A 64KB memory system with 16-bit memory addresses (Maximum Memory Address = 0xFFFF = 4 hex symbols x 4 bits)
- Memory representation using hexadecimal and ASCII characters
- Common memory inspection formats include tables and compact views
- Modern computing devices have significantly larger memory capacities

![](/images/07-02-01.png)

![](/images/07-02-02.png)

![](/images/07-02-03.png)

![](/images/07-02-04.png)

### Exercise 7-1: Calculate the Required Number of Bits

Using the techniques described, determine the number of bits required for addressing 4GB of memory.
You’ll want to look back at Table 1-3 for a reference on SI prefixes.
Remember that each byte is assigned a unique address, which is just a number.

giga = 1,073,741,824
x 4 = 4,294,967,296
unique addresses = 4,294,967,296
range of addresses = 0 to 4,294,967,295
4 x 4 x 4 x 4 x 4 x 4 x 4 x 4 = 4,294,967,296
4 x 8 = 32 bits
8 hex digits
lowest address (hex) = 0x00000000 = 0
highest address (hex) = 0xFFFFFFFF = 4,294,967,295

log2(4,294,967,296) = 32

## 07.03 - Central Processing Unit (CPU)

- Memory stores data and program instructions; CPU executes instructions.
- CPU enables flexibility to run various programs.
- Processor implements instructions for programmers to construct software.
- Types of instructions CPUs support:
  - Memory access (read, write)
  - Arithmetic (add, subtract, multiply, divide)
  - Logic (AND, OR, NOT)
  - Program flow (jump, call)
- Programs consist of ordered sets of CPU instructions.
- CPU reads program instructions from memory to run the program.
- Example program involves reading from memory, arithmetic operation, logical comparison, and conditional branching.
- Pseudocode used for human-readable description of program.
- Analogy: CPU is the cook, Program is the recipe, each Instruction is a step of the recipe that the cook knows how to perform

![](/images/07-03-01.png)

### 07.03.01 - Instruction Set Architectures

- CPUs implement various types of instructions, with differences across processors.
- CPUs sharing the same instructions constitute an Instruction Set Architecture (ISA).
- Two prevalent ISAs are x86 and ARM.
- x86 CPUs are common in desktops, laptops, and servers, with Intel leading and AMD also producing them.
- x86 architecture includes 16-bit, 32-bit, and 64-bit generations.
- The number of bits associated with a processor (bitness or word size) refers to the number of bits it can deal with at a time. So a 64-bit CPU can operate on values that are 64 bits in length.
- AMD introduced the first 64-bit x86 CPU, later adopted by Intel, known as x64 or x86-64.
- ARM processors dominate mobile devices, with ARM Holdings licensing designs to other companies.
- ARM architecture originated as 32-bit, with a 64-bit version introduced in 2011.
- ARM processors offer lower power consumption and cost, hence favored in mobile devices.
- While ARM CPUs can be used in PCs, x86 remains dominant due to software compatibility.
- Apple announced plans to transition macOS computers from x86 to ARM CPUs in 2020.

### 07.03.02 - CPU Internals

- CPU is multiple components that work together to execute instructions:
  - Processor Registers
  - Arithmetic Logic Unit (ALU)
  - Control Unit
- Processor registers hold data during processing, stored internally for fast access.
- Registers are small in size, typically measured in bits, and are part of the register file.
- ALU performs logical and mathematical operations, functioning as a complex combinational logic circuit.
- ALU takes operands and operation codes as inputs and outputs the result of the operation along with status.
- Control unit coordinates CPU operations, following a cycle of fetch, decode, and execute instructions.
- Control unit utilizes the program counter (PC) to determine the memory address of the next instruction.
- After fetching an instruction, the control unit decodes it, executes it, and updates the program counter.
- Execution of instructions may require coordination with other CPU components, such as the ALU.
- Control unit repeats the fetch-decode-execute cycle for each instruction.

![](/images/07-03-02.png)

### 07.03.03 - Clock, Cores, and Cache

- CPUs utilize clock signals to transition between states, with each pulse of the clock representing movement forward in executing instructions.
- Modern CPUs can execute multiple instructions in parallel through techniques like pipelining and multicore architecture.
- Clock speed, measured in GHz, determines how many instructions a CPU can perform per second, with higher frequencies allowing for more instructions.
- Increasing clock frequency faces limitations due to heat generation and practical upper limits on input clock frequency.
- Multicore CPUs feature multiple independent processing units called cores, allowing for parallel execution of tasks.
- Multicore architecture enhances performance by enabling simultaneous execution of multiple instructions, but software must be optimized to fully utilize this capability.
- CPU cache is a small, high-speed memory within the CPU that stores frequently accessed data to improve performance.
- CPUs check different cache levels (L1, L2, L3) before accessing main memory, with L1 being the fastest but smallest, and L3 being the slowest but largest.
- In multicore CPUs, some caches are specific to each core while others are shared among all cores.

![](/images/07-03-03.png)

![](/images/07-03-04.png)

![](/images/07-03-05.png)

![](/images/07-03-06.png)

## 07.04 - Beyond Memory and Processor

- Fundamental components for a computer: memory and processor.
- Gaps in functionality of a device with only memory and a processor:
  - Both memory and CPUs are volatile; they lose state without power.
  - Lack of interaction with the outside world.
- Secondary storage fills the gap of volatile memory, allowing data to persist without power.
- Input/output (I/O) devices provide a means for the computer to interact with the external environment.
- Both secondary storage and I/O devices are essential for creating a useful computing device beyond just memory and processor.

### 07.04.01 - Secondary Storage

- Without secondary storage, computers would lose all data when powered down, requiring users to reload the operating system and applications each time.
- Secondary storage is non-volatile and retains data even when the system is powered off.
- Unlike RAM, secondary storage is not directly accessible by the CPU.
- Secondary storage is cheaper per byte compared to RAM but slower, making it unsuitable as a replacement for main memory.
- Common types of secondary storage devices include hard disk drives (HDDs) and solid-state drives (SSDs).
- HDDs use magnetism on spinning platters, while SSDs use electrical charges in non-volatile memory cells.
- SSDs are faster, quieter, and more resistant to mechanical failure due to lacking moving parts compared to HDDs.
- Secondary storage devices allow computers to load data on demand, with the operating system and applications loading from secondary storage into main memory during startup.
- Program code and user data stored locally also load from secondary storage into main memory before use.
- Secondary storage is often referred to simply as "storage," while primary storage/main memory is called "memory" or "RAM."

### 07.04.02 - Input/Output

- Input/Output (I/O) devices facilitate communication between a computer and the outside world.
- They include devices like keyboards, mice, monitors, printers, and touchscreens.
- Human-computer interaction and computer-to-computer communication rely on I/O.
- Secondary storage devices, like hard drives, are considered I/O devices as well.
- CPUs communicate with I/O devices through physical address space.
- Physical address space encompasses memory addresses available to the hardware.
- CPUs communicate with I/O devices via memory-mapped I/O (MMIO).
- MMIO allows the CPU to interact with I/O devices by reading or writing to their assigned memory addresses.
- Some CPU families, like x86, use special instructions for accessing I/O devices.
- In x86 systems, devices are assigned I/O ports rather than memory addresses, known as port-mapped I/O (PMIO).
- x86 CPUs support both port-mapped and memory-mapped I/O.
- I/O ports and memory-mapped I/O addresses usually refer to device controllers rather than direct data storage.
- Device controllers provide interfaces for the CPU to request read or write operations to the device, like a hard disk drive.

![](/images/07-04-02.png)

![](/images/07-04-03.png)

## 07.05 - Bus Communication

- Bus communication is crucial in computer systems for communication between the CPU, memory, and I/O devices.
- A bus is a hardware communication system, initially consisting of parallel wires for transferring data in parallel.
- Today's bus designs are more complex but serve the same purpose.
- There are three common bus types: address bus, data bus, and control bus.
- The address bus selects the memory address that the CPU wants to access.
- The data bus transmits values read from or written to memory.
- The control bus manages operations over the address and data buses.
- The CPU utilizes these buses to read and write to memory and communicate with I/O devices.
- In the example provided, the CPU writes the memory address to the address bus and sets control signals for read or write operations.
- The memory controller retrieves the data from memory and writes it to the data bus for the CPU to read.

![](/images/07-05-01.png)

### Exercise 7-2: Get To Know The Hardware Devices In Your Life

- What kind of CPU does the device have?
  - Apple M2 Pro (5nm TSMC)
- Is the CPU 32-bit or 64-bit (or something else)?
  - 64-bit
- What’s the CPU clock frequency?
  - 3.5 Ghz
- Does the CPU have L1, L2, or L3 cache? If so, how much?
  - L1: Performance cores 192+128 KB per core | Efficiency cores 128+64 KB per core
  - L2: Performance cores 32 MB | Efficiency cores 4 MB
  - L3: 24 MB
- Which instruction set architecture does the CPU use?
  - ARMv8.6-A
- How many cores does the CPU have?
  - 12 (8 Performance 4 Efficiency)
- How much and what kind of main memory does the device have?
  - 32 GB
- How much and what kind of secondary storage does the device have?
  - 512 GB SSD
- What I/O devices does the device have?
  - Thunderbolt 4 ports, HDMI port, SDXC card slot, 3.5mm headphone jack, Wi-Fi 6E, Bluetooth 5.3

## 07.06 - Summary

- Covered computer hardware basics: CPU, RAM, and I/O devices.
- Memory composition: single-bit memory cells using flip-flops (SRAM) and transistors with capacitors (DRAM).
- Memory addressing explained: each address refers to a byte of memory.
- CPU architectures discussed: x86 and ARM.
- Internal workings of CPUs explored: registers, ALU, and control unit.
- Secondary storage and other I/O types mentioned.
- Bus communication overviewed.
