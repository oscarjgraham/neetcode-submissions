class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        for i in s:
            if not i.isalnum():
                s = s.replace(i, "")
        s = s.lower()
        s = s.replace(" ", "")
        
        
        print(s)

        for i in range(len(s)):
            if s[i] != s[-1-i]:
                return False
        return True