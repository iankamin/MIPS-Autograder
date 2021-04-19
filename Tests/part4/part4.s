.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line

.text
main:
    lui $a0, 0x1000
    ori $a0, $a0, 0x0100
    jal calculator 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    lui $a0, 0x1000
    ori $a0, $a0, 0x0200
    jal calculator 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    lui $a0, 0x1000
    ori $a0, $a0, 0x0300
    jal calculator 
    add $0,$0,$0  # set a breakpoint on this line and check your results
    
    addi $v0, $0, 10
    syscall


# modifications above this line will be ignored on autograder
#XXAAXX783908782388289038339B do not modify or duplicate this line


# your code begins here

calculator:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	jal getInput
	jal findOperator
	move $s4, $v1
	move $a1, $v0
	jal AsciiToDec
	move $s3, $v0
	move $s1, $a1
	add $s0, $s1, $a0

LOOP:
	lbu $t0, 1($s0)
	beq $t0, 0xa, decide
	addi $s0, $s0, 1
	addi $s1, $s1, 1
	j LOOP

decide:
	move $t1, $a0
	add $a0, $a0, $a1
        addi $a0, $a0, 1
	sub $a1, $s1, $a1
	jal AsciiToDec
	move $s5, $v0
	move $a0, $t1
	beq $s4, 0x2a, MULTIPLY
	beq $s4, 0x2b, ADD
	beq $s4, 0x2d, SUBTRACT

MULTIPLY:
	mult $s3, $s5
	mflo $v0
	j FINAL

ADD:
	add $v0, $s3, $s5
	j FINAL

SUBTRACT:
	sub $v0, $s3, $s5
	j FINAL

FINAL:
	# optionally add output
	lw $ra, 0($sp)
	jr $ra


getInput:
        move $s0, $a0
        li $v0, 4
        la $a0, prompt
        syscall
        move $a0, $s0
        li $v0, 8
	li $a1, 14 # did not know this existed LOL! (did 14 to ensure full input)
        syscall
        li $s1, 0
        # modified by removing redundant j L1

L1:
        lbu $t0, 0($s0)
        beq $t0, 0xa, endL1
        beq $s1, 11, endL1 # changed 14 character limit to 11 to prevent overflow
        addi $s1, $s1, 1
        addi $s0, $s0, 1
        j L1

endL1:
        li $t0, 0xa
        sb $t0, 0($s0)
        sb $zero, 1($s0)
        jr $ra


findOperator:
        lbu $t0, 0($a0)
        beq $t0, 0, INVALID
        addi $s0, $a0, 1
        li $s1, 1

L2:	# had to change name of this loop from L1 to L2 to ensure that the code assembles correctly
        lbu $s2, 0($s0)
        beq $s2, 0x2a, END
        beq $s2, 0x2b, END
        beq $s2, 0x2d, END
        beq $s2, 0, INVALID
        addi $s0, $s0, 1
        addi $s1, $s1, 1
        j L2

INVALID:
        li $v0, -1
        li $v1, -1
        jr $ra

END:
        move $v0, $s1
        move $v1, $s2
        jr $ra


AsciiToDec:
        li $v0, 0
        addi $s0, $a1, -1 # $s0 is the counter
        li $s2, 1 #s2 is the multiplier for the number place

L3:	# had to change name of this loop from L1 to L3 to ensure that the code assembles correctly
        add $s1, $a0, $s0 # $s1 will contain the character at whatever place
        lbu $s1, 0($s1)
        beq $s1, 0x2d, AppendNegative
        addi $s1, $s1, -48
        mult $s1, $s2
        mflo $t0
        add $v0, $v0, $t0
        addi $s0, $s0, -1
        beq $s0, -1, end
        li $t0, 10
        mult $s2, $t0
        mflo $s2
        j L3
# in L3, I had to change END to end, and rename the other label to ensure that the code assembles correctly
AppendNegative:
        li $t0, -1
        mult $v0, $t0
        mflo $v0

end:
        jr $ra


.data 0x10010000  # uncomment this line
	 prompt: .asciiz "Please enter the expression:\n"
