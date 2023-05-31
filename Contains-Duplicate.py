class Solution:
    def containsDuplicate(self,  nums) -> bool:
        hashset1 = set()
        for i in nums:
            if i in hashset1:
                return True
            else:
                hashset1.add(i)
        else:
            return False
