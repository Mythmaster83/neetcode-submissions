from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            anagram_map["".join(sorted(word))].append(word)

        return list(anagram_map.values())