class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a+b


        # mask = 0xFFFFFFFF
        # while b != 0:
        #     # Calculate carry bits, limited to 32 bits
        #     carry = (a & b) << 1
        #     # Calculate sum without carry, limited to 32 bits
        #     a = (a ^ b) & mask
        #     # Move the carry to b for the next iteration
        #     b = carry & mask           
        # # If the 32nd bit is 1, the number is negative in two's complement
        # if a > 0x7FFFFFFF:
        #     return ~(a ^ mask)
        # return a