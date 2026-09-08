class RecentCounter:

    def __init__(self):
        self.recentcounter = []

    def ping(self, t: int) -> int:
        self.recentcounter.append(t)

        while self.recentcounter[0] < t-3000:
            self.recentcounter.pop(0)

        return len(self.recentcounter)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)