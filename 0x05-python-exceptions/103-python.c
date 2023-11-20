#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double value;
	char *string = NULL;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);

}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	char *byteString;

	if (!p || !PyBytes_Check(p))
	{
		fprintf(stderr, "[!] Invalid argument. Expected a bytes object.\n");
		return;
	}
	assert(PyBytes_Check(p));

	PyBytesObject *byteObj = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));

	byteString = PyBytes_AsString(p);
	if (!byteString)
	{
		fprintf(stderr, "[!] Failed to retrieve string from bytes object.\n");
		return;
	}

	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 6 bytes: ");
	for (Py_ssize_t i = 0; i < 6 && i < PyBytes_Size(p); ++i)
	{
		printf("%02x ", (unsigned char)byteObj->ob_sval[i]);
	}
	printf("\n");
}


/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	printf("[*] Python list info\n");

	if (!PyList_CheckExact(p))
		printf("  [ERROR] Invalid List Object\n");
	else
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			i++;
		}
	}

}
