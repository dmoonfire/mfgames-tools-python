all:

install:
	python setup.py install
	rm -rf build

uninstall:
	python setup.py uninstall

clean:
	rm -rf build
	find -name "*.pyc" -o -name "*~" -print0 | xargs -0 rm -f

docs:
	cd doc && sphinx-apidoc -f -o source ../src
	rm -f doc/source/modules.rst
	make -C doc html

check:
	python setup.py check

	cd src && PYTHONPATH=src pylint \
		--reports=no \
		--include-ids=yes \
		--disable=R0201 \
		*/*.py

#	cd test && PYTHONPATH=../src ./run_tests.py
