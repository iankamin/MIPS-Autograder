.global main
#XXAAXX783908782388289038339A do not modify or duplicate this line

.data 0x10000900
    .asciiz "993893843999+03981897"         # modifiable
.data 0x10000920
    .asciiz "912419-123457897"             # modifiable


.text
main:
    lui $a0, 0x1000 
    addi $a0, $a0, 0x0900 
    jal findOperator
    add $0,$0,$0  # set a breakpoint on this line and check your results

    lui $a0, 0x1000 
    addi $a0, $a0, 0x0920 
    jal findOperator
    add $0,$0,$0  # set a breakpoint on this line and check your results

    addi $v0, $0, 10
    syscall

# modifications above this line will be ignored on autograder
#XXAAXX783908782388289038339B do not modify or duplicate this line


# your code begins here
findOperator:
    move $t0, $a0                #copy $a0 to $t0
    li $v0, -1                #set $v0 & $v1 to -1 in case operator isn't found
    li $v1, -1

findOperator_loop:
    lb $t1, ($t0)                #load character    
    beq $t1, 0x2A, checkSymbol         #branch to determine if a found symbol is the operator
    beq $t1, 0x2B, checkSymbol
    beq $t1, 0x2D, checkSymbol
    beq $t1, 0x00, findOperator_return     #branch to return if NULL is reached
    
increment:
    addi $t0, $t0, 1            #increment $t0 and continue loop
    j findOperator_loop
    
checkSymbol:
    lb $t2, -1($t0)                #load the character just before the symbol
    bgt $t2, 0x2F, findOperator_end     #$t0 points to the operator if the character's value was greater than 47
    j increment                #otherwise continue looping
    
findOperator_end:
    sub $v0, $t0, $a0            #subtract to get the byte offset into $v0
    move $v1, $t1                #copy the operator to $v1
    
findOperator_return:
    jr $ra                    #return from findOperator



.data 0x10010000  # uncomment this line 
# your data goes here