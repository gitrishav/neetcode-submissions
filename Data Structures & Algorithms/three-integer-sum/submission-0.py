class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate Anchors so we don't evaluate the same starting number twice
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # ACTION 1: Sum is too small, step left pointer up to get a bigger number
                    left += 1
                elif total > 0:
                    # ACTION 2: Sum is too big, step right pointer down to get a smaller number
                    right -= 1
                else:
                    # We found a match!
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    # ACTION 3: Skip duplicate numbers for the 'left' pointer to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res