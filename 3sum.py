class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = set()
        for idx, item in enumerate(nums):
            target = -item
            i = idx + 1
            j = len(nums) - 1
            sum = 0
            while (i < j):
                sum = nums[i] + nums[j]
                if sum < target:
                    i += 1
                elif sum > target:
                    j -= 1
                else:
                    output.add((item, nums[i], nums[j]))
                    i += 1
                    j -= 1
                    
        return output
            
