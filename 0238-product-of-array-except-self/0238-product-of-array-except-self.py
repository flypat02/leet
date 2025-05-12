class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        
        wen = 1
        for i in range(n):
            output[i] = wen
            wen *= nums[i]
        
        
        oh = 1
        for i in range(n-1, -1, -1):
            output[i] *= oh
            oh *= nums[i]
        
        return output