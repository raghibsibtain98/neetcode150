class Solution:
    def isOpening(self,char):
        if (char=='(' or char=='{' or char=='[') :
            return True;
        return False


    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (self.isOpening(char)):
                stack.append(char)
            else :
                if (stack and ((char == ')' and stack[-1] == '(')
                    or (char == '}' and stack[-1] == '{')
                    or (char == ']' and stack[-1] == '['))):
                    stack.pop()
                else :
                    return False
        if not stack :
            return True
        return False



        