class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     if target in matrix[i]:
        #         return True
        #     else:
        #         return False
        # return True

        res = False
        i = 0
        while i < len(matrix):
            if target in matrix[i]:
                res = True
                break
            else:
                i+=1
        return res