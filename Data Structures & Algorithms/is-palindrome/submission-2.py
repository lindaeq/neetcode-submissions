class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1 = []
        t1 = []

        for char in s:
            if char.isalnum():
                s1.append(char.lower())

        if s1 == s1[::-1]:
            return True
        return False