class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return a+b


        mask = 0xFFFFFFFF
        while b != 0:            
            carry = (a & b) << 1        # Calculate carry bits, limited to 32 bits
            a = (a ^ b) & mask          # Calculate sum without carry, limited to 32 bits
            b = carry & mask            # Move the carry to b for the next iteration       
        if a > 0x7FFFFFFF:              # If the 32nd bit is 1, the number is negative in two's complement
            return ~(a ^ mask)
        return a