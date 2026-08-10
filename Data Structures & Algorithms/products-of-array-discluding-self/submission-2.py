class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]

        #     res[i] = prod
        # return res


        n = len(nums)
     
        acc= [0]*n
        zero_count = 0
        prod = 1
        for i in range(n):
            if nums[i] == 0:
                zero_count+=1
                continue
            prod = nums[i] * prod
        if zero_count > 1:
            return acc

        res= [0]*n
        for j in range(n):
            if zero_count == 1:
                if nums[j] == 0 :
                    res[j] = prod

            else:
                res[j] = prod // nums[j]

        return res

        



