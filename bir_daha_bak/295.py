import heapq


class MedianFinder:

    def __init__(self):
        self.smaller = [] # max_heap
        # larger number with equal numbers or 1 more numbers
        self.larger = [] # min_heap
        
    
    def addNum(self, num):
        if len(self.smaller) == len(self.larger):
            heapq.heappush(self.larger, -heapq.heappushpop(self.smaller, -num))
        else:
            heapq.heappush(self.smaller, -heapq.heappushpop(self.larger, num))

    def findMedian(self):
        # if equal, then pick both 
        # if one more items in larger, pick it from larger
        if len(self.larger) == len(self.smaller):
            return (self.larger[0] - self.smaller[0]) / 2
        else:
            return self.larger[0]



class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)
        
        if self.smallHeap and self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            value = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, value)
        
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            value = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, value)
        
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            value = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -value)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        return (-self.smallHeap[0] + self.largeHeap[0]) / 2 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()