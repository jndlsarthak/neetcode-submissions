class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = list(range(len(nums)+1))
        df = list(set(num)-set(nums))
        return df[0]