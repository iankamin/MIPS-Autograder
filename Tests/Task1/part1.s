.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line

.text
main:
    lui $a0, 0x1000 
    addi $a0, $a0, 0x0300 # this line is modifiable
    jal getInput
    #add $0,$0,$0  # set a breakpoint on this line and check your results
    

    lui $a0, 0x1000 
    addi $a0, $a0, 0x0400 # this line is modifiable
    jal getInput
    #add $0,$0,$0  # set a breakpoint on this line and check your results
    #BREAK2: 

    lui $a0, 0x1000 
    addi $a0, $a0, 0x0500 # this line is modifiable
    jal getInput
    #add $0,$0,$0  # set a breakpoint on this line and check your results
    #BREAK3: 
     
    addi $v0, $0, 10
    syscall

# modifications above this line will be ignored on autograder
#XXAAXX783908782388289038339B do not modify or duplicate this line

#your code begins here

getInput:
    #Store address where userInput needs to go
    move $t0 $a0 
    	        

    #Prompt user to type a string
    li $v0, 4
    la $a0, prompt
    syscall
    
    #Get the userInput
    li $v0, 8
    la $a0, userInput
    li $a1, 14
       sw $t1, 0($a0) #Save userInput to $t1 
    syscall    
    
    #display Message
      li $v0 4
    la $a0, message
    syscall
    
      #display userInput 
    li $v0, 4
    la $a0, userInput 
    syscall
    
      lui $t2, 0x1000
      addi $t2, 0x0300
 
      lui $t3, 0x1000
      addi $t3, 0x0400    

      lui $t4, 0x1000
      addi $t4, 0x0500

      lui $t7 0x1001 #stores upper bits of .data 
      	
      beq $t0, $t2, STRING1    
      beq $t0, $t3, STRING2
      beq $t0, $t4, STRING3
          
      STRING1:
    #save string($t1) to 0x10000300 
	lw $t1, 0($t7) 
        sw $t1, 0x10000300
	#trying to save the word and not just the pointer in memory to data
	addi $t7, $t7, 4 #testline
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
    #save string($t1) to 0x10000400 
       	lw $t1, 0($t7) 
        sw $t1, 0x10000400
	addi $t7, $t7, 4 #testline
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
    #save string($t1) to 0x10000500 
        
	lw $t1, 0($t7) 
        sw $t1, 0x10000500
	addi $t7, $t7, 4 #testline
        lw $t1, 0($t7)
	sw $t1, 0x10000504
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x10000508      
	addi $t7, $t7, 4
	lw $t1, 0($t7)
	sw $t1, 0x1000050c
    
    FIN:    
    #clear $t7 for next read
	sw $t0 ($t7) 
	
	addi $t7 $t7 -4
	sw $t0 ($t7)  
	
	addi $t7 $t7 -4
	sw $t0 ($t7)  
	
	addi $t7 $t7 -4
	sw $t0 ($t7) 	

jr $ra


.data 0x10010000  # uncomment this line 
# your data goes here
    userInput: .space 14
    userInput2: .space 14
     userInput3: .space 14
    prompt: .asciiz "ENTER A STRING: "
     message: .asciiz "\nYour string: "
    