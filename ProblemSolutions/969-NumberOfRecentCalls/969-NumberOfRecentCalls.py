# Last updated: 7/14/2025, 10:21:27 AM
class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)

        i = 0
        while i < len(self.requests) and self.requests[i] < t - 3000:
            # don't care about the max range just that its okay with the min range
            # if it's not in the range we are gonna remove i elements
            i += 1

        if i != 0:
            # if different means there where some elements at the start that didn't comply so we remove them
            self.requests = self.requests[i:]

        return len(self.requests)

        #other quick solution i made but this is of course much slower as it needs to go through all elements everytime
        #counter = 0
        #self.requests.append(t)
        
        #for request in self.requests:
        #    if t - 3000 <= request <= t:
        #        counter += 1
        #return counter
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
