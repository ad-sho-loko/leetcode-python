import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        nums = sorted(nums)

        self.top = []

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.top) < self.k:
            heapq.heappush(self.top, val)
            return self.top[0]

        kth = heapq.heappop(self.top)
        if val > kth:
            heapq.heappush(self.top, val)
        else:
            heapq.heappush(self.top, kth)

        return self.top[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)