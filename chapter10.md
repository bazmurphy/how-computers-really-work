# Chapter 10 - Operating Systems

## 10.01 - Programming Without an Operating System

- Operating systems act as intermediaries between hardware and other software.
- Devices without an OS allow software to have direct access to hardware.
- Early video game consoles like Atari 2600, Nintendo Entertainment System, and Sega Genesis operated without an OS.
- Game software ran directly on the console hardware without any intermediary layer.
- Inserting a cartridge and turning on the system initiated the game.
- Game consoles of this era could run only one program at a time, the game from the cartridge.
- No background programs or multitasking capabilities existed; the game had complete hardware attention.
- Game developers had to control hardware directly with code, including system initialization, video hardware control, and controller input reading.
- Different console hardware had distinct designs, requiring developers to understand specific hardware intricacies.
- Despite hardware variations, consoles maintained consistent designs during manufacturing years.
- NES consoles, for instance, shared the same processor, RAM, PPU, and APU.
- Developers needed a deep understanding of the hardware but could target code to specific hardware for optimal performance.
- Porting games to different consoles often required rewriting substantial portions of code.
- Game cartridges included similar code for fundamental tasks like hardware initialization.
- Developers reused code but still faced similar challenges repeatedly, resulting in varied levels of success.

![](/images/10-01-01.png)

## 10.02 - Operating Systems Overview

- Operating systems (OS) serve as a bridge between software and hardware, facilitating program execution and system management.
- OS allows programs to request system services such as storage access and network communication.
- Functions include system initialization, multitasking, and resource management to ensure efficient program execution.
- OS maintains isolation between programs and users, ensuring appropriate access levels.
- Conceptually, the OS sits between hardware and applications, abstracting hardware details for developers.
- Components of an OS can be broadly categorized into the kernel and non-kernel components.
- The kernel manages memory, facilitates I/O operations, and provides system services for applications.
- Non-kernel components include the shell, which provides a user interface, either CLI or GUI.
- Daemons or services run in the background, offering additional functionalities like scheduling tasks.
- OS includes software libraries for developers and basic applications like text editors and calculators.
- Device drivers facilitate communication between the OS kernel and specific hardware devices.
- OS often includes standard utilities and applications, though they may not be considered part of the core OS functionality.

![](/images/10-02-01.png)

![](/images/10-02-02.png)

## 10.03 - Operating System Families

- **Unix-like Operating Systems:**
  - Unix-like operating systems behave similarly to Unix.
  - Examples include Linux, macOS, iOS, and Android.
  - Unix originated at Bell Labs in the 1960s.
  - Supports multiple users, multitasking, and hierarchical directory structure.
  - Strong presence on servers, personal computers, and smartphones.
  - Robust command line shell with well-defined standard tools.
- **Linux:**
  - Kernel developed by Linus Torvalds, aiming to mimic Unix.
  - Open source, freely available, with many distributions.
  - Often bundled with GNU software.
  - Collaboration with GNU to create a complete operating system.
  - Commonly used in servers, embedded systems, smartphones, and Raspberry Pi OS.
- **Microsoft Windows:**
  - Dominant on personal computers and servers.
  - Roots not traced back to Unix; based on MS-DOS initially.
  - Windows NT introduced as a new kernel-based operating system.
  - Designed for portability, software compatibility, multi-user support, security, and reliability.
  - Developed by Dave Cutler, incorporating elements from VMS operating system.
  - Windows NT initially targeted at business, later integrated into consumer-focused releases.
  - All desktop and server versions since Windows XP built on NT kernel.

![](/images/10-03-01.png)

## 10.04 - Kernel Mode and User Mode

- An operating system ensures programs behave well.
- Programs must not interfere with each other or with the kernel.
- Users cannot modify system files.
- Applications cannot directly access hardware; requests must go through the kernel.
- CPU capability grants special rights to the operating system while restricting other code.
- This capability is known as the privilege level of the code.
- Processors may offer more than two levels of privilege, but most OSes use two.
- Higher privilege level: kernel mode (also known as supervisor mode).
- Lower privilege level: user mode.
- Code in kernel mode has full system access, including memory, I/O devices, and special CPU instructions.
- Code in user mode has limited access.
- Kernel and many device drivers run in kernel mode.
- Everything else runs in user mode.

- Microsoft Windows has several major components operating in kernel mode.
- Kernel mode capabilities in Windows are divided between two components: the kernel and the executive.
- This division is significant mainly for discussions on Windows' internal architecture.
- From a user or developer perspective, this separation is not typically a concern.
- Both the kernel and executive's compiled machine code are contained within the same file (ntoskrnl.exe).
- Distinction between the Windows NT kernel and executive won't be made further in this book.
- Aside from the kernel, executive, and device drivers, Windows also has other significant components in kernel mode.
- The Hardware Abstraction Layer (HAL) isolates the kernel, executive, and device drivers from low-level hardware differences.
- This isolation includes variations in motherboards and other hardware specifics.
- The windowing and graphics system (win32k) facilitates graphic rendering and programmatic user interface interactions.

![](/images/10-04-01.png)

## 10.05 - Processes

- An operating system facilitates program execution by creating processes.
- Programs, stored as sequences of machine instructions in executable files, need processes to run.
- Processes contain the program's instructions loaded into memory and manage their execution by the CPU.
- Processes ensure program behavior and prevent misbehavior.
- Each running instance of a program is a process.
- User mode operations, like shell, services, and utilities, execute within processes.
- Processes have a private virtual memory address space and contain information about the program's state.
- Every process has a unique identifier called a process identifier (PID).
- Processes have parent-child relationships, forming a process tree.
- Orphan processes have no parent; on Linux, they're typically adopted by the init process.
- Figure 10-6 illustrates a process tree in Raspberry Pi OS, generated using the pstree utility.
- The pstree command shows the hierarchy of processes, including the parent-child relationships.
- On Windows, Process Explorer provides a graphical representation of running processes.

![](/images/10-05-01.png)

<details>
<summary>pstree output</summary>

```sh
baz@baz-pc:~$ pstree
systemd─┬─ModemManager───3*[{ModemManager}]
        ├─NetworkManager───3*[{NetworkManager}]
        ├─accounts-daemon───3*[{accounts-daemon}]
        ├─avahi-daemon───avahi-daemon
        ├─bluetoothd
        ├─colord───3*[{colord}]
        ├─containerd───18*[{containerd}]
        ├─cron
        ├─cups-browsed───3*[{cups-browsed}]
        ├─cupsd
        ├─dbus-daemon
        ├─dnsmasq───dnsmasq
        ├─dockerd───20*[{dockerd}]
        ├─flatpak-system-───3*[{flatpak-system-}]
        ├─fwupd───5*[{fwupd}]
        ├─gdm3─┬─gdm-session-wor─┬─gdm-wayland-ses─┬─gnome-session-b───3*[{gnome-session-b}]
        │      │                 │                 └─3*[{gdm-wayland-ses}]
        │      │                 └─3*[{gdm-session-wor}]
        │      └─3*[{gdm3}]
        ├─irqbalance───{irqbalance}
        ├─2*[kerneloops]
        ├─mount.ntfs
        ├─nvidia-persiste
        ├─packagekitd───3*[{packagekitd}]
        ├─polkitd───3*[{polkitd}]
        ├─2*[postgres───5*[postgres]]
        ├─power-profiles-───3*[{power-profiles-}]
        ├─rsyslogd───3*[{rsyslogd}]
        ├─rtkit-daemon───2*[{rtkit-daemon}]
        ├─snapd───23*[{snapd}]
        ├─switcheroo-cont───3*[{switcheroo-cont}]
        ├─systemd─┬─(sd-pam)
        │         ├─at-spi2-registr───3*[{at-spi2-registr}]
        │         ├─chrome_crashpad───2*[{chrome_crashpad}]
        │         ├─dbus-daemon
        │         ├─dconf-service───3*[{dconf-service}]
        │         ├─evolution-addre───6*[{evolution-addre}]
        │         ├─evolution-calen───9*[{evolution-calen}]
        │         ├─evolution-sourc───4*[{evolution-sourc}]
        │         ├─gcr-ssh-agent───2*[{gcr-ssh-agent}]
        │         ├─2*[gjs───11*[{gjs}]]
        │         ├─gnome-keyring-d───4*[{gnome-keyring-d}]
        │         ├─gnome-session-b─┬─at-spi-bus-laun─┬─dbus-daemon
        │         │                 │                 └─4*[{at-spi-bus-laun}]
        │         │                 ├─evolution-alarm───6*[{evolution-alarm}]
        │         │                 ├─gnome-software───7*[{gnome-software}]
        │         │                 ├─gsd-disk-utilit───3*[{gsd-disk-utilit}]
        │         │                 ├─python3───3*[{python3}]
        │         │                 ├─update-notifier───4*[{update-notifier}]
        │         │                 └─4*[{gnome-session-b}]
        │         ├─gnome-session-c───{gnome-session-c}
        │         ├─gnome-shell─┬─Xwayland
        │         │             ├─code─┬─code───code───58*[{code}]
        │         │             │      ├─code───code─┬─code───24*[{code}]
        │         │             │      │             └─code───10*[{code}]
        │         │             │      ├─code───7*[{code}]
        │         │             │      ├─code───14*[{code}]
        │         │             │      ├─code─┬─2*[bash]
        │         │             │      │      └─16*[{code}]
        │         │             │      ├─code───16*[{code}]
        │         │             │      ├─code─┬─3*[code───7*[{code}]]
        │         │             │      │      ├─code───11*[{code}]
        │         │             │      │      └─15*[{code}]
        │         │             │      └─38*[{code}]
        │         │             ├─firefox─┬─Isolated Servic───27*[{Isolated Servic}]
        │         │             │         ├─2*[Isolated Web Co───27*[{Isolated Web Co}]]
        │         │             │         ├─Isolated Web Co───41*[{Isolated Web Co}]
        │         │             │         ├─MainThread───2*[{MainThread}]
        │         │             │         ├─Privileged Cont───26*[{Privileged Cont}]
        │         │             │         ├─RDD Process───2*[{RDD Process}]
        │         │             │         ├─Socket Process───5*[{Socket Process}]
        │         │             │         ├─Utility Process───5*[{Utility Process}]
        │         │             │         ├─3*[Web Content───12*[{Web Content}]]
        │         │             │         ├─WebExtensions───29*[{WebExtensions}]
        │         │             │         ├─file:// Content───27*[{file:// Content}]
        │         │             │         └─141*[{firefox}]
        │         │             ├─mutter-x11-fram───37*[{mutter-x11-fram}]
        │         │             └─17*[{gnome-shell}]
        │         ├─gnome-shell-cal───6*[{gnome-shell-cal}]
        │         ├─gnome-terminal-─┬─bash───pstree
        │         │                 └─6*[{gnome-terminal-}]
        │         ├─goa-daemon───4*[{goa-daemon}]
        │         ├─goa-identity-se───3*[{goa-identity-se}]
        │         ├─gsd-a11y-settin───4*[{gsd-a11y-settin}]
        │         ├─gsd-color───4*[{gsd-color}]
        │         ├─gsd-datetime───4*[{gsd-datetime}]
        │         ├─gsd-housekeepin───4*[{gsd-housekeepin}]
        │         ├─gsd-keyboard───4*[{gsd-keyboard}]
        │         ├─gsd-media-keys───4*[{gsd-media-keys}]
        │         ├─gsd-power───4*[{gsd-power}]
        │         ├─gsd-print-notif───3*[{gsd-print-notif}]
        │         ├─gsd-printer───3*[{gsd-printer}]
        │         ├─gsd-rfkill───3*[{gsd-rfkill}]
        │         ├─gsd-screensaver───3*[{gsd-screensaver}]
        │         ├─gsd-sharing───4*[{gsd-sharing}]
        │         ├─gsd-smartcard───4*[{gsd-smartcard}]
        │         ├─gsd-sound───4*[{gsd-sound}]
        │         ├─gsd-wacom───4*[{gsd-wacom}]
        │         ├─gsd-xsettings───4*[{gsd-xsettings}]
        │         ├─gvfs-afc-volume───4*[{gvfs-afc-volume}]
        │         ├─gvfs-goa-volume───3*[{gvfs-goa-volume}]
        │         ├─gvfs-gphoto2-vo───3*[{gvfs-gphoto2-vo}]
        │         ├─gvfs-mtp-volume───3*[{gvfs-mtp-volume}]
        │         ├─gvfs-udisks2-vo───4*[{gvfs-udisks2-vo}]
        │         ├─gvfsd─┬─gvfsd-dnssd───3*[{gvfsd-dnssd}]
        │         │       ├─gvfsd-network───4*[{gvfsd-network}]
        │         │       ├─gvfsd-recent───3*[{gvfsd-recent}]
        │         │       ├─gvfsd-trash───4*[{gvfsd-trash}]
        │         │       └─3*[{gvfsd}]
        │         ├─gvfsd-fuse───6*[{gvfsd-fuse}]
        │         ├─gvfsd-metadata───3*[{gvfsd-metadata}]
        │         ├─ibus-daemon─┬─ibus-dconf───4*[{ibus-dconf}]
        │         │             ├─ibus-engine-sim───3*[{ibus-engine-sim}]
        │         │             ├─ibus-extension-───4*[{ibus-extension-}]
        │         │             └─3*[{ibus-daemon}]
        │         ├─ibus-portal───3*[{ibus-portal}]
        │         ├─ibus-x11───3*[{ibus-x11}]
        │         ├─2*[pipewire───2*[{pipewire}]]
        │         ├─pipewire-pulse───2*[{pipewire-pulse}]
        │         ├─snap───14*[{snap}]
        │         ├─snapd-desktop-i───snapd-desktop-i───3*[{snapd-desktop-i}]
        │         ├─ssh-agent
        │         ├─tracker-miner-f───6*[{tracker-miner-f}]
        │         ├─ubuntu-report───6*[{ubuntu-report}]
        │         ├─wireplumber───5*[{wireplumber}]
        │         ├─xdg-desktop-por───7*[{xdg-desktop-por}]
        │         ├─2*[xdg-desktop-por───4*[{xdg-desktop-por}]]
        │         ├─xdg-document-po─┬─fusermount3
        │         │                 └─7*[{xdg-document-po}]
        │         └─xdg-permission-───3*[{xdg-permission-}]
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-machine
        ├─systemd-oomd
        ├─systemd-resolve
        ├─systemd-timesyn───{systemd-timesyn}
        ├─systemd-udevd
        ├─teamviewerd───28*[{teamviewerd}]
        ├─udisksd───6*[{udisksd}]
        ├─unattended-upgr───{unattended-upgr}
        ├─upowerd───3*[{upowerd}]
        └─wpa_supplicant

```

</details>

## 10.06 - Threads

- By default, programs execute instructions sequentially, handling one task at a time.
- Threads allow programs to perform multiple tasks in parallel.
- Threads are schedulable units of execution within a process.
- Threads run within a process and share resources with other threads in the same process.
- Processes may create multiple threads as needed for parallel processing.
- Threads have identifiers called thread IDs (TIDs).
- Windows treats threads and processes as distinct object types, while Linux uses a single data type for both.
- In Linux, threads that share an address space and have a common process identifier are considered a process.
- Linux terminology for process and thread identifiers can be confusing; a process has a process ID (PID) and a thread has a thread ID (TID) in user mode, but the Linux kernel refers to the thread ID as PID and the process ID as a thread group identifier (TGID).
- Not all threads can run simultaneously; the number of processor cores determines how many threads can run at once.
- Physical cores are hardware implementations within a CPU, while logical cores represent a single physical core's ability to run multiple threads at once.
- The operating system's scheduler ensures that threads get their turn to run, typically by giving each thread a short period of time (quantum) before suspending it to allow another thread to run.
- Developers write multithreaded applications as if all threads were running continuously in parallel, though the scheduler manages the actual execution.

![](/images/10-06-01.png)

## 10.07 - Virtual Memory

- **Operating systems and Memory Management:**
  - Support for multiple running processes, each requiring memory.
  - Isolation between processes to prevent data theft or corruption.
  - Each process is provided with virtual memory for abstraction.
- **Virtual Memory Addressing:**
  - Hardware assigns physical addresses to memory.
  - Operating systems present processes with virtual memory.
  - Virtual addresses are translated to physical addresses when needed.
- **Advantages of Virtual Memory:**
  - Each process has its own private range of virtual memory.
  - Same virtual address for different programs maps to different physical addresses.
  - Ensures separation of memory between processes, preventing corruption.
- **Usage of Virtual Memory:**
  - Virtual address range doesn't represent mapped physical memory entirely.
  - Kernel has a separate virtual address space shared by kernel mode code.
  - Virtual address space divided between user mode and kernel mode.
- **Paging and Virtual Memory Management:**
  - Paging allows for greater virtual memory usage.
  - Least used memory is paged first to secondary storage.
  - Performance hit incurred while moving bytes to and from secondary storage.
- **Transition to 64-bit Operating Systems:**
  - 64-bit processors and operating systems offer much larger address spaces.
  - 64-bit OS uses a smaller number of bits to represent addresses.
  - Support for 48-bit addresses, providing 256TB of virtual address space.

![](/images/10-06-01.png)

![](/images/10-06-02.png)

## 10.08 - Application Programming Interface (API)

- Application Programming Interface (API):
  - User interface (UI) is a small part of the operating system's code.
  - Operating system's API is crucial for software developers.
  - APIs not only for operating systems but for any software allowing programmatic interaction.
- OS API:
  - Specification defined in source code and documentation.
  - Includes functions, inputs, outputs, and data structures.
  - Implementation provided by software libraries.
  - Developers "call" or "use" APIs to invoke functions.
- UI vs. API:
  - UI defines OS's personality for users.
  - API defines OS's personality for applications.
- Interaction with OS:
  - Users interact with UI (shell), which translates commands into API calls.
  - Applications call API directly without going through UI.
- Example: Creating a File via API:
  - Unix/Linux: Use `open` function.
  - Windows: Use `CreateFileA` function.
  - Both examples demonstrate using the C programming language.
- Cross-Language and OS Compatibility:
  - APIs must be called regardless of the programming language.
  - Languages wrap API calls, ensuring portability.
  - Example: Using `fopen` function in C for file creation.
- Example: Python Code for File Creation:
  - Python interpreter handles API calls.
  - Code is compatible with any OS with a Python interpreter.
- POSIX Standard for Unix-like Systems:
  - Defines a standard for OS API, shell behavior, and utilities.
  - Provides a baseline for Unix-like operating systems.
- OS-specific APIs:
  - Cocoa for macOS, Cocoa Touch for iOS.
  - Android Platform APIs for Android OS.
- Windows API Evolution:
  - Win16 for 16-bit Windows.
  - Win32 for 32-bit Windows.
  - Win64 for 64-bit Windows.
  - Universal Windows Platform (UWP) introduced in Windows 10 for consistent app development across devices.

```c
// Unix/Linux API to create a file in C
open("hello.txt", O_WRONLY|O_CREAT);
```

```c
// Windows API to create a file in C
CreateFileA("hello.txt", GENERIC_WRITE, 0, NULL,
  CREATE_NEW, FILE_ATTRIBUTE_NORMAL, NULL);
```

```c
// Any OS create a file using fopen (from the standard library) in C
fopen("hello.txt", "w");
```

```python
# Any OS create a new file in python
open('hello.txt', 'w')
```

![](/images/10-08-01.png)

## 10.09 - The User Mode Bubble and System Calls

- User mode code capabilities:
  - Read and write to its own virtual memory
  - Perform mathematical and logical operations
  - Control program flow of its own code
- Limitations of user mode code:
  - Cannot access physical memory addresses
  - Cannot perform I/O directly
- Interaction with the outside world:
  - User mode code can request kernel mode code to perform operations on its behalf
  - This request is known as a system call
- Example of system call:
  - Reading from a file requires a system call to the kernel
  - Kernel performs necessary I/O operations and provides data back to user mode process
- Kernel abstraction:
  - Kernel encapsulates hardware details, allowing user mode code to perform tasks without knowledge of underlying hardware
- CPU instructions for system calls:
  - ARM processors: SVC instruction
  - x86 processors: SYSCALL and SYSENTER instructions
- Implementation of system calls:
  - Both Linux and Windows implement a variety of system calls
  - Each call is identified by a unique number
- Making a system call:
  - Program loads desired system call number into a processor register
  - Additional parameters are placed in specific registers
  - System call instruction is executed
- Ease of making system calls:
  - Operating systems and high-level programming languages provide interfaces for making system calls
  - Programmers may not realize they are making a system call as it's abstracted by the OS API or language's standard library.

![](/images/10-09-01.png)

![](/images/10-09-02.png)

![](/images/10-09-03.png)

## 10.10 - APIs and System Calls

- Definition and Relationship
  - Operating system API vs. system calls
  - Related but not equivalent
  - API: Interaction with OS regardless of kernel mode
  - System calls: User mode requests for kernel mode services
- Linux Example
  - Linux API as a specification for using Linux system calls
  - OSes based on Linux (e.g., Android) have their own APIs (Android Platform APIs)
- Microsoft Windows Example
  - Windows NT kernel provides system calls through Native API
  - Windows API: Wrapper around Native API, used by developers
  - Rare direct use of Native API by application developers
  - Windows API functions: Some require system calls, others do not
    - Example: CreateFileW (requires system call)
    - Example: PathFindFileNameW (does not require system call)
      - Uses virtual memory access, possible in user mode
- Recap
  - Operating system API: Programmatic interface for OS
  - System calls: User mode requests for privileged kernel mode operations
  - API functions: Some rely on system calls, others do not

## 10.11 - Operating System Software Libraries

- Definition and Purpose
  - Describes the programmatic interface to an operating system
  - Concrete method of invoking the API via software libraries
- Characteristics
  - Collection of code included with the OS
  - Implements OS API operations
- Comparison with Language Libraries
  - Similarities and differences
- Structure and Functionality
  - File containing machine code
  - Exports functions for use by programs
- Example: GNU C Library (glibc) in Linux
  - Functions and system calls integration
  - Standard library functionalities
- Example: Windows API
  - Extensiveness and evolution
  - Key library files: kernel32.dll, user32.dll, gdi32.dll
  - Dynamic link libraries (dll) explanation
- Direct System Calls vs. Software Libraries
  - Pros and cons
  - Limitations and compatibility concerns
- Windows Subsystem for Linux (WSL)
  - Introduction and Purpose
    - Integration of Linux programs on Windows
  - Evolution of WSL
    - Intercepting system calls in the first version
    - Incorporating a real Linux kernel in the second version
  - Compatibility and Functionality
    - Enabling Linux executables to run on Windows without modification
    - Virtual machine setup alongside the NT kernel

![](/images/10-11-01.png)

## 10.12 - Application Binary Interface

- Application Binary Interface (ABI)
  - Defines machine code interface to a software library
  - Contrasts with API which defines a source code interface
  - API remains consistent across processor families; ABI varies
- Developer writes code utilizing OS API, compiles for multiple processor types
  - Source code targets common API
  - Compiled code targets architecture-specific ABI
- Compiled machine code adheres to ABI for target architecture
  - At execution, ABI defines interaction between programs and libraries
- Importance of consistent ABI in OS libraries
  - Allows older programs to run on newer OS releases without recompilation

## 10.13 - Device Drivers

- Computers support various hardware devices like displays, keyboards, and cameras, each with its own input/output interface.
- Different device types have different I/O needs; for example, a Wi-Fi adapter functions differently from a game controller.
- Even devices of the same type may implement different I/O approaches; for instance, two video card models may communicate differently with the system.
- Direct hardware interactions are limited to code running in kernel mode.
- However, expecting the operating system kernel to communicate with every device is unreasonable.
- Device drivers bridge this gap by interacting with hardware and providing a programmatic interface.
- Device drivers are typically implemented as kernel modules to access hardware.
- Kernel modules allow drivers wide-ranging access, akin to the kernel itself, necessitating the installation of trusted drivers only.
- The kernel collaborates with device drivers to interact with hardware on behalf of user-mode code.
- This enables hardware interactions without requiring applications or the OS to understand specific hardware details, a form of encapsulation.
- Some drivers can execute in user mode, but they still rely on a kernel-mode component, often provided by the operating system, for handling hardware interactions.

## 10.14 - Filesystems

- **Filesystems Overview:**
  - Secondary storage common in computers: HDD or SSD.
  - Storage devices contain bits, maintain data even when powered down.
  - Divided into partitions.
  - Operating systems implement filesystems to organize data into files and directories.
  - Partitions must be formatted with a specific filesystem for OS use.
- **Types of Filesystems:**
  - Linux commonly uses ext (extended) family (ext2, ext3, ext4).
  - Windows uses FAT (File Allocation Table) and NTFS (NT File System).
  - Different OSes support different filesystems.
- **Volume vs. Partition:**
  - Some systems present storage as a volume, logical abstraction built on partitions.
  - Filesystems reside on volumes, not partitions.
- **File and Directory Structure:**
  - File: container of data.
  - Directory (folder): container of files or directories.
  - Unix-like systems: hierarchical directory structure starting from root `/`.
  - Example: `/usr/lib `- `usr` is a subdirectory of `root`, `lib` is a subdirectory of `usr`.
- **Mounting Devices:**
  - Additional storage devices mapped to directory structure.
  - USB drive example: mounted to `/mnt/usb1`.
- **Windows File and Directory Structure:**
  - Windows assigns drive letters (A–Z) to volumes.
  - Each drive has its own root and directory hierarchy.
  - Windows uses backslash `\` in directory paths, colon `:` after drive letter.
  - Example: `C:\windows\system32` - C drive contains system files.

## 10.15 - Services and Daemons

- Operating systems facilitate processes running automatically in the background without user interaction
- These processes are termed as services in Windows and daemons in Unix-like systems
- Default services include network configuration and scheduled tasks
- Services provide capabilities not tied to a specific user, don't require kernel mode, but need to be available on demand
- Operating systems typically have a component for managing services
- Some services start at OS boot, others in response to events, and some need to be restarted after failure
- In Windows, the Service Control Manager (SCM) handles these functions, with its executable file services.exe
- Many Linux distributions utilize systemd for managing daemons, although other methods are available
- systemd also serves as the init process in Linux, starting early in the boot process and running throughout
- The term "daemon" in Unix and Linux is derived from Maxwell's demon, a hypothetical entity in a physics thought experiment
- Daemon, pronounced "DAY-mon," operates in the background similar to computer daemons
- "Daemon" outside computing is typically pronounced as "demon"
- Historically, "service" was a Windows-specific term, now also used in Linux to refer to daemons started by systemd

## 10.16 - Security

- An operating system provides a security model for the code that runs on it
- Security entails restricting software and users to appropriate system parts
- Mistakes by users, like running untrustworthy code, can compromise security
- OS helps limit damage by restricting access if malicious software is run
- Shared systems should prevent users from accessing each other's data by default
- OS implements various techniques for security:
  - Applications are segregated in a user mode bubble to prevent interference
  - Filesystem security ensures data in files can only be accessed by appropriate users/processes
  - Virtual memory can be secured with read-only or executable regions to limit misuse
  - Login system manages security based on user identity
- Security vulnerabilities are regularly discovered in operating systems
- Keeping modern internet-connected OS up-to-date with latest updates is critical for security

## 10.17 - Summary

- Operating systems: software facilitating communication with computer hardware and enabling program execution
- Covered components: operating system kernel, non-kernel components, and the differentiation between kernel mode and user mode
- Discussed dominant operating system families: Unix-like systems and Microsoft Windows
- Highlighted the concept of processes as containers for programs, with the ability for multiple threads to run concurrently within a process
- Explored programmatically interacting with an operating system: API, system calls, software libraries, and ABI

## 10.18 - Project 20: Examine a Running Process

## 10.19 - Project 21: Create a Thread and Observe It

## 10.20 - Project 22: Examine Virtual Memory

## 10.21 - Project 23: Try the Operating System API

## 10.22 - Project 24: Observe System Calls

## 10.23 - Project 25: Use glibc

## 10.24 - Project 26: View Loaded Kernel Modules

## 10.25 - Project 27: Examine Storage Devices and Filesystems

## 10.26 - Project 28: View Services
