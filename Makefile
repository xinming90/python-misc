all: clean test

test:
	find __pycache__ -type f | xargs rm -f
	gcc -fPIC -shared -I/usr/include/python2.7 hellomodule.c -o hello.so
	gcc -fPIC -shared -I/usr/include/python2.7 _utilsmodule.c -o _utils.so
	gcc -fPIC -shared -I/usr/include/python2.7 _typesmodule.c -o _types.so
	py.test -sv

clean:
	rm -f *.so *.o
