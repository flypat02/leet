class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        
        while val in nums:
            nums.remove(val)
            
        return len(nums)