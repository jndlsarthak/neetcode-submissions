class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        acc= []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    acc.append(i)
                    acc.append(j)
                    

        return acc


