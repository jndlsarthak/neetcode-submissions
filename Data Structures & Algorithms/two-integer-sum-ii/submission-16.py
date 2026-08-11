class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # acc = []
        # n= len(numbers)
 

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if numbers[i] + numbers[j] == target and j>i :
        #             acc = [i+1, j+1]
        # return acc

        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]


            