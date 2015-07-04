#include "Python.h"

PyMODINIT_FUNC
init_types(void)
{
    PyObject *m;
    m = Py_InitModule("_types", NULL);
    PyModule_AddObject(m, "FunctionType", &PyFunction_Type);
}
