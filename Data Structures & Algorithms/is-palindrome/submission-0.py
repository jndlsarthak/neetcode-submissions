class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not (i.isdigit() or i.isalpha()):
                s = s.replace(i,"")
        s = s.lower()
        return (s[::-1]) == s