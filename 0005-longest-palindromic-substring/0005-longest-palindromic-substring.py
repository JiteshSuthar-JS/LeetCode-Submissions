class Solution:
    def longestPalindrome(self, s: str) -> str: 
        def ispalindrome(string: str) -> bool:
            return string == string[::-1]

        max_pal = ""
        for left in range(len(s)):
            for right in range(left, len(s)):
                substring = s[left:right+1]
                if ispalindrome(substring) and len(substring) > len(max_pal):
                    max_pal = substring
        return max_pal
