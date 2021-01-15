#include <stdio.h>
#include <stdlib.h>

int main()
{
	int qntd_casos;
	scanf("%d", &qntd_casos);

	// Function to return gcd of a and b 
	int gcd(int a, int b) 
	{ 
    	if (a == 0) 
        	return b; 
    	return gcd(b%a, a); 
	} 


	for (int i = 0; i < qntd_casos; ++i)
	{
		int n_res, d_res;
		int n1, n2, d1, d2;
		char op;
		scanf("%d / %d %c %d / %d", &n1, &d1, &op, &n2, &d2);

		if (op == '+')
		{
			n_res = n1*d2 + n2*d1;
			d_res = d1 * d2;
		} else if (op == '-')
		{
			n_res = n1*d2 - n2*d1;
			d_res = d1 * d2;
		} else if (op == '*')
		{
			n_res = n1*n2;
			d_res = d1*d2;
		}else if (op == '/')
		{
			n_res = n1*d2;
			d_res = n2*d1;
		}

		int mdc = gcd(n_res, d_res); 

		int n_final = n_res / abs(mdc);
		int d_final = d_res / abs(mdc);

		printf("%d/%d = %d/%d\n", n_res, d_res, n_final, d_final);

	}





	return 0;
}