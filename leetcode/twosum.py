class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx0, val0 in enumerate(nums):
            for idx1, val1 in enumerate(nums[idx0+1:]):
                if val0+val1 == target:
                    return [idx0, idx0 + idx1 + 1]
        else:
            return []
