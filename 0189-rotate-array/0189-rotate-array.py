class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = nums[n - k:] + nums[:n - k]
        for i in range(len(nums)):
            nums[i] = temp[i]
        