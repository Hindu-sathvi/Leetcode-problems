#https://leetcode.com/problems/last-stone-weight/?envType=problem-list-v2&envId=heap-priority-queue
#Code:
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)
            if heaviest != second_heaviest:
                heapq.heappush(stones, -(heaviest - second_heaviest))
        if stones:
            return -stones[0]
        return 0
