#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
	char matriz[3][10];

	strcopy(matriz[0], "abc");
	strcopy(matriz[1], "def");
	strcopy(matriz[2], "ghi");



	printf("%s\n", matriz[0]);
	printf("%s\n", matriz[1]);
	printf("%s\n", matriz[2]);



	return 0;
}