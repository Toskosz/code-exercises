#include <stdio.h>
#include <string.h>

int main()
{
	int n;
	scanf("%d", &n);	

	for (int i = 0; i < n; ++i)
	{
		int contador_leds = 0;
		char numero[101];
		scanf(" %s", numero);

		for (int j = 0; j < strlen(numero); ++j)
		{
			switch(numero[j])
			{
				case('1'):
					contador_leds += 2;
					break;
				case('2'):
					contador_leds += 5;
					break;
				case('3'):
					contador_leds += 5;
					break;
				case('4'):
					contador_leds += 4;
					break;
				case('5'):
					contador_leds += 5;
					break;
				case('6'):
					contador_leds += 6;
					break;
				case('7'):
					contador_leds += 3;
					break;
				case('8'):
					contador_leds += 7;
					break;
				case('9'):
					contador_leds += 6;
					break;
				case('0'):
					contador_leds += 6;
					break;
			}
		}

		printf("%d leds\n", contador_leds);

	}


	return 0;
}


