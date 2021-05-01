all:
	@tar xf autograde.tar
	@cp handin.* grader/submission.s
	@python3 grader/wrapper.py


clean: 
	-rm grader/error.txt
	-rm grader/concatErrors.txt
	-rm grader/input.txt
	-rm grader/output.txt
	-rm grader/submission.s
	-rm grader/concat.s
	-rm -r MIPS_creator/grader_data

list:
	ls 

%.s:
	@make clean
	@cp Tests/$*/$*.json grader/settings.json
	@cp Tests/$*/$*.s grader/submission.s
	@python3 grader/wrapper.py True

student_%.s: 
	@make clean
	@cp Tests/$*/$*.json grader/settings.json
	@cp Tests/$*/$*.s grader/submission.s
	@python3 grader/wrapper.py

%.tar:
	-make clean
	-rm grader/settings.json
	tar -cf Generic.tar grader
	@cp Tests/$*/$*.json grader/settings.json
	-tar -cf Tests/$*/$*.tar grader
	-cp Makefile Tests/$*/Makefile




