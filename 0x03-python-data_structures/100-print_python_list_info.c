#include <Python.h>
#include <object.h>
#include <listobject.h>


/*
 * print_python_list_info - Prints information about a Python list.
 * @p: PyObject representing a Python list.
 *
 * Description: This function takes a PyObject pointer representing a Python
 * list and prints information about the list, including its size,
 * allocated size, and the types of its elements.
 */

void print_python_list_info(PyObject *p)
{

	if (PyList_Check(p))
	{
		PyListObject *listObj = (PyListObject *)p;

		printf("[*] Size of the Python List = %li\n", PyList_Size(p));
		printf("[*] Allocated = %li\n", listObj->allocated);

		for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
			printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

	}
	else
	{
		printf("Error: Object is not a list.\n");
	}

}
