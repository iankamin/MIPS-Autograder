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
calculator:
    addi $sp, $sp -24
    sw $ra, 20($sp)
    sw $s0, 16($sp)
    sw $s1, 12($sp)
    sw $s2, 8($sp)
    sw $s3, 4($sp)
    sw $s4, 0($sp)
    la $s0, input # $s0 = address of first char in string
    move $a0, $s0
    jal getInput 
    jal findOperator    
    move $s1, $v0 # $s1 = byte offset of operator char
    move $s2, $v1 # $s2 = operation ascii char

    move $a0, $s0 # $a0 = pointer to first char in string
    move $a1, $s1 # $a1 = number of chars in string
    jal AsciiToDec
    move $s3, $v0 # $s3 = first operand

    add $a0, $a0, $s1
    addi $a0, $a0, 1 # $a0 = pointer to first char in string 
    li $a1, 6 # $a1 = number of chars in string
    jal AsciiToDec
    move $s4, $v0 # $s4 = second operand

    li $t0, 0x2B
    beq $s2, $t0, calcAddition
    li $t0, 0x2D
    beq $s2, $t0, calcSubtraction
    li $t0, 0x2A
    beq $s2, $t0, calcMultiplication

    calcAddition: add $v0, $s3, $s4
    j calcEnd
    calcSubtraction: sub $v0, $s3, $s4
    j calcEnd
    calcMultiplication: mult $s3, $s4
    mflo $v0
    j calcEnd

    calcEnd: 
    lw $ra, 20($sp)
    lw $s0, 16($sp)
    lw $s1, 12($sp)
    lw $s2, 8($sp)
    lw $s3, 4($sp)
    lw $s4, 0($sp)
    addi $sp, $sp, 24
    j $ra

getInput:
    addi $sp, $sp, -4
    sw $a0, 0($sp)
    li $v0, 4
    la $a0, askinput
    syscall
    lw $a0, 0($sp)
    addi $sp, $sp, 4
    li $v0, 8
    li $a1, 13
    syscall
    j $ra

findOperator:
    addi $sp, $sp, -4
    sw $s0, 0($sp)
    li $s0, 0
    add $t0, $a0, $s0
    lb $t1, 0($t0)

    #first, find the first operand (ascii numbers range 48 - 57 decimal)
    findL1:beq $t1, $zero, NA
    li $t2, 48
    blt $t1, $t2, findL1Incre
    li $t2, 57
    bgt $t1, $t2, findL1Incre
    # number found
    addi $s0, $s0, 1
    add $t0, $a0, $s0
    lb $t1, 0($t0)
    j findL2

    findL1Incre: addi $s0, $s0, 1
    add $t0, $a0, $s0
    lb $t1, 0($t0)
    j findL1 
    

    findL2: beq $t1, $zero, NA
    li $t2, 0x2B
    beq $t1, $t2, Addition
    li $t2, 0x2D
    beq $t1, $t2, Subtraction
    li $t2, 0x2A
    beq $t1, $t2, Multiplication

    addi $s0, $s0, 1
    add $t0, $a0, $s0
    lb $t1, 0($t0)
    j findL2

    Addition: move $v0, $s0
    li $v1, 0x2B
    j findEnd

    Subtraction: move $v0, $s0
    li $v1, 0x2D
    j findEnd

    Multiplication: move $v0, $s0
    li $v1, 0x2A
    j findEnd

    NA: li $v0, -1
    li $v1, -1
    j findEnd

    findEnd: lw $s0, 0($sp)
    addi $sp, $sp, 4
    j $ra

AsciiToDec:
    addi $sp, $sp, -8
    sw $s0, 4($sp)
    sw $s1, 0($sp)
    #sw $s2, 0($sp)
    li $s0, 0 # offset
    li $s1, 0 # if negative
    #li $s2, 0 # 
    lb $t1, 0($a0)
    li $v0, 0
    # first, find number(ascii numbers range 48 - 57 decimal)
    # check if negative and save.

    asciiL1:beq $s0, $a1 asciiEnd
    li $t2, 45
    beq $t1, $t2, Negative
    li $t2, 48
    blt $t1, $t2, asciiEnd
    li $t2, 57
    bgt $t1, $t2, asciiEnd
    # number found, subtract by 48 to find decimal
    # if not zero number,multiply previous number by 10 and add digit number
    addi $t1, $t1, -48
    bne $v0, $0, NotZero
    add $v0, $v0, $t1
    j asciiL1Incre
    NotZero:
    mul $v0, $v0, 10
    add $v0, $v0, $t1
    j asciiL1Incre
    
    Negative: addi $s1, $s1, 1

    asciiL1Incre: addi $s0, $s0, 1
    add $t0, $a0, $s0
    lb $t1, 0($t0)
    j asciiL1 

    asciiEnd: beq $s1, $0, Positive
    nor $v0, $v0, $v0
    addi $v0, $v0, 1
    Positive: lw $s1, 0($sp)
    lw $s0, 4($sp)
    addi $sp, $sp, 8
    j $ra

.data 0x10010000  # uncomment this line 
# your data goes here
askinput: .asciiz "Input string up to 11 chars:\n"
.align 2
input: .space 11