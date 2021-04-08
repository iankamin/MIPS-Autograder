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
getInput:
    lui $a0, 0x1000 
    addi $a0, $a0, 0x0300
    move $t0, $a0
    li $v0, 4
    la $a0, str1
    syscall
    move $a0, $t0
    li $v0, 8
    li $a1, 15
    syscall
    j findOperator

findOperator:
    li $v0, -1 
    oploop:
    addi $v0, $v0, 1
    add $t0, $a0, $v0
    lb $t1,0($t0)
    beq $t1, '+',adit
    beq $t1, '*',tim 
    beq $t1, '-',opsubt
    beq $t1, 0x00, noth
    j oploop
    noth:
    addi $v0, $0, -1
    addi $v1, $0, -1
    j opend
    adit:
    li $v1, 0x2B
    j opend
    tim:
    li $v1, 0x2A
    j opend
    opsubt:
    beq $v0, $0, oploop
    li $v1, 0x2D
    opend:
    j return1

AsciiToDec:
    li $t0, 0 #length counter
    li $v0, 0
    li $t2, 1 #neg flag
    decloop:
    beq $t0, $a1, decend
    add $t1, $a0, $t0
    lb $t1,0($t1)
    bne $t0, 0, pos
    beq $t1, '-',decsubt
    pos:
    mul $v0, $v0, 10
    addi $t1, $t1, -48
    add $v0, $v0, $t1
    addi $t0, $t0, 1
    j decloop
    decsubt:
    li $t2 , -1
    addi $t0, $t0, 1
    j decloop
    decend:
    mul $v0, $v0, $t2
    bne $t4, $0, return3
    j return2

calculator:
    j getInput
    return1:
    beq $v0, -1, end
    add $a1, $v0, $0
    li $t4, 0
    j AsciiToDec
    return2:
    move $t3, $v0
    add $a0, $a0, $a1
    addi $a0, $a0, 2
    li $a1, -1
    loop:
    addi $a1, $a1, 1 
    add $t0, $a0, $a1
    lb $t1,0($t0)
    bne $t1, 0x00, loop
    addi $a0,$a0,-1
    li $t4, 1
    j AsciiToDec
    return3:
    beq $v1, 0x2B, adii
    beq $v1, 0x2A, timii
    beq $v1, 0x2D, minii
    j end
    adii:
    add $v0,$v0,$t3
    j end
    timii:
    mult $v0,$t3
    mflo $v0
    j end
    minii:
    sub $v0,$t3,$v0
    j end
    end:
    li $v1, 0
    jr $ra

.data 0x10010000  # uncomment this line 
# your data goes here
str1: .asciiz "Enter String:\n"