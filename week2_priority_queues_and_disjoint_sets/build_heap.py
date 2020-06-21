# python3

class HeapBuilder:
    def __init__(self,data):
        self.heap = data
        self.swap = []
        
    def getSize(self):
        return len(self.heap)

    def printSwaps(self):
        print(len(self.swap))
        for i, j in self.swap:
            print(i, j)

    def getLeftChildIdx(self, i):
        LChild = 2 * i + 1
        if LChild >= self.getSize():
            return False
        return LChild

    def getRightChildIdx(self, i):
        RChild = 2 * i + 2
        if RChild >= self.getSize():
            return False
        return RChild

    def builtHeap(self):
        n = len(self.heap)
        for i in range(n//2,-1,-1):
            self.siftDown(i)

    def siftDown(self,i):
        l = self.getLeftChildIdx(i)
        r = self.getRightChildIdx(i)
        
        minIdx = i
        if l and self.heap[l] < self.heap[minIdx]:
            minIdx = l
        if r and self.heap[r] < self.heap[minIdx]:
            minIdx = r
        if minIdx != i:
            self.swap.append((i,minIdx))
            self.heap[minIdx], self.heap[i] = self.heap[i] , self.heap[minIdx]
            self.siftDown(minIdx)

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    heapBuilder = HeapBuilder(data)
    heapBuilder.builtHeap()
    heapBuilder.printSwaps()


