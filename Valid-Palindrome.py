class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = "" #init new string shouldnt have to but I suck
        for i in range(0, s.__len__()): #goes through s
            if s[i].isalnum(): # checks if its valid thing in palindrome
                new_string+=s[i].lower() #if its valid add it





        for n, i in enumerate(new_string): # go through valid string
            if new_string[n] != new_string[new_string.__len__()-n-1]: # make sure every value same forward and backwards
                return False
        return True
