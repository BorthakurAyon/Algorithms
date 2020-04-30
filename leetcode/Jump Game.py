class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_idx, prev_idx, steps = 0, 0, 0
        n = len(nums)
        while (curr_idx < n):
            prev_idx = curr_idx
            steps += 1
            for idx in range(0, prev_idx + 1):
                curr_idx = max(curr_idx, idx + nums[idx])
                if curr_idx >= n - 1:
                    return True
                elif steps > n:
                    return False
