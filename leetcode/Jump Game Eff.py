class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        n = len(nums)
        for idx, value in enumerate(nums):
            if idx > reachable:
                break
            reachable = max(reachable, idx + nums[idx])
        return reachable >= n - 1
