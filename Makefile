all: clean test

test:
	find __pycache__ -type f | xargs rm -f
	gcc -shared -I/usr/include/python2.7 hellomodule.c -o hello.so
	py.test -sv

clean:
	rm -f *.so *.o
