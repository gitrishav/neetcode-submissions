class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for position, n in enumerate(nums):
            reqNum = target - n

            if reqNum in seen:
                return [seen[reqNum], position]

            seen[n] = position    