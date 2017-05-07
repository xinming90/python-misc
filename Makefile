all: clean test


test:
	find __pycache__ -type f | xargs rm -f
	gcc -g -fPIC -shared hellomodule.c -o hello.so
	gcc -g -fPIC -shared _utilsmodule.c -o _utils.so
	gcc -g -fPIC -shared _typesmodule.c -o _types.so
	py.test -sv


clean:
	rm -f *.so *.o
