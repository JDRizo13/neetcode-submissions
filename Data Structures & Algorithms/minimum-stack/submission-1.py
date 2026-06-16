class MinStack:

    def __init__(self):
            self.stack = deque()
            self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(
                min(val, self.minStack[-1])
            )

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # minimum = inf
        # # print(self.minStack)
        # for element in self.minStack:
        #     # print(element)
        #     if element < minimum:
        #         minimum = element
        return self.minStack[-1]

        
