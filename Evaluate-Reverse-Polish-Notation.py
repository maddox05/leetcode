

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if(tokens[i] != "+" and tokens[i] != "-" and tokens[i] != "/" and tokens[i] != "*"):
                stack.append(tokens[i])
            else:
                
                first = int(stack.pop())
                second = int(stack.pop())
                if(tokens[i] == "+"):
                    stack.append(first+second)
                elif(tokens[i] == "-"):
                    stack.append(second-first)
                elif(tokens[i] == "/"):
                    stack.append(second/first)
                elif(tokens[i] == "*"):
                    stack.append(second*first)
        return int(stack[0])
