class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for idx in range(n - 1, 0, -1):
            if nums[idx] > nums[idx - 1]:
                for idx2 in range(n - 1, idx - 1, -1):
                    if nums[idx - 1] < nums[idx2]:
                        tmp_val = nums[idx2]
                        nums[idx2] = nums[idx - 1]
                        nums[idx - 1] = tmp_val
                        if idx < n - 1:
                            nums[idx:] = nums[idx:][::-1]
                            
                        return
        nums.sort()
