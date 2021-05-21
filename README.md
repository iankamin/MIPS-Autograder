# MIPS Autograder

This program will generate an autograder for a mips subroution. You provide the input registers, initial data section, Any User Input, and the expected output registers and the correct answer.

All tests will be run on one emulator instance meaning that if one test fails all following tests may also fail. 

For instance if the given subroutine does not initialize registers then there code will pass the first test but will fail all following tests.


## **Installation**

### Mac
* Install SPIM terminal emulator
* Currently there is no executable for mac so please go to the build section for more details.

### Windows
* This program does not work natively on Windows.
* To use on windows you will need **_WSL 2_** and **_XLaunch_**
* TODO: provide links

### Linux
* To use this program you will need the terminal based spim emulator. 
* ``` sudo apt install spim ```

### Build Instructions
If you would like to make modifications to the autograder then the folowing programs are needed
* SPIM - ```sudo apt install spim```
* PyQt5 - to run the user interface ( provided with virtualEnv )
* VirtualEnv
* (optional) Pyinstaller - to generate an executable


## Deployment
To use this program the subroutine must be written using a Skeleton Code
To create Executable
```pyinstaller MIPS_Autograder.spec```

To run executable
1. download the release file
2. Type ```./MIPS_Autograder.linux```

To run python code
1. Go to the project root
2. type ```python3 GUI_wrapper.py```

To run Terminal version (TODO)


## Usage Instructions (TODO)

Explain how to create tests for this system

```
Give an example
```

## Author

* **Ian Kaminer** 
