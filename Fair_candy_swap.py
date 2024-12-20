#https://leetcode.com/problems/fair-candy-swap/?envType=problem-list-v2&envId=binary-search
#Code:
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        diff = (sumAlice - sumBob) // 2
        bobSet = set(bobSizes)
    
        for a in aliceSizes:
            b = a - diff
            if b in bobSet:
                return [a, b]
        
