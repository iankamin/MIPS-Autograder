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

UI_clean:
	-rm Frontend/grader_data/*.s
	-rm Frontend/grader_data/*.txt
	-rm Frontend/grader_data/*.json


list:
	ls 

%.s:
	@make clean
	@cp Tests/$*/$*.json Autograder/settings.json
	@cp Tests/$*/$*.s Autograder/submission.s
	@python3 Autograder/wrapper.py True

student_%.s: 
	@make clean
	@cp Tests/$*/$*.json Autograder/settings.json
	@cp Tests/$*/$*.s Autograder/submission.s
	@python3 Autograder/wrapper.py

%.tar:
	-make clean
	-rm Autograder/settings.json
	tar -cf Generic.tar Autograder
	@cp Tests/$*/$*.json Autograder/settings.json
	-tar -cf Tests/$*/$*.tar Autograder
	-cp Makefile Tests/$*/Makefile

UI_tar:
	-make clean
	-make UI_clean
	@tar -cf Frontend/grader_data/UI.tar Autograder
	






