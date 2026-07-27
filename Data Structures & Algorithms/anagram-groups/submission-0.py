class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = strs
        ans = []
        ind = []
        for i in range(len(strs)):
            if i in ind:
                pass
            else:
                temp = [strs[i]]
                for g in range(i+1, len(strs)):
                    if len(strs[i]) != len(strs[g]):
                        pass
                    else:
                        ird = True
                        set1 = set(strs[i])
                        set2 = set(strs[g])
                        for f in set1:
                            if f not in set2 or strs[i].count(f) != strs[g].count(f):
                                ird = False
                                break
                        if ird == True:
                            temp.append(strs[g])
                            ind.append(g)
                ans.append(temp)
        return ans