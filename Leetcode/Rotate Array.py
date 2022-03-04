class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            n=nums[-1]
            nums.insert(0,n)
            nums.pop()
        
        return nums
        
