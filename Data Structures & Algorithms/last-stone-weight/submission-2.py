class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # brute force
        stones.sort()
        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            if first - second > 0:
                stones.append(first - second)
                stones.sort()
        if stones:
            return stones[0]
        return 0