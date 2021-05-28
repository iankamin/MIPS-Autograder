.globl main


#XXAAXX783908782388289038339A do not modify or duplicate this line

.data 0x10000000
    .asciiz "5436"
.text
main:
    
        
    lui $a0, 0x1000
    addi $a0, $a0, 0x0000    
    lui $a1, 0
    addi $a1, $a1, 4

    jal AsciiToDec
    add $0,$0,$0

    addi $v0, $0, 10
    syscall

#XXAAXX783908782388289038339B do not modify or duplicate this line
# modifications above this line will be ignored on autograder
# but feel free to make changes for your own testing purposes


# your code begins here



#.data 0x10010000  # uncomment this line 
# your data goes here
