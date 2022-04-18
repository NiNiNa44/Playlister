class Min_Heap:

    def __init__(self, cap):
        self.cap = cap
        self.size = 0
        self.Heap = [0]*(self.cap + 1)
        self.Heap[0] = 100
        self.FRONT = 1
        self.index = list(range(0, cap + 1))

    # find parent from the position of the children
    def parent(self, pos):
        return pos//2

    # find position of the left child given the parent's position
    def leftChild(self, pos):
        return pos * 2

     # find position of the right child given the parent's position
    def rightChild(self, pos):
        return (pos * 2) + 1

    # Determine if the node at the position is a leaf node
    def is_leaf(self, pos):
        return (pos * 2) > self.size

    # Swap node
    def swap(self, fpos, spos):
        tmp1 = self.Heap[fpos]
        tmp2 = self.index[fpos]
        self.Heap[fpos] = self.Heap[spos]
        self.index[fpos] = self.index[spos]
        self.Heap[spos] = tmp1
        self.index[spos] = tmp2

    def heapify(self, pos):

        if not self.is_leaf(pos):
            # check if a parent contains higher values than its children
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # Left swap case
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))
                # Right swap case
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.heapify(self.rightChild(pos))

    # Insert function
    def insert(self, node):
        if self.size >= self.cap:
            return
        self.size = self.size + 1
        self.Heap[self.size] = node

        curr = self.size
        while self.Heap[curr] < self.Heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

    def print(self):
        for i in range(1, (self.size//2)+1):
            print(" parent : " + str(self.Heap[i])+" left baby => " +
                  str(self.Heap[2 * i])+" right baby => : " +
                  str(self.Heap[2 * i + 1]))

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):

        for pos in range(self.size//2, 0, -1):
            self.heapify(pos)

    # pop min index
    def pop(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.index[self.FRONT] = self.index[self.size]
        self.size = self.size - 1
        self.heapify(self.FRONT)
        return popped, self.index[self.FRONT]
