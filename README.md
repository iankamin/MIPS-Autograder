# MIPS Autograder

This program will generate assembly code for a MIPS subroutine. You provide the input registers, initial data section, any User Input, and the output registers and their corresponding expected answers.

NOTE: All tests will be run on one emulator instance meaning that if one test fails all following tests may also fail. 

This Program was intended for use by teachers and was designed to be used with [Autolabs](https://autolabproject.com).

## Table of Contents
- [MIPS Autograder](#mips-autograder)
  - [Table of Contents](#table-of-contents)
- [Known Bugs](#known-bugs)
- [**Installation**](#installation)
  - [Mac](#mac)
  - [Windows](#windows)
  - [Linux](#linux)
    - [Build Instructions](#build-instructions)
  - [Usage Instructions (TODO)](#usage-instructions-todo)
  - [Author](#author)
  - [Copyright Information](#copyright-information)

However this program can be used as a testbench for MIPS code as well.

## Known Bugs

1. *Bug:* Read Character (Syscall 12) does not function correctly.
   
   *fix:* Have the students always use read string (See bug 2 for more details) 

2. *Bug:* Read String requires and additional character for the input buffer.
        For example:
~~~
  la $a0, userinput1
  li $a1, 3
  li $v0, 8
  syscall
  
  la $a0, userinput2
  li $a1, 3
  li $v0, 8
  syscall
~~~
  if the student were to input *'aaa'* followed by *'bbb'* 
  this would work correctly on the local machine resulting in
~~~
  userinput1: 'aaa'
  userinput2: 'bbb'
~~~
  however Autograder would result in the following
~~~
  userinput1: 'aaa'
  userinput2: ''
~~~
  
  **CAUSE:** The autograder requires space for a newline character after the string is input
  
  **FIX:** have the students always use a fixed buffer size larger than the number of input characters.
  If the largest input will be 4 characters have the student set $a1 to 16





# **Installation**

## Mac
Currently There is no executable for mac
1. Clone The Repo
   ~~~
   git clone https://github.com/iankamin/MIPS-Autograder
   ~~~
2. install required python modules
   ~~~
   pip3 install PyQt5
   ~~~ 
3. Install Homebrew
   ~~~
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ~~~
4. Install SPIM
   ~~~
   brew install spim
   ~~~
5. run the program
   ~~~
   cd MIPS_Autograder
   python3 
   ~~~

## Windows
1. This program has no dependencies for Windows simply download the latest release and you're good to go
2. Download latest .exe release file here https://github.com/iankamin/MIPS-Autograder/release
3. double click to run

## Linux
1.  install SPIM emulator
    ~~~
    sudo apt install spim
    ~~~
2. Download latest .bin release file here https://github.com/iankamin/MIPS-Autograder/releases
   


### Build Instructions
Instructions for setup and execution without Executable 

- SPIM 
- PyQt5
- (optional) Pyinstaller - to generate an executable
  ~~~
  sudo apt install spim
  pip3 install PyQt5 Pyinstaller
  ~~~
- To run the program
  ~~~
  python3 MIPS_Autograder.py
  ~~~
- to create Executable 
  ~~~
  pyinstaller MIPS_Autograder.py
  ~~~

## Usage Instructions (TODO)

Explain how to create tests for this system

```
Give an example
```
## Author

* **Ian Kaminer**  

## Copyright Information
This Project was built upon the MIPS Emulator the source code can be found here
https://sourceforge.net/p/spimsimulator/code/HEAD/tree/
