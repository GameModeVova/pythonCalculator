# Makefile for FIT VUT IVS project

.PHONY: all
.PHONY: pack 
.PHONY: clean 
.PHONY: test
.PHONY: doc 
.PHONY: run 
.PHONY: profile
all: stddev.py test_calc.py math_lib.py calc.py

pack: 
	mkdir -p ../../xbalaz18_xazaro00_xvasik05_xospal01
	mkdir -p ../../xbalaz18_xazaro00_xvasik05_xospal01/doc
	mkdir -p ../../xbalaz18_xazaro00_xvasik05_xospal01/install
	mkdir -p ../../xbalaz18_xazaro00_xvasik05_xospal01/repo
#TODO: add user documentation copy
	cp ../dokumentace.pdf ../../xbalaz18_xazaro00_xvasik05_xospal01/doc
#TODO: copy installators to install 
	# some code that copies installators
	cp -rT ../../pythonCalculator ../../xbalaz18_xazaro00_xvasik05_xospal01/repo
	mv ../../xbalaz18_xazaro00_xvasik05_xospal01 ../.
	zip -r ../xbalaz18_xazaro00_xvasik05_xospal01.zip ../xbalaz18_xazaro00_xvasik05_xospal01
	rm -r ../xbalaz18_xazaro00_xvasik05_xospal01
run: calc.py
	python calc.py
profile: stddev.py
clean:
	rm -r -f ../xbalaz18_xazaro00_xvasik05_xospal01.zip
	rm -r -f html
	rm -r -f latex

test: test_calc.py
	python test_calc.py
doc: 
	doxygen
	cd latex/ && make
	cd latex/ && mv refman.pdf ../../dokumentace.pdf

# End of Makefile