class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
    
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, count in seen.items():
            freq[count].append(num)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res