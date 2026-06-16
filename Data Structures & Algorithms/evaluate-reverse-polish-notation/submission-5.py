class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            print(element)
            if element in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()
                if element == '+':
                    stack.append(left+right)
                elif element == '-':
                    stack.append(left-right)
                elif element == '*':
                    stack.append(left*right)
                else: 
                    stack.append(int(left/right))
            else:
                stack.append(int(element))
            print(stack)
        return stack.pop()