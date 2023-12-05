#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#include <stddef.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info - A function that prints some basic
 * info about Python lists
 * @p: The python list
 */
void print_python_list_info(PyObject *p) {
    Py_ssize_t size, alloc;
    PyListObject *list = (PyListObject *)p;

    size = PyList_Size(p);
    alloc = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (Py_ssize_t i = 0; i < size; ++i) {
        printf("Element %zd: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
