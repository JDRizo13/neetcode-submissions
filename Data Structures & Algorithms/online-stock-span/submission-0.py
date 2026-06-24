from collections import deque

class StockSpanner:

    def __init__(self):
        self.stockStack = deque()

    def next(self, price: int) -> int:
        span = 1
        while self.stockStack and self.stockStack[-1][0] <= price:
            oldPrice, oldSpan = self.stockStack.pop()
            span += oldSpan
        self.stockStack.append((price,span))
        # print(self.stockStack)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)