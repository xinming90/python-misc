#include "Python.h"

static PyObject *
isiterator(PyObject *self, PyObject *v) {
    if (v->ob_type->tp_iter == NULL)
        return Py_False;
    return Py_True;
}

static PyMethodDef module_methods[] = {
    {"isiterator", isiterator, METH_O, "isiterator's doc"},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
init_utils(void)
{
    PyObject *m = Py_InitModule("_utils", module_methods);
}
