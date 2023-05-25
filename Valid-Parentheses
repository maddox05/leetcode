class Solution: # i learned hashmaps and stacks, this one was a good one
    def isValid(self, s: str) -> bool:
        stack =[]
        #stack will be true if empty
        hashmap_closetoopen ={")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in hashmap_closetoopen:
                if stack and stack[-1] == hashmap_closetoopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
