#include <stdio.h>

int main()
{
    int qntd_vagoes;
    scanf("%d", &qntd_vagoes);
    int zero = 0;

    while(qntd_vagoes != 0)
    {
    	int trem_vem[qntd_vagoes];
    	int i;
    	/* Criacao do trem que está vindo */
    	for (i = 1; i <= qntd_vagoes; ++i)
    	{
    		trem_vem[i-1]=i;
    	}


    	while(1==1)
    	{
    		int contagem = 0;
			/* Criacao do trem que vai */
	    	int trem_vai[qntd_vagoes];
	    	for (i = 1; i <= qntd_vagoes; ++i)
	    	{
	    		scanf("%d", &trem_vai[qntd_vagoes-i]);
	    		if(trem_vai[qntd_vagoes-1] == 0)
	    		{
	    			zero = 1;
	    			break;
	    		}
	    	}
	    	if (zero == 1)
	    	{
	    		printf("\n");
	    		break;
	    	}

	    	/* Cria estacao */
	    	int estacao[qntd_vagoes];
	    	for (i = 0; i < qntd_vagoes; ++i)
	    	{
	    		estacao[i] = 0;
	    	}

	    	int indice_estacao = 0;
	    	int j = qntd_vagoes-1;

	    	int t = 0;
	    	int deu_errado = 0;
	    	while(contagem < qntd_vagoes)
	    	{
	    		if (trem_vem[t] == trem_vai[j])
	    		{
	    			contagem++;
	    		} else 
	    		{
	    			int deu_certo = 0;
	    			int x;
	    			for (x = 0; x <= indice_estacao; ++x)
	    			{
	    				if(estacao[x] == trem_vai[j] && estacao[x + 1] != 0)
	    				{
	    					printf("No\n");
	    					deu_errado = 1;
	    					break;
	    				} else if (estacao[x] == trem_vai[j] && estacao[x + 1] == 0)
	    				{
	    					contagem++;
	    					indice_estacao--;
	    					estacao[indice_estacao] = trem_vai[t];
	    					t--;
	    					deu_certo = 1;
	    					estacao[x] = 0;
	    					break;
	    				}
	    			}
	    			if (deu_certo == 0)
	    			{
	    				estacao[indice_estacao] = trem_vem[t];
	    				indice_estacao++;
	    				j++;
	    			}
	    		}
	    		if (deu_errado == 1)
	    		{
	    			break;
	    		}
	    		j--;
				t++;
				if(t > qntd_vagoes-1)
				{
					t = qntd_vagoes-1;
				}
	    	}
	    	if (contagem == qntd_vagoes)
	    	{
	    		printf("Yes\n");
	    	}
	    }
	    scanf("%d", &qntd_vagoes);
	    zero = 0;
    }
    return 0;
}