#https://leetcode.com/problems/group-anagrams/description/
#Code:
#using hashmap
class Solution(object):
    def __init__(self):
        self.anagrams = {}

    def groupAnagrams(self, strs):
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in self.anagrams:
                self.anagrams[sorted_word] = []
            self.anagrams[sorted_word].append(word)
        return [sorted(group) for group in self.anagrams.values()]
