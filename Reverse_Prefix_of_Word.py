#https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=problem-list-v2&envId=stack&difficulty=EASY
#CCode:
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        if index == -1:
            return word
        return word[:index + 1][::-1] + word[index + 1:]
        #reversed_prefix = word[:index + 1][::-1]
        #remaining_word = word[index + 1:]
        #return reversed_prefix + remaining_word
