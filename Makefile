all:

install:
	python setup.py install
	rm -rf build

uninstall:
	python setup.py uninstall

clean:
	rm -rf build
	find -name "*.pyc" -o -name "*~" -print0 | xargs -0 rm -f

doc:
	make -C doc singlehtml

check:
	python setup.py check

	cd src && PYTHONPATH=src pylint \
		--reports=no \
		--include-ids=yes \
		--disable=R0201 \
		*/*.py

#	cd test && PYTHONPATH=../src ./run_tests.py
