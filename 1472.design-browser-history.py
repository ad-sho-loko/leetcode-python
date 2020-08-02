class BrowserHistory:
    homepage = ""
    histories = []
    back_histories = []

    def __init__(self, homepage: str):
        self.histories = []
        self.back_histories = []
        self.homepage = homepage

    def visit(self, url: str) -> None:
        self.histories.append(url)
        self.back_histories = []

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.histories) == 0:
                break
            self.back_histories.append(self.histories.pop())

        if len(self.histories) == 0:
            return self.homepage
        return self.histories[-1]

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.back_histories) == 0:
                break
            self.histories.append(self.back_histories.pop())

        if len(self.histories) == 0:
            return self.homepage
        return self.histories[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
