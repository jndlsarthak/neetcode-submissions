class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if nums:
        #     for i in range(k-1):
        #         nums.remove(max(nums))
        #     return max(nums)
        # else:
        #     return 0

        nums = sorted(nums)
        return nums[-k]