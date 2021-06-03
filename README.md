# MIPS Autograder

This program will generate assembly code for a MIPS subroutine. You provide the input registers, initial data section, any User Input, and the output registers and their corresponding expected answers.

NOTE: All tests will be run on one emulator instance meaning that if one test fails all following tests may also fail. 

This Program was intended for use by teachers and was designed to be used with [Autolabs](https://autolabproject.com).

## Table of Contents
- [MIPS Autograder](#mips-autograder)
  - [Table of Contents](#table-of-contents)
  - [**Installation**](#installation)
    - [Mac](#mac)
    - [Windows](#windows)
    - [Linux](#linux)
    - [Build Instructions](#build-instructions)
  - [Deployment](#deployment)
  - [Usage Instructions (TODO)](#usage-instructions-todo)
  - [Author](#author)

However this program can be used as a testbench for MIPS code as well.

## **Installation**

### Mac
* currently the compiled program fails to run on Mac. To use this must be run on Mac

### Windows
Donwload The latest release and your good to go.

### Linux
- To use this program you will need the terminal based spim emulator. 
1. Type ``` sudo apt install spim ```

### Build Instructions
If you would like to make modifications to the autograder then the folowing programs are needed
- SPIM - ```sudo apt install spim```
- PyQt5 - to run the user interface ( provided with virtualEnv )
- VirtualEnv
- (optional) Pyinstaller - to generate an executable


## Deployment
With Executable 
1. Download executable [here](https://github.com/iankamin/MIPS-Autograder/releases)
2. Go to the install location in terminal
3. Type ```./MIPS_Autograder.linux```

From Python files
1. The Required python modules are
   - VirtualEnv
   - PyQt5 (included with ```./venv/bin/activate```)
2. Clone the project
3. Go to the project root folder in terminal
4. Type ```python3 MIPS_Autograder.py```

To Create Executable
1. Clone the project

2. Go to the project root folder in terminal
3. install pyinstaller
   - ```pip install pyinstaller```
4. run pyinstaller
   - ```pyinstaller MIPS_Autograder.spec```


## Usage Instructions (TODO)

Explain how to create tests for this system

```
Give an example
```

## Author

* **Ian Kaminer**  
