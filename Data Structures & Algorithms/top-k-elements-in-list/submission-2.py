class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1


        sorted_nums = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)
        return sorted_nums[:k]