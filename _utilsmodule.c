#include "Python.h"

static PyObject *
isiterator(PyObject *self, PyObject *v)
{
    if (v->ob_type->tp_iter == NULL)
        return Py_False;
    return Py_True;
}


static PyObject *
hashable(PyObject *self, PyObject *v)
{
    hashfunc tp_hash = v->ob_type->tp_hash;
    if (tp_hash == NULL)
        return Py_False;
    // list->tp_hash = PyObject_HashNotImplemented
    if (tp_hash == PyObject_HashNotImplemented)
        return Py_False;
    return Py_True;
}

static PyObject *
setflag(PyObject *self, PyObject *v)
{
    PyTypeObject *type = (PyTypeObject*)v;
    type->tp_flags = type->tp_flags | Py_TPFLAGS_HEAPTYPE;
    return v;
}


static PyMethodDef module_methods[] = {
    {"isiterator", isiterator, METH_O, "isiterator's doc"},
    {"hashable", hashable, METH_O, "hashable's doc"},
    {"setflag", setflag, METH_O, "setflag's doc"},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
init_utils(void)
{
    PyObject *m = Py_InitModule("_utils", module_methods);
}
