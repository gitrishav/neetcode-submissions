class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n-1

        inPos = n-1

        while left <= right:
            ls = nums[left] ** 2
            rs = nums[right] ** 2

            if rs > ls:
                result[inPos] = rs
                right -= 1
            else:
                result[inPos] = ls
                left += 1
            inPos -= 1  

        return result           

