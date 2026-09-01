class MedianFinder:

    def __init__(self):
        # small = max heap (left side of the data structure / array )
        self.small = [] 
        # large = min heap (right side of the data structure / array)
        self.large = [] 


    def addNum(self, num: int) -> None:
        
        if self.large and num > self.large[0] : 
            heapq.heappush(self.large, num)
        else : 
            heapq.heappush(self.small, -1 * num)

        
        if len(self.large) > len(self.small) + 1 : 
            elem = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * elem)
        
        if len(self.small) > len(self.large) + 1 : 
            elem = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, elem)
        

    def findMedian(self) -> float:
        
        if len(self.large) > len(self.small) : 
            return self.large[0]
        elif len(self.small) > len(self.large) : 
            return -1 * self.small[0]
        else : 
            number = ((-1 * self.small[0]) + self.large[0]) / 2 
            return number 