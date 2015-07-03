#include "Python.h"

static PyObject *
hello_world(void) {
    return PyString_FromString("hello world");
}


static PyMethodDef HelloMethods[] = {
    {"world", hello_world, METH_NOARGS, "hello world's doc"},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
inithello(void)
{
    PyObject *m = Py_InitModule("hello", HelloMethods);
}
