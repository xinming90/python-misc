#include "Python.h"

PyMODINIT_FUNC
init_types(void)
{
    PyObject *m;
    m = Py_InitModule("_types", NULL);
    PyModule_AddObject(m, "FunctionType", &PyFunction_Type);
    PyModule_AddObject(m, "LambdaType", &PyFunction_Type);
    PyModule_AddObject(m, "CodeType", &PyCode_Type);
    PyModule_AddObject(m, "GeneratorType", &PyGen_Type);
    PyModule_AddObject(m, "ClassType", &PyClass_Type);
    PyModule_AddObject(m, "ModuleType", &PyModule_Type);
    PyModule_AddObject(m, "TypeType", &PyType_Type);
    PyModule_AddObject(m, "DictProxyType", &PyDictProxy_Type);
}
