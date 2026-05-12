import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # use ord() -> returns ASCII code
        # convert all string to lowercase
        # 0 -> 48 ... 9 -> 57
        # a -> 97 ... z -> 122
        # rebuild string
        # compare the new string and its reverse 

        st = s.lower()
        new_st = ""

        for c in st:
            if ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
                new_st += c
        if new_st == new_st[::-1]:
            return True
        return False
                
        
