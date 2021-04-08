.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line

.text
main:
    jal calculator 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    jal calculator 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    jal calculator 
    add $0,$0,$0  # set a breakpoint on this line and check your results
    
    addi $v0, $0, 10
    syscall


# modifications above this line will be ignored on autograder
#XXAAXX783908782388289038339B do not modify or duplicate this line


# your code begins here


#.data 0x10010000  # uncomment this line 
# your data goes here
