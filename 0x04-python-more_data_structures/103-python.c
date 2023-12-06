#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - A function that prints some basic info
 * about Python bytes objects
 * @p: The python object
 **/
void print_python_bytes(PyObject *p)
{
  char *st;
  Py_ssize_t length, a;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p))
    printf("  [ERROR] Invalid Bytes Object\n");
  else
    {
      PyBytes_AsStringAndSize(p, &st, &length);
      printf("  size: %lu\n", length);
      printf("  trying string: %s\n", st);
      if (length > 10)
	length = 10;
      else
	length++;
      printf("  first %lu bytes: ", length);
      for (a = 0; a < length - 1; a++)
	printf("%02x ", st[a] & 0xff);
      printf("%02x\n", s[length - 1] & 0xff);
    }
}


/**
 * print_python_list - A function that prints some info about Python lists
 * @p: The python object
 **/
void print_python_list(PyObject *p)
{
  Py_ssize_t a;
  PyObject *inn_list;

  if (PyList_Check(p))
    {
      printf("[*] Python list info\n");
     printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
      printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
      for (a = 0; a < PyList_Size(p); a++)
	{
	  inn_list = PySequence_GetItem(p, a);
	  printf("Element %lu: %s\n", a,
		 inn_list->ob_type->tp_name);
	  if (strcmp(inn_list->ob_type->tp_name, "bytes") == 0)
	    print_python_bytes(inn_list);
	}
    }
}
