class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashy_boi = {} # creates blank array
        bool_return = True # create what to return
        if s.__len__() != t.__len__(): #checks at start if not equal than quit
            return False
        for i in s: # loads hashmap
            if i not in hashy_boi: # if key not in hashmap than add the key and set it to one
                hashy_boi[i] = 1 # how many times letter has shown up
            else:
                hashy_boi[i] = hashy_boi[i]+1 # if already in there than add one to how many times the letter shows up
        for x in t: # go through t
            if x in hashy_boi: #if char in t in hashy boi
              hashy_boi[x] = hashy_boi[x]-1 # go to key and remove one as it has same letter
        for y in hashy_boi: # checks if all values are 0 since if they all have same amt of letters it should be full of 0s
            if hashy_boi[y] == 0:
                bool_return = True
            else:
                return False
        return bool_return
