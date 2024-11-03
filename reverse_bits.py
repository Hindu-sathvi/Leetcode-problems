#https://leetcode.com/problems/reverse-bits/?envType=problem-list-v2&envId=divide-and-conquer
#Code:
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reversed_num = 0
        for i in range(32):
            last_bit = n & 1
            reversed_num = (reversed_num << 1) | last_bit
            n >>= 1
        return reversed_num
