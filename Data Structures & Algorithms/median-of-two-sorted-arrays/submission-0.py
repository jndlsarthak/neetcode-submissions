class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fin = sorted(nums1 + nums2)
        n = len(fin)
        if n%2 != 0:
            return fin[n//2]
        else:
            numt = (fin[n//2] + fin[(n//2)-1])
            return numt/2