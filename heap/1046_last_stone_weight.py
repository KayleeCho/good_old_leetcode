import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while (len(stones) > 1):
            max1 = abs(heappop(stones))
            max2 = abs(heappop(stones))

            remaining = max1 - max2
            if remaining != 0:
                heappush(stones, - remaining)

        return 0 if not stones else abs(heappop(stones))