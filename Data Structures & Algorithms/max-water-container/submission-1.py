class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ### brute force solution:
        # n = len(heights)
        
        # max_area = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if i == j:
        #             continue
        #         length = min(heights[i],heights[j])
        #         breadth = abs(j-i)
        #         area = length * breadth
        #         max_area = max(area,max_area)
                
        # return max_area




        l =0
        r = len(heights)-1
        res = 0
        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r-=1
        return res
            