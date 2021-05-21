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
* SPIM
* PyQt5
* VirtualEnv
* (optional) Pyinstaller



## Deployment
To use this program the subroutine must be written using a Skeleton Code

To run executable
1. Go to the project root
2. Type ```./GUI_Wrapper```


To run with User Interface 
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