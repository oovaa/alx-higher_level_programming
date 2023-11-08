#include <stdio.h>
#include <Python.h>

/**
 * print_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_bytes(PyObject *p)
{
char *string;
long int size, i, lim;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

string = ((PyBytesObject *)p)->ob_sval;
size = ((PyVarObject *)p)->ob_size;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);

if (size >= 10)
lim = 10;
else
lim = size + 1;

printf("  first %ld bytes:", lim);

for (i = 0; i < lim; i++)
if (string[i] >= 0)
printf(" %02x", string[i]);
else
printf(" %02x", 256 + string[i]);

printf("\n");
}

/**
 * print_python_list - Prints list info
 *
 * @p: Python Object
 * Return: none
 */
void print_python_list(PyObject *p)
{
int size, i;
PyListObject *list;
PyObject *obj;

list = (PyListObject *)p;
size = ((PyVarObject *)p)->ob_size;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
obj = ((PyListObject *)p)->ob_item[i];
printf("Element %d: %s\n", i, ((obj)->ob_type)->tp_name);
if (PyBytes_Check(obj))
print_bytes(obj);
}
}
