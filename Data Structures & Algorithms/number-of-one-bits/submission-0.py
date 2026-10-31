class Solution:
    def hammingWeight(self, n: int) -> int:
        b = str(bin(n))
        x = 0
        for i in range(len(b)):
            if b[i] == '1':
                x +=1
        return x

