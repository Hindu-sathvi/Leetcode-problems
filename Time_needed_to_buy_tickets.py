#https://leetcode.com/problems/time-needed-to-buy-tickets/description/?envType=problem-list-v2&envId=queue
#code:
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        n = len(tickets)
        
        # Continue the loop until the k-th person has finished buying all tickets
        while tickets[k] > 0:
            for i in range(n):
                # If the current person has tickets left to buy
                if tickets[i] > 0:
                    # Decrease their ticket count by 1 (since they buy 1 ticket)
                    tickets[i] -= 1
                    # Increase the time taken by 1 second
                    time += 1
                    
                    # If the k-th person finishes buying tickets, return the total time
                    if tickets[k] == 0:
                        return time
