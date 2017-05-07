#include "Python.h"

static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_types",
    "a Python module",
    -1,
    module_methods,
};


PyMODINIT_FUNC
PyInit__types(void)
{
    PyObject *m;
    m = PyModule_Create(&module);
    PyModule_AddObject(m, "FunctionType", (PyObject *)&PyFunction_Type);
    PyModule_AddObject(m, "LambdaType", (PyObject *)&PyFunction_Type);
    PyModule_AddObject(m, "CodeType", (PyObject *)&PyCode_Type);
    PyModule_AddObject(m, "GeneratorType", (PyObject *)&PyGen_Type);
    PyModule_AddObject(m, "ModuleType", (PyObject *)&PyModule_Type);
    return m;
}
