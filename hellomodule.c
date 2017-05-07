#include "Python.h"

static PyObject*
hello_world(void) {
    return PyUnicode_FromString("hello world");
}


static PyMethodDef module_methods[] = {
    {
        "world",
        (PyCFunction)hello_world,
        METH_NOARGS,
        "hello world's doc"
    },
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef module = {
   PyModuleDef_HEAD_INIT,
   "hello",
   "a Python module",
   -1,
   module_methods,
};


PyMODINIT_FUNC
PyInit_hello(void)
{
    return PyModule_Create(&module);
}
