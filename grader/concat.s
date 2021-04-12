
.data 0x10010000  

    userInput: .space 14
    userInput2: .space 14
     userInput3: .space 14
    prompt: .asciiz "ENTER A STRING: "
     message: .asciiz "\nYour string: "
    


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
	jal zzzdivider
	add $0, $0, $0

	
lui $a0, 0x1000
addi $a0, $a0, 0x0300


	jal getInput
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $a0, 0x1000
addi $a0, $a0, 0x0300
addi $v0, $0, 4
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
	jal zzzdivider
	add $0, $0, $0

	
lui $a0, 0x1000
addi $a0, $a0, 0x0300


	jal getInput
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $a0, 0x1000
addi $a0, $a0, 0x0300
addi $v0, $0, 4
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
	jal zzzdivider
	add $0, $0, $0

	
lui $a0, 0x1000
addi $a0, $a0, 0x0330


	jal getInput
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $a0, 0x1000
addi $a0, $a0, 0x0330
addi $v0, $0, 4
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================



# ================================================================
	jal zzzdivider
	add $0, $0, $0

	
lui $a0, 0x1000
addi $a0, $a0, 0x0350


	jal getInput
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	
sw $a0, 0($sp)
sw $v0, 4($sp)

lui $a0, 0x1000
addi $a0, $a0, 0x0350
addi $v0, $0, 4
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)



	jal zzzdivider
	add $0, $0, $0

# ================================================================


	
	addi $v0, $0, 10
	syscall

	

 



getInput:
    
    move $t0 $a0 
    	        

    
    li $v0, 4
    la $a0, prompt
    syscall
    
    
    li $v0, 8
    la $a0, userInput
    li $a1, 14
       sw $t1, 0($a0) 
    syscall    
    
    
      li $v0 4
    la $a0, message
    syscall
    
      
    li $v0, 4
    la $a0, userInput 
    syscall
    
      lui $t2, 0x1000
      addi $t2, 0x0300
 
      lui $t3, 0x1000
      addi $t3, 0x0400    

      lui $t4, 0x1000
      addi $t4, 0x0500

      lui $t7 0x1001 
      	
      beq $t0, $t2, STRING1    
      beq $t0, $t3, STRING2
      beq $t0, $t4, STRING3
          
      STRING1:
    
	lw $t1, 0($t7) 
        sw $t1, 0x10000300
	
	addi $t7, $t7, 4 
        lw $t1, 0($t7)
	sw $t1, 0x10000304
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x10000308      
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x1000030c
    j FIN 

     STRING2:
    
       	lw $t1, 0($t7) 
        sw $t1, 0x10000400
	addi $t7, $t7, 4 
        lw $t1, 0($t7)
	sw $t1, 0x10000404
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x10000408      
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x1000040c

    j FIN

     STRING3:
    
        
	lw $t1, 0($t7) 
        sw $t1, 0x10000500
	addi $t7, $t7, 4 
        lw $t1, 0($t7)
	sw $t1, 0x10000504
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x10000508      
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x1000050c
    
    FIN:    
    
	sw $t0 ($t7) 
	
	addi $t7 $t7 -4
	sw $t0 ($t7)  
	
	addi $t7 $t7 -4
	sw $t0 ($t7)  
	
	addi $t7 $t7 -4
	sw $t0 ($t7) 	

jr $ra


