#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

bool isHappy(int n){
	int contador = 0;
	int primeiro = 0;
	int nDigits = floor(log10(abs(n)));
	int n_final = 0;
	do
	{
		n_final = 0;
		primeiro = 0;
		nDigits = floor(log10(abs(n)));
		for (int i = nDigits; i >= 0; --i)
		{
			n = n - primeiro;
			n_final += pow((int)(n / pow(10, i)), 2);
			primeiro = (int)(n / pow(10, i)) * (pow(10, i));
		}
		n = n_final;
		contador = contador + 1;
		if (contador > 99)
		{
			n_final = 0;
			break;
		}
	} while (n_final != 1);
	return n_final;
}

int main()
{
	int n;
	scanf("%d", &n);

	printf("%d\n", isHappy(n));

	return 0;
}

