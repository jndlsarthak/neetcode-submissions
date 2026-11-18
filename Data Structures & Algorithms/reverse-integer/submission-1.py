class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev =  0 -  int(str(x)[:0:-1])
        else:
            rev =  int(str(x)[::-1])            
        if (rev > ((2**31)-1)) or (rev < -(2**31)):
            rev =  0
        return rev