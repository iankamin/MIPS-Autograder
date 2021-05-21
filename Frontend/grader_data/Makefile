# This File is intended for use with AutoLabs
# however this file will autograde any .s file 
# kept in the same directory as this and the tar file

all:
	@tar xf autograde.tar
	@cp handin.* Autograder/submission.s
	@python3 Autograder/wrapper.py


clean: 
	-rm Autograder/error.txt
	-rm Autograder/concatErrors.txt
	-rm Autograder/input.txt
	-rm Autograder/output.txt
	-rm Autograder/submission.s
	-rm Autograder/concat.s







