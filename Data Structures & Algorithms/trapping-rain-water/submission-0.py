class Solution:
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     sum = 0 
    #     max_soFar = 0 
    #     for i in range(n):
    #         max_soFar = max(height[i], max_soFar)
    #         sum += max_soFar - height[i] 
    #     return sum
        

    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        leftMax = []
        max_soFar = 0

        for i in range(n):
            max_soFar = max(height[i], max_soFar)
            leftMax.append(max_soFar)

        rightMax = [0] * n
        max_soFar = 0

        for i in range(n - 1, -1, -1):
            max_soFar = max(height[i], max_soFar)
            rightMax[i] = max_soFar

        for i in range(n):
            total += min(leftMax[i], rightMax[i]) - height[i]

        return total