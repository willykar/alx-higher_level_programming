#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int size_st;
	int integer;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size_st);

	printf("  size_struct: %li\n", size_st);
	printf("  trying string: %s\n", trying_str);
	if (size_st < 10)
		printf("  first %li bytes:", size_st + 1);
	else
		printf("  first 10 bytes:");
	for (integer = 0; integer <= size_st && integer < 10; integer++)
		printf(" %02hhx", trying_str[integer]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int integer;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (integer = 0; integer < size; integer++)
        {
                type = (list->ob_item[integer])->ob_type->tp_name;
		printf("Element %i: %s\n", integer, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[integer]);
        }
}
