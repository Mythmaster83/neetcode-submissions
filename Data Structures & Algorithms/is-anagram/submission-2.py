class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        set1 = set(s)
        set2 = set(t)

        for i in set1:
            if i not in set2 or s.count(i) != t.count(i):
                return False
        return True
