class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}
        for i in range(len(tokens)):
            if tokens[i] in operations:
                if tokens[i] == '+':
                    stack[-2] += stack[-1]
                
                elif tokens[i] == '-':
                    stack[-2] -= stack[-1]

                elif tokens[i] == '*':
                    stack[-2] *= stack[-1]
                
                elif tokens[i] == '/':
                    stack[-2] = int(stack[-2]/(stack[-1]*1.0))

                stack.pop()
            
            else:
                stack.append(int(tokens[i]))

        return stack[0]
        