class Solution(object):
    def twoSum(self, nums, target):
        indexes = []
        valueAddOne = -99999

        #I want to add the first sum and +1 of that index to see if
        #it equals the target

        for i in range(len(nums)):

            if ((nums[i] + nums[i+1]) == target):
                #java
                indexes.append(i)
                break
    
        if indexes[0] != None:
            valueAddOne = indexes[0]+1
        
        #elegant printf instead of print
        print(f"[{indexes[0]}, {valueAddOne}]")

#### Testing
test = Solution()
nums = [2,7,11,15]
target = 9
test.twoSum(nums, target)

#Test 2
nums2 = [3,2,4] 
target2 = 6

test.twoSum(nums2, target2)

#Test 3
nums3 = [3,3]
target3 = 6

#Expected Output: [0,1]

test.twoSum(nums3, target3)