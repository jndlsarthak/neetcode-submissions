class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        acc = []
        for i in nums:
            if i in acc:
                return True
            acc.append(i)
        return False