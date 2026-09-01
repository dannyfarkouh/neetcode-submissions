class MedianFinder:

    def __init__(self):
        # Two heaps
        # Small = maxHeap, since it is on the left side 
        # Large = minHeap, since it is on the right side 
        self.small, self.large = [], [] 

    def addNum(self, num: int) -> None:
        # Python only has min heaps, so we -1 * num when adding to small heap, which is a maxHeap 
        if self.large and num > self.large[0] : 
            heapq.heappush(self.large, num)
        else : 
            heapq.heappush(self.small, -1 * num)


        # If the lengths of the heaps are unbalanced, we balance 
        if len(self.large) > len(self.small) + 1 : 
            min_num = heapq.heappop(self.large) 
            heapq.heappush(self.small, -1 * min_num)
        
        if len(self.small) > len(self.large) + 1 : 
            max_num = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, max_num)

    def findMedian(self) -> float:

        if len(self.large) > len(self.small) : 
            return self.large[0]
        
        if len(self.small) > len(self.large) : 
            return (-1 * self.small[0])
        
        return ( (-1 * self.small[0]) + self.large[0] ) / 2.0 