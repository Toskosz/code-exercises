#include <stdio.h>
#include <stdlib.h>

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}



int main()
{
	int caso = 1;

	int n, q;
	scanf("%d %d", &n, &q);

	while(n != 0 && q != 0)
	{
		int marmores[n];
		int i;
		for (i = 0; i < n; ++i)
		{
			scanf("%d", &marmores[i]);
		}	

		qsort(marmores, n, sizeof(int), cmpfunc);

		printf("CASE# %d:\n", caso);

		for (i = 0; i < q; ++i)
		{
			int achou = 0;
			int chute, j;
			scanf("%d", &chute);
			for (j = 0; j < n; ++j)
			{
				if(chute == marmores[j])
				{
					achou = 1;
					break;
				}
			}
			if (achou == 1)
			{
				printf("%d found at %d\n", chute, j+1);
			} else 
			{
				printf("%d not found\n", chute);
			}
		}
		caso++;
		scanf("%d %d", &n, &q);
	}


	return 0;
}