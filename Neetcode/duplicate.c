#include <stdio.h>

_Bool containsDuplicate(int * nums, int numSize)
{
    int counter = 0;
    int temp = nums[0]; 

    for (int i = 1; i < numSize; i++)
    {
        if (nums[i] == temp)
        {
            counter++;
            
        }
    }
    if (counter >= 1)
    {
        return 1;
    }
    else
        return 0;
}



int main(){
    int nums[] = {1, 2, 3, 1};

    _Bool check = containsDuplicate(nums, 4);
    printf("%d", check);

    return 0;
}


