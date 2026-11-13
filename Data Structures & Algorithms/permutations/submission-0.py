class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        perms = permutations(nums)
        return [list(p) for p in perms]