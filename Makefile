all: clean test


test:
	find __pycache__ -type f | xargs rm -f
	gcc -g -fPIC -shared -I/opt/python/3.6/include/python3.6m hellomodule.c -o hello.so
	gcc -g -fPIC -shared -I/opt/python/3.6/include/python3.6m _utilsmodule.c -o _utils.so
	gcc -g -fPIC -shared -I/opt/python/3.6/include/python3.6m _typesmodule.c -o _types.so
	py.test -sv


clean:
	rm -f *.so *.o
