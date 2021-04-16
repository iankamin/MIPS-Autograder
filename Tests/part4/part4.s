.globl main
#XXAAXX783908782388289038339A do not modify or duplicate this line

.text
main:
        li $t0, 5
        li $t1, 5
        li $t2, 5
        li $t3, 5
        li $t4, 5
        li $t5, 5
        li $t6, 5
        li $t7, 5
        li $s0, 5
        li $s1, 5
        li $s2, 5
        li $s3, 5
        li $s4, 5
        li $s5, 5
        li $s6, 5
        li $s7, 5
        li $v1, 5
        li $a0, 5
        li $a1, 5
        li $a2, 5
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

calculator:
    # set address of input
    li $a0, 0x10000300  # set base address
    lb $t0, 0($a0)      # byte check
    Empty_Address:
        # if address empty
        beq $t0, $0, getInput

        # add address
        addi $a0, $a0, 0x0100
        # get new byte
        lb $t0, 0($a0)

        j Empty_Address
    
    # get user input
    getInput:
        # move $a0 address into $s0
        move $s0, $a0
        move $s7, $a0   # temporary

        # "Input a string up to 14 characters: "
        li $v0, 4
        la $a0, message
        syscall

        # going to do a string input
        li $v0, 8
        # store input's address (0x10010000) into $a0
        la $a0, input
        # input's maximum length into $a1
        li $a1, 12
        syscall

        # store input into address - loop
        lb $s1, 0($a0)
        writeInput:
            # repeat load/store bytes until end of string
            beq $s1, $zero, findOperator

            # load input byte (character) into $s1
            lb $s1, 0($a0)
            # shift input byte by 1
            addi $a0, $a0, 1

            # store loaded character into memory
            sb $s1, 0($s0)
            # shift stack by 1
            addi $s0, $s0, 1

            j writeInput
        
    findOperator:
        # instantiate first character into $s0
        lb $s0, 0($s7)
        # reset a0 address
        move $a0, $s7
        # instantiate +,-,* into $s1,$s2,$s3
        li $s1, '+'   # 43
        li $s2, '-'   # 45
        li $s3, '*'   # 42

        # if negative number
        bne $s0, $s2, operator_loop
            move $t6, $s0
            # shift $a0 character byte
            addi $a0, $a0, 1
            # add offset 1
            addi $s5, $0, 1
            # load new byte
            lb $s0, 0($a0)

            # if current byte is an operator, return -1
            beq $s0, $s1, error
            beq $s0, $s2, error
            beq $s0, $s3, error
        # if + or * throw error
        beq $s0, $s1, error
        beq $s0, $s3, error

        operator_loop:
            # if end of string (no operator), $v0 $v1 = -1
            beq $s0, $zero, error

            # load new byte
            lb $s0, 0($a0)

            # if $s0==(+), $s4=0x2B(43)
            bne $s0, $s1, plus_exit
                addi $s4, $zero, 0x2B   # put 43(+) into $s4
                j endOperator
            plus_exit:

            # if $s0==(-), $s4=0x2D(45)
            bne $s0, $s2, minus_exit
                addi $s4, $zero, 0x2D   # put 45(-) into $s4
                j endOperator
            minus_exit:

            # if $s0==(*), $s4=0x2A(42)
            bne $s0, $s3, times_exit
                addi $s4, $zero, 0x2A   # put 42(*) into $s4
                j endOperator
            times_exit:

            # shift $a0 character byte
            addi $a0, $a0, 1
            # add offset $s5 + 1
            addi $s5, $s5, 1

            j operator_loop

        endOperator:
            # put offset into $s5
            add $s5, $s5, $zero
            
            # operation in $v1
            add $v1, $s4, $zero
            # offset in $v0
            add $v0, $s5, $zero

            # reset offset $s5
            li $s5, 0

            # shift $a0 character byte
            addi $a0, $a0, 1
            # load byte
            lb $s0, 0($a0)
            # if second "number" actually isn't, return -1
            beq $s0, $s1, error
            beq $s0, $s3, error
            beq $s0, $zero, error
            # if second number is negative
            bne $s0, $s2, negativeNum2_Exit
                # shift $a0 character byte
                addi $a0, $a0, 1
                # load new byte
                lb $s0, 0($a0)

                # if current byte is an operator or \0, return -1
                beq $s0, $s1, error
                beq $s0, $s2, error
                beq $s0, $s3, error
                beq $s0, $zero, error
            negativeNum2_Exit:

            # address to $a0
            move $a0, $s7
            # amt of chars in $a1
            move $a1, $v0
            # operator in $a2
            move $a2, $v1

            j AsciiToDec

        error:
            # put -1 into $v0
            li $v0, -1
            # put -1 into $v1
            li $v1, -1

            # reset offset $s5
            li $s5, 0

    AsciiToDec:
        # final product
        li $v0, 0
        # instantiate main count
        la $t0, 0($a1)

        # check if negative
        lb $s0, 0($a0)  # $s0 - load string
        li $t4, 45      # t4 - 45 (ascii for -)
        # if not neg, skip to Loop
        bne $s0, $t4, Loop
            # update variables
            addi $a0, $a0, 1    # $a0 - shift ascii array
            addi $t0, $t0, -1   # $t0 - subtract count
            addi $t7, $0, -1    # $t7 - -1 if neg; 0 if pos
            
        Loop:
            # loop until main count is 0 (end of array)
            beq $t0, $0, Loop_Exit

            # instantiate character
            lb $s0, 0($a0)      # $s0 - load string
            andi $s1, $s0, 15   # $s1 - ascii to dec

            # multiplier (10, 100, 1000...)
            addi $t1, $t0, -1   # t1 - multiplier count
            li $t2, 1           # t2 - multiplier
            Multiplier:
                # loop until multiplier count is 0
                beq $t1, $0, Multiplier_Exit

                # mutiply by 10
                li $t3, 10          # t3 - 10
                mul $t2, $t2, $t3   # t2 - multiply self by 10

                # update multiplier count
                addi $t1, $t1, -1

                j Multiplier
            Multiplier_Exit:

            # dec * multiplier
            mul $s2, $s1, $t2
            # add to final product
            add $v0, $v0, $s2

            # update variables
            addi $a0, $a0, 1    # $a0 - shift ascii array
            addi $t0, $t0, -1   # $t0 - subtract count

            j Loop
        Loop_Exit:

        # check if negative
        beq $t7, $0, Not_Neg
            mul $v0, $v0, $t7   # negate result
            li $t7, 0           # reset $t7 to 0
        Not_Neg:

        # $s5 is empty
        bne $s5, $0, Second_Num
            # $s5 - store 1st num
            move $s5, $v0

            # shift $a0 addres to char
            addi $a0, $a0, 1

            # instantiate loop variables
            li $a1, -1          # a1 - 2nd num count
            move $s3, $a0       # s3 - address pointer
            lb $s4, 0($s3)      # s4 - new byte

            Num_Count:
                # if end of number
                beq $s4, $0, AsciiToDec

                # update variables
                addi $a1, $a1, 1    # a1 - 2nd num count
                addi $s3, $s3, 1    # s3 - address pointer
                lb $s4, 0($s3)      # s4 - new byte

                j Num_Count

        # otherwise, store second number into $s6
        Second_Num:
            # make sure second number not already stored
            bne $s6, $0, Exit

            # $s6 - store 2nd num
            move $s6, $v0

            # instantiate +,-,* into $s1,$s2,$s3
            li $s1, '+'   # 43
            li $s2, '-'   # 45
            li $s3, '*'   # 42

            # add
            bne $a2, $s1, plus_exit2
                add $v0, $s5, $s6   # v0 = s5 + s6
                j Exit
            plus_exit2:

            # subtract
            bne $a2, $s2, minus_exit2
                sub $v0, $s5, $s6   # v0 = s5 - s6
                j Exit
            minus_exit2:

            # multiply
            bne $a2, $s3, Exit
                mul $v0, $s5, $s6   # v0 = s5 * s6

        Exit:

        # reset registers
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

.data 0x10010000  # uncomment this line 
    message: .asciiz "Input a calculation up to 11 characters: "
    input: .space 11
    .align 2