class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        hold = []
        for op in operations:
            if op == "C":
                # print("remove")
                stack.pop()
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)