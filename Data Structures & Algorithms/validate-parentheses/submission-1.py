class Solution:
    def isValid(self, s: str) -> bool:
        # if s.count("(") == s.count(")") and s.count("[") == s.count("]") and s.count("{") == s.count("}"):
        #     return True
        # else:
        #     return False



            ### use stack for this one 
            # push new bracket if its equal to prev bracket pop both then move to next 

        has = {")": "(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if stack and stack[-1] == has[i]:
                    stack.pop()
                else:
                    return False
        return stack == []

       
        