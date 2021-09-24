.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line

.text
main:
    
    

    jal HexOut
    add $0,$0,$0
    add $0,$0,$0  # set a breakpoint here to check your results

    addi $v0, $0, 10
    syscall

#XXAAXX783908782388289038339B do not modify or duplicate this line
# modifications above this line will be ignored on autograder
# but feel free to make changes for your own testing purposes
HexOut:
    addi $v0, $0, -18
    jr $ra
    add $0, $0, $0
    add $0, $0, $0
    add $0, $0, $0

# your code begins here

#.data 0x10000000  # uncomment this line 
# your data goes here

