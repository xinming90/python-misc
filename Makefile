all: clean test

build:
	pip install pytest-raisesregexp

test:
	find __pycache__ -type f | xargs rm -f
	gcc -g -fPIC -shared -I/usr/include/python2.7 hellomodule.c -o hello.so
	gcc -g -fPIC -shared -I/usr/include/python2.7 _utilsmodule.c -o _utils.so
	gcc -g -fPIC -shared -I/usr/include/python2.7 _typesmodule.c -o _types.so
	py.test -sv

clean:
	rm -f *.so *.o
