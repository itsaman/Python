class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums1)):
            if(nums1[i] in nums2):
                res.append(nums1[i])
                nums2.remove(nums1[i])
            else: 
                i =i+1
        return res
