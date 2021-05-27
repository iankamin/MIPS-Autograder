.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line
# For negative values the sign must increments $a1
# i.e.   for "-1234"     $a1 = 5

.data 0x10000900
    .ascii "620"         # modifiable - must also change line 23
.data 0x10000910
    .ascii "11111"         # modifiable - must also change line 31
    
.text
main:
    lui $a0, 0x1000 
    addi $a0, $a0, 0x0900 
    addi $a1, $0, 3    # modifable - must be the number of character in the number above
    jal AsciiToDec 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    lui $a0, 0x1000 
    addi $a0, $a0, 0x0910 
    addi $a1, $0, 5    # modifable - must be the number of character in the number above
    jal AsciiToDec 
    add $0,$0,$0  # set a breakpoint on this line and check your results

    add $0,$0,$0  # set a breakpoint on this line and check your results

    addi $v0, $0, 10
    syscall

# modifications above this line will be ignored on autograder
#XXAAXX783908782388289038339B do not modify or duplicate this line

# your code begins here

AsciiToDec:
    lw $s0, ($a0)               #s0 will hold the memory address of the pointer of the first character
    move $s0, $a0               

    move $s1, $a1               #s1 will hold the number of characters in the string
    lb $s2, ($s0)               #s2 will hold the first character of the string.
    
    
    move $s6, $zero
    move $s7, $zero
    #The first character of the string is represented in ASCII, which will be converted to a decimal. "1" = 49, "2" = 50, etc...
    li $t1, 48                  #This will give us the hex value of the integer. 
    li $t2, 10                  #This will help us move to the next number in the integer.
    li $t4, 10                  #This will help us get the actual integer value


    beq $s1, 5, conversion_5        #This will help us check if it's a 5-digit number or not.
    beq $s1, 4, conversion_4        #This will help us check if it's a 4-digit number or not.
    beq $s1, 3, conversion_3        #This will help us check if it's a 3-digit number or not.
    beq $s1, 2, conversion_2        #This will help us check if it's a 2-digit number or not.
    beq $s1, 1, last_dig            #This will help us check if it's a 1-digit number or not.
    beq $s1, 0, end
    #beq $s1, $t7, conversion_4
    #slt $s5, $s1, $t7
    #beq $s5, 1, conversion_3
    

conversion_5: 
    addi $t3, $t3, 1            #Increases the counter t3 by 1 everytime the loop is run.
    beq $t3, $s1, last_dig      #If the number of loops ran == length of the number, we are at the last digit.
    #mult $t4, $t0              #Multiplying by 10 because if loop ran, that means next digit needs to be evaluated. 
    lui $s5, 0x0000
    addi $s5, 0x2710
    #mult $t4, $t0
    #mflo $t6

    sub $s4, $s2, $t1
    mult $s4, $s5
    mflo $s7

    addi $s0, $s0, 1            #going to the next address in memory
    lb $s2, ($s0)               #loading the next address in memory
    j conversion_4

conversion_4: 
    addi $t3, $t3, 1            #Increases the counter t3 by 1 everytime the loop is run.
    beq $t3, $s1, last_dig      #If the number of loops ran == length of the number, we are at the last digit.
    #mult $t4, $t0              #Multiplying by 10 because if loop ran, that means next digit needs to be evaluated. 
    lui $s5, 0x0000
    addi $s5, 0x03E8
    #mult $s0, $s5

    sub $s4, $s2, $t1
    mult $s4, $s5
    mflo $s6

    add $s7, $s7, $s6

    addi $s0, $s0, 1            #going to the next address in memory
    lb $s2, ($s0)               #loading the next address in memory
    j conversion_3

conversion_3:
    addi $t3, $t3, 1
    beq $t3, $s1, last_dig      #If the number of loops ran is == length of the number then we are at the last digit.
    lui $s5, 0x0000
    addi $s5, 0x0064

    sub $s4, $s2, $t1
    mult $s4, $s5
    mflo $t4

    add $s7, $t4, $s7

    addi $s0, $s0, 1
    lb $s2, ($s0)
    j conversion_2
    
conversion_2:
    addi $t3, $t3, 1
    beq $t3, $s1, last_dig      #If the number of loops ran is == length of the number then we are at the last digit.
    lui $s5, 0x0000
    addi $s5, 0x000A

    sub $s4, $s2, $t1
    mult $s4, $s5
    mflo $t2

    add $s7, $t2, $s7
    
    addi $s0, $s0, 1
    lb $s2, ($s0)
    j last_dig

#if this is the last digit
last_dig:
    #add $s7, $t2, $s7
    sub $s4, $s2, $t1           #s4 will contain the decimal value of the ASCII character.
    add $s7, $s7, $s4           #adding the decimal value to the final number. 
    #bne $t3, $s1, conversion
  
    
end:
    move $v0, $s7
    jr $ra


.data 0x10010000 