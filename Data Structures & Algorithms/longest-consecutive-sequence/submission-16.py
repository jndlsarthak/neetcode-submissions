class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        dup = sorted(set(nums))

        if len(dup) >= 2:
            current = 1
            longest = 1

            for i in range(len(dup) - 1):
                if dup[i] + 1 == dup[i + 1]:
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 1
            longest = max(longest, current)

            return longest

        else:
            return len(dup)
        
    

        