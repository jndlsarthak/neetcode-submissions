class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                return [[]]
            s_sublists = backtrack(start + 1)
            return [[nums[start]] + sub for sub in s_sublists] + s_sublists
        return backtrack(0)
   
   