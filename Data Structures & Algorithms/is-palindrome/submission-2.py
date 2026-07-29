class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ("".join([char for char in s if char.isalnum()])).lower()
        return n == n[::-1]
        