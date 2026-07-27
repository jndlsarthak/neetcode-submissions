class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_items = []
        for value in nums:
            if value in seen_items:
                return True
            seen_items.append(value)
        return False
                
