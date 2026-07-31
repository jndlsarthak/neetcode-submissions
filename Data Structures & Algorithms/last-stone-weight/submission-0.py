class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]

        maxi = max(stones)
        stones.remove(maxi)

        maxi1 = max(stones)
        stones.remove(maxi1)

        diff = maxi - maxi1

        if diff > 0:
            stones.append(diff)

        return self.lastStoneWeight(stones)