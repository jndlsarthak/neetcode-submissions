class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idc = {}

        # for i in s:
        #     idc[i] = s.count(i)
        #     ele = max(idc.values())
        #     if len(s) - ele >= k:
        #         return ele + k
        #     else:
        #         return ele 
        idc = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            idc[s[right]] = idc.get(s[right], 0) + 1

            ele = max(idc.values())

            while (right - left + 1) - ele > k:
                idc[s[left]] -= 1
                left += 1
                ele = max(idc.values())

            longest = max(longest, right - left + 1)

        return longest