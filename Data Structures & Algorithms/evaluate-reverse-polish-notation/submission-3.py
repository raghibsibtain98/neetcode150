class Solution:

    def isOperator(self, char):
        if char == '+' or char =='-' or char == '*' or char=='/' :
            return True
        return False


    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens :
            if (not self.isOperator(token)):
                stack.append(int(token))
            else :
                a = int(stack.pop()) if stack else 0
                b = int(stack.pop()) if stack else 0
                if token == '+':
                    stack.append(b+a)
                elif token == '-':
                    stack.append(b-a)
                elif token == '*':
                    stack.append(b*a)
                elif token == '/':
                    if a==0:
                        stack.append(0)
                    else:
                        stack.append(int(b/a))

        return stack[-1]
