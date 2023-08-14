class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if s.__len__() != t.__len__(): #if they are not same length then just quit
            return False

        chars_in_word = list(s) # convert s to list so I can edit it
        for j in t: # go through t
            if j in chars_in_word: # if value in t == any value in s than remove a value from s
                chars_in_word.remove(j)

        if chars_in_word.__len__() != 0: # s should be blank if true
            return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.isAnagram("rat", "car"))
