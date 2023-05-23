from MaxHeapTree import *

def heapSort(data):
    heap = MaxHeap()

    for n in data:
        heap.insert(n)

    for i in range(1, len(data)+1):
        data[-i] = heap.delete()

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
heapSort(data)
print(data)
