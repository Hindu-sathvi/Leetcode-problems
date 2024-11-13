#https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=heap-priority-queue
#Code:
#General Solution
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
#using max heap:
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        for _ in range(k - 1):
            heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)

#using min heap:
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]
        
