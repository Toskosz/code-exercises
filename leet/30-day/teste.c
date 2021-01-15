

int maxSubArray(int* nums, int numsSize){
	int max_atual = nums[0];
	int max_global = nums[0];
	for (int i = 1; i < numsSize; ++i)
	{
		if (nums[i] > max_atual + nums[i])
		{
			max_atual = nums[i];
		} else if (max_atual + nums[i] > nums[i])
		{
			max_atual += nums[i];
		} else {
			max_atual = nums[i];
		}

		if (max_atual > max_global)
		{
			max_global = max_atual;
		}
	}

	return max_global;
}

