#include "Python.h"
#include "_utilsmodule.h"

static PyObject *
isiterator(PyObject *self, PyObject *v)
{
    if (v->ob_type->tp_iter == NULL)
        return Py_False;
    return Py_True;
}


static PyObject *
ilen(PyObject *self, PyObject *v)
{
    if (PyListIter_CheckExact(v)) {
        listiterobject *v = (listiterobject *)v;
        return PyInt_FromLong(Py_SIZE(v->it_seq));
    }
    return v;
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
    type->tp_flags |= Py_TPFLAGS_HEAPTYPE;
    return v;
}


static PyObject *
_assert(PyObject *self, PyObject *args)
{
    PyObject *ob;
    PyObject *exc = PyExc_AssertionError;
    if (!PyArg_ParseTuple(args, "O|O", &ob, &exc))
        return NULL;
    if (PyObject_IsTrue(ob))
        return Py_True;
    if (PyExceptionClass_Check(exc))
        PyErr_SetNone(exc);
    else if (PyExceptionInstance_Check(exc))
        PyErr_SetObject(PyExceptionInstance_Class(exc), exc);
    return NULL;
}


static PyMethodDef module_methods[] = {
    {"isiterator", isiterator, METH_O, "isiterator's doc"},
    {"ilen", ilen, METH_O, "ilen's doc"},
    {"hashable", hashable, METH_O, "hashable's doc"},
    {"setflag", setflag, METH_O, "setflag's doc"},
    {"_assert", _assert, METH_VARARGS, "_assert's doc"},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
init_utils(void)
{
    PyObject *m = Py_InitModule("_utils", module_methods);
}
