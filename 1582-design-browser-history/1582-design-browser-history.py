class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.homepage.next = newNode
        newNode.prev = self.homepage
        self.homepage = newNode

        

    def back(self, steps: int) -> str:
        while steps > 0 and self.homepage.prev:
            self.homepage = self.homepage.prev
            steps -= 1
        return self.homepage.val
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.homepage.next:
            self.homepage = self.homepage.next
            steps -= 1
        return self.homepage.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)