class Solution:
    def isHappy(self, n: int) -> bool:
    #     visit = set()
    #     while n not in visit:
    #         visit.add(n)
    #         n = self.sumOfSquares(n)
    #         if n==1:
    #             return True
    #         return False

    # def sumOfSquares(self, n: int) -> int:
    #     output = 0
    #     while n:
    #         digit = n % 10
    #         digit = digit ** 2
    #         output += digit
    #         n = n // 10
    #     return output

        seen = set()
        while n not in seen:
            seen.add(n)
            digits = map(int, list(str(n)))
            n = 0
            for digit in digits: 
                n += digit ** 2
            if n == 1: 
                return True
        return False