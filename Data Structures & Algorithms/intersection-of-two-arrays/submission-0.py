class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        qnums1 = set(nums1)
        qnums2 = set(nums2)

        return list(qnums1 & qnums2)