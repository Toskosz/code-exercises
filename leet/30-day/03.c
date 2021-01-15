#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/*Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.*/

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

int main()
{
	int numsSize;
	scanf("%d", &numsSize);
	int nums[numsSize];

	for (int i = 0; i < numsSize; ++i)
	{
		scanf("%d", &nums[i]);
	}

	int max  = maxSubArray(nums, numsSize);

	printf("maximo = %d\n", max);

	return 0;
}