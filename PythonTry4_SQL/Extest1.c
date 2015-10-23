#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int fac(int n)
{
	if (n < 2) return 1;
	return n*(fac(n - 1));
}

static PyObject* Extest_fac(PyObject *self, PyObject *args)
{
	int num;
	PyObject* retval;
	if (!PyArg_ParseTuple(args, "i", &num))
		return NULL;
	res = fac(num);
	retval = (PyObject*)Py_BuildValue("i", res);
	return retval;
}

/*
char* reversze(char *s)
{
register char t,
*p = s,
*q = (s + (strelen(s) - 1));
while (p < q)
{
t = *p;
*p++ = *q;
*q-- = t;
}
return s;
}
*/


int main()
{
	//char s[BUFSIZE];
	printf("4! : %d\n", fac(4));
	printf("8! : %d\n", fac(8));
	printf("12! : %d\n", fac(12));
}

