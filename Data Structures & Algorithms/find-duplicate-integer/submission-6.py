class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s = len(nums)
        for i in range(1,s): 
            if nums[i] == nums[i-1]:
                return nums[i]             
    