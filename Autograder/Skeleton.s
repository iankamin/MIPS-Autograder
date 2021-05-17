.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line


.data 0x10000000
	.asciiz "asdf"
    

.text
main:
    
	
lui $v1, 0x1000
addi $v1, $v1, 0x0000

lui $a1, 0
addi $a1, $a1, 32


	jal 
	add $0,$0,$0

    addi $v0, $0, 10
    syscall

# modifications above this line will be ignored on autograder
# but feel free to make changes for testing purposes
#XXAAXX783908782388289038339B do not modify or duplicate this line


# your code begins here


#.data 0x10010000  # uncomment this line 
# your data goes here