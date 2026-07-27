class Solution:

    def encode(self, strs: List[str]) -> str:
        an = ""
        for i in strs:
            b = i + "é"
            an += b
        return an

    def decode(self, s: str) -> List[str]:
        l = s.split("é")
        ans = []

        for i in l[:-1]:
            ans.append(i)

        return ans