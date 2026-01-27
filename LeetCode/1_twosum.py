class Solution(object):
    def twoSum(self, nums, target):
        indexes = []

        #I want to add the first sum and +1 of that index to see if
        #it equals the target
        for i in range(len(nums)):

            if ((nums[i] + nums[i+1]) == target):
                indexes.append(i)
                indexes.append(i+1)
                break
            else:
                for j in range(len(nums)):
                    if (nums[i] + nums[j] == target):
                        indexes.append(i)
                        indexes.append(j)
                        break
        return indexes

#### Testing
test = Solution()
nums = [2,7,11,15]
target = 9
print(test.twoSum(nums, target))

#Test 2
nums2 = [3,2,4] 
target2 = 6

print(test.twoSum(nums2, target2))

#Test 3
nums3 = [3,3]
target3 = 6

#Expected Output: [0,1]

print(test.twoSum(nums3, target3))