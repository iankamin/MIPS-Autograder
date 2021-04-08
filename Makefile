all:
	@tar xf autograde.tar
	@cp handin.* grader/submission.s
	@python3 grader/wrapper.py


tar: 
	-rm grader/error.txt
	-rm grader/concatErrors.txt
	-rm grader/input.txt
	-rm grader/output.txt
	-rm grader/submission.s
	-rm grader/concat.s
	tar -cf Generic.tar grader


build_%.s: 
	@cp $*.json grader/settings.json
	@cp handins/$*.s grader/submission.s
	@python3 grader/wrapper.py True

student_%.s: 
	@cp $*.json grader/settings.json
	@cp handins/$*.s grader/submission.s
	@python3 grader/wrapper.py

%.json: FORCE
	-make tar
	-tar xf Generic.tar
	@cp $*.json grader/settings.json
	-tar -cf TARs/$*.tar grader
	-cp Makefile TARs/Makefile

FORCE:



