class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        # Approach 1
        # create a max = 0, count = 0 
        # create i = 0 
        # while el at i doesnt repeat increase max 
        # now start at the repeated i and increase count and return max(max,count)
        # loop on i 
        chars = set()
        left = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            longest = max(longest, right - left + 1)

        return longest
        
      
        # Approach 2
        # zz = []
        # length = len(s)
        # xx =  [s[i:j] for i in range(length) for j in range(i + 1, length + 1)]
        # for uu in xx :
        #   if uu[0] == uu[-1]:
        #     zz.append(uu)
        # return len(max(zz))-2