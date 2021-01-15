int singleNumber(int* nums, int numsSize){
	int contador = 0;
	int n;
    for(int i = 0; i<numsSize; i++)
    {
    	contador = 0;
    	for (int j = 0; j < numsSize; ++j)
    	{
    		if (nums[i] == nums[j])
    		{
    			contador++;
    		}
    	}
    	if (contador == 1)
    	{
    		n = nums[i];
    	}
    }
    return n;
}