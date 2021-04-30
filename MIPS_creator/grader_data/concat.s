
.data  

askinput: .asciiz "Input string up to 11 chars:\n"
.align 2
input: .space 11


.kdata 0x90000220
	.asciiz "XXFFVV3793"
.kdata 0x90000230
	.asciiz "\n"

	



.text
zzzneaten:
	sw $a0, 0($sp)
	sw $v0, 4($sp)
	sw $ra, 8($sp)
	addi $sp, $sp, -12

	lui $a0, 0x9000		# prints new line stuff for neatness
	addi $a0,$a0,0x0230
	addi $v0, $0, 4		#syscall string print 
	syscall
	
	addi $sp, $sp, 12
	lw $a0, 0($sp)
	lw $v0, 4($sp)
	lw $ra, 8($sp)

	jr $ra
	add $0,$0,$0

zzzdivider:
	sw $a0, 0($sp)
	sw $v0, 4($sp)
	sw $ra, 8($sp)
	addi $sp, $sp, -12

	jal zzzneaten

	lui $a0, 0x9000		# prints new line stuff for neatness
	addi $a0,$a0,0x0220
	addi $v0, $0, 4		#syscall string print 
	syscall

	jal zzzneaten

	addi $sp, $sp, 12
	lw $a0, 0($sp)
	lw $v0, 4($sp)
	lw $ra, 8($sp)

	jr $ra
	add $0,$0,$0
	
main:
	

# ================================================================
# Test    14

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    15

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    16

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    17

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    18

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    19

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    20

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    21

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    22

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    23

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    24

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    0

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    1

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    2

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    3

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    4

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    5

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    6

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    7

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    8

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    9

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    10

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    11

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    12

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
# Test    13

	jal zzzdivider
	add $0, $0, $0

	

	jal calculator
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $0, 0
addi $a0, $v0, 0
addi $v0, $0, 1
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================


	
	addi $v0, $0, 10
	syscall

	

 



calculator:
    addi $sp, $sp -24
    sw $ra, 20($sp)
    sw $s0, 16($sp)
    sw $s1, 12($sp)
    sw $s2, 8($sp)
    sw $s3, 4($sp)
    sw $s4, 0($sp)
    la $s0, input 
    move $a0, $s0
    jal getInput 
    jal findOperator    
    move $s1, $v0 
    move $s2, $v1 

    move $a0, $s0 
    move $a1, $s1 
    jal AsciiToDec
    move $s3, $v0 

    add $a0, $a0, $s1
    addi $a0, $a0, 1 
    li $a1, 6 
    jal AsciiToDec
    move $s4, $v0 

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

    
    findL1:beq $t1, $zero, NA
    li $t2, 48
    blt $t1, $t2, findL1Incre
    li $t2, 57
    bgt $t1, $t2, findL1Incre
    
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
    
    li $s0, 0 
    li $s1, 0 
    
    lb $t1, 0($a0)
    li $v0, 0
    
    

    asciiL1:beq $s0, $a1 asciiEnd
    li $t2, 45
    beq $t1, $t2, Negative
    li $t2, 48
    blt $t1, $t2, asciiEnd
    li $t2, 57
    bgt $t1, $t2, asciiEnd
    
    
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

