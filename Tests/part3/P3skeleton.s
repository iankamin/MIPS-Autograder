.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line
# For negative values the sign must increments $a1
# i.e.   for "-1234"     $a1 = 5

.data 0x10000900
    .ascii "999"         # modifiable - must also change line 23
.data 0x10000910
    .ascii "1239"         # modifiable - must also change line 31
    
.text
main:
    lui $a0, 0x1000 
    addi $a0, $a0, 0x0900 
    addi $a1, $0, 3    # modifable - must be the number of character in the number above
    jal AsciiToDec 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    lui $a0, 0x1000 
    addi $a0, $a0, 0x0910 
    addi $a1, $0, 4    # modifable - must be the number of character in the number above
    jal AsciiToDec 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    add $0,$0,$0  # set a breakpoint on this line and check your results

    addi $v0, $0, 10
    syscall

# modifications above this line will be ignored on autograder
#XXAAXX783908782388289038339B do not modify or duplicate this line



# your code begins here




#.data 0x10010000  # uncomment this line 
# your data goes here
