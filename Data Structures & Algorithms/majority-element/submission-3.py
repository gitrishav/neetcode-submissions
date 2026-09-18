class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        return max(seen, key=seen.get)         
        