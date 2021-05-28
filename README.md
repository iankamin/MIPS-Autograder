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
* Install SPIM terminal emulator
* I dont have access to a Mac so this is all guesses based on research at the moment
1. You may be able to type ```brew install spim``` into terminal

alternative (Compile SPIM yourself)
1. download the SPIM source code [here](https://sourceforge.net/p/spimsimulator/code/HEAD/tree/)
2. go to the install location in terminal
3. type ```cd spim```
4. type ```make spim```
5. to verify type ```make test```

### Windows
- This program does not work natively on Windows.
- To use on windows you will need **_Windows Subsystem for Linux (WSL 2)_** and an **_X Server_**
1. Install WSL2 - <https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10>
2. install Ubuntu from the windows Store - <https://www.microsoft.com/store/productId/9N6SVWS3RX71>
3. Setup Ubuntu  
   - NOTE: while in ubuntu your local system is located at the directory "/mnt/c/Users/"
4. Install X Server - <https://sourceforge.net/projects/vcxsrv/>
5. Create Firewall acception for WSL - <https://skeptric.com/wsl2-xserver/>
6. Open The Ubuntu App
8. Type ``` sudo apt install spim ```
7. From this point on follow instructions for use with Linux

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
