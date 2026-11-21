class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        low_string = string.lower()
        rev_string = low_string[::-1]
        
        if low_string == rev_string:
            return True
        return False
        
        