class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_of_digits_normal = []
        list_of_digits_backwards = []
        for i in str(x):
            list_of_digits_normal.append(i)
        for j in range(len(list_of_digits_normal), 0, -1): #123
            list_of_digits_backwards.append(list_of_digits_normal[j-1]) #012 why do these things have to start and 0 or 1 just start them the same
        if list_of_digits_normal == list_of_digits_backwards:
            return True
        else:
            return False
