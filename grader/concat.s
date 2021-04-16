
.data 0x10010000  
    message: .asciiz "Input a calculation up to 11 characters: "
    input: .space 11
    .align 2


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


	
	addi $v0, $0, 10
	syscall

	

 

calculator:
    
    li $a0, 0x10000300  
    lb $t0, 0($a0)      
    Empty_Address:
        
        beq $t0, $0, getInput

        
        addi $a0, $a0, 0x0100
        
        lb $t0, 0($a0)

        j Empty_Address
    
    
    getInput:
        
        move $s0, $a0
        move $s7, $a0   

        
        li $v0, 4
        la $a0, message
        syscall

        
        li $v0, 8
        
        la $a0, input
        
        li $a1, 12
        syscall

        
        lb $s1, 0($a0)
        writeInput:
            
            beq $s1, $zero, findOperator

            
            lb $s1, 0($a0)
            
            addi $a0, $a0, 1

            
            sb $s1, 0($s0)
            
            addi $s0, $s0, 1

            j writeInput
        
    findOperator:
        
        lb $s0, 0($s7)
        
        move $a0, $s7
        
        li $s1, '+'   
        li $s2, '-'   
        li $s3, '*'   

        
        bne $s0, $s2, operator_loop
            move $t6, $s0
            
            addi $a0, $a0, 1
            
            addi $s5, $0, 1
            
            lb $s0, 0($a0)

            
            beq $s0, $s1, error
            beq $s0, $s2, error
            beq $s0, $s3, error
        
        beq $s0, $s1, error
        beq $s0, $s3, error

        operator_loop:
            
            beq $s0, $zero, error

            
            lb $s0, 0($a0)

            
            bne $s0, $s1, plus_exit
                addi $s4, $zero, 0x2B   
                j endOperator
            plus_exit:

            
            bne $s0, $s2, minus_exit
                addi $s4, $zero, 0x2D   
                j endOperator
            minus_exit:

            
            bne $s0, $s3, times_exit
                addi $s4, $zero, 0x2A   
                j endOperator
            times_exit:

            
            addi $a0, $a0, 1
            
            addi $s5, $s5, 1

            j operator_loop

        endOperator:
            
            add $s5, $s5, $zero
            
            
            add $v1, $s4, $zero
            
            add $v0, $s5, $zero

            
            li $s5, 0

            
            addi $a0, $a0, 1
            
            lb $s0, 0($a0)
            
            beq $s0, $s1, error
            beq $s0, $s3, error
            beq $s0, $zero, error
            
            bne $s0, $s2, negativeNum2_Exit
                
                addi $a0, $a0, 1
                
                lb $s0, 0($a0)

                
                beq $s0, $s1, error
                beq $s0, $s2, error
                beq $s0, $s3, error
                beq $s0, $zero, error
            negativeNum2_Exit:

            
            move $a0, $s7
            
            move $a1, $v0
            
            move $a2, $v1

            j AsciiToDec

        error:
            
            li $v0, -1
            
            li $v1, -1

            
            li $s5, 0

    AsciiToDec:
        
        li $v0, 0
        
        la $t0, 0($a1)

        
        lb $s0, 0($a0)  
        li $t4, 45      
        
        bne $s0, $t4, Loop
            
            addi $a0, $a0, 1    
            addi $t0, $t0, -1   
            addi $t7, $0, -1    
            
        Loop:
            
            beq $t0, $0, Loop_Exit

            
            lb $s0, 0($a0)      
            andi $s1, $s0, 15   

            
            addi $t1, $t0, -1   
            li $t2, 1           
            Multiplier:
                
                beq $t1, $0, Multiplier_Exit

                
                li $t3, 10          
                mul $t2, $t2, $t3   

                
                addi $t1, $t1, -1

                j Multiplier
            Multiplier_Exit:

            
            mul $s2, $s1, $t2
            
            add $v0, $v0, $s2

            
            addi $a0, $a0, 1    
            addi $t0, $t0, -1   

            j Loop
        Loop_Exit:

        
        beq $t7, $0, Not_Neg
            mul $v0, $v0, $t7   
            li $t7, 0           
        Not_Neg:

        
        bne $s5, $0, Second_Num
            
            move $s5, $v0

            
            addi $a0, $a0, 1

            
            li $a1, -1          
            move $s3, $a0       
            lb $s4, 0($s3)      

            Num_Count:
                
                beq $s4, $0, AsciiToDec

                
                addi $a1, $a1, 1    
                addi $s3, $s3, 1    
                lb $s4, 0($s3)      

                j Num_Count

        
        Second_Num:
            
            bne $s6, $0, Exit

            
            move $s6, $v0

            
            li $s1, '+'   
            li $s2, '-'   
            li $s3, '*'   

            
            bne $a2, $s1, plus_exit2
                add $v0, $s5, $s6   
                j Exit
            plus_exit2:

            
            bne $a2, $s2, minus_exit2
                sub $v0, $s5, $s6   
                j Exit
            minus_exit2:

            
            bne $a2, $s3, Exit
                mul $v0, $s5, $s6   

        Exit:

        
        li $t0, 0
        li $t1, 0
        li $t2, 0
        li $t3, 0
        li $t4, 0
        li $t5, 0
        li $t6, 0
        li $t7, 0
        li $s0, 0
        li $s1, 0
        li $s2, 0
        li $s3, 0
        li $s4, 0
        li $s5, 0
        li $s6, 0
        li $s7, 0
        li $v1, 0
        li $a0, 0
        li $a1, 0
        li $a2, 0

    jr $ra

