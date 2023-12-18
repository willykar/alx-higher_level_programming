#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - A function that gives data of the PyFloatObject
 * @p: the PyObject data
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
/**
 * print_python_bytes - A function that gives data of the PyBytesObject
 * @p: the PyObject data
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, a = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (a < size + 1 && a < 10)
	{
		printf(" %02hhx", string[a]);
		a++;
	}
	printf("\n");
}
/**
 * print_python_list - A function that gives data of the PyListObject
 * @p: The PyObject data
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *it;
	int a = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (a < size)
		{
			it = PyList_GET_ITEM(p, a);
			printf("Element %d: %s\n", a, it->ob_type->tp_name);
			if (PyBytes_Check(it))
				print_python_bytes(it);
			else if (PyFloat_Check(it))
				print_python_float(it);
			a++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
