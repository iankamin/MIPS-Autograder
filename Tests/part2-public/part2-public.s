.globl main
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
    addi $t1, $zero, 0
    Loop:
        lb $t0, 0($a0)
        beq $t0, 0x2B, Addition
        beq $t0, 0x2D, Subtraction
        beq $t0, 0x2A, Multiplication
        beq $t0, $zero, Terminate
        addiu $a0, $a0, 1
        addiu $t1, $t1, 1
        j Loop
    Addition:
        move $v0, $t1
        add $v1, $zero, $t0
        jr $ra
    Subtraction:
        move $v0, $t1
        add $v1, $zero, $t0
        jr $ra
    Multiplication:
        move $v0, $t1
        add $v1, $zero, $t0
        jr $ra
    Terminate:
        addi $v0, $zero, -1
        addi $t2, $zero, -1
        sb $v1, 0($t2)
        jr $ra


.data 0x10010000  # uncomment this line 
# your data goes here