class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2:
            if s[p1] != s[p2]:
                # Check if removing s[p1] makes the substring [p1+1, p2] a palindrome
                if is_palindrome_range(p1 + 1, p2):
                    return True
                
                # Check if removing s[p2] makes the substring [p1, p2-1] a palindrome
                if is_palindrome_range(p1, p2 - 1):
                    return True
                
                # If neither option makes a palindrome, then it's not possible
                return False
            
            p1 += 1
            p2 -= 1
        
        return True
