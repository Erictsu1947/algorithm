
def heapify():
    pass


class Heap(object):
    def __init__(self, n):
        self.size = n
        self._items = []

    def is_empty(self):
        pass

    @property
    def count(self):
        return len(self._items)

    def _parent(self, j):
        return int(j/2)

    def insert(self, item):
        length = self.count
        if length > self.size:
            raise Exception("great than size")

        self._items.append(item)
        idx = self.count
        while idx > 0:
            parent_idx = self._parent(idx)
            parent = self._items[parent_idx-1]
            print(idx, parent_idx, parent, item)
            if parent_idx > 0 and parent < item:
                self._items[parent_idx-1], self._items[idx-1] = self._items[idx-1], self._items[parent_idx-1]
                idx = parent_idx
            else:
                break
        print(self._items)

    def delete_top(self):
        pass

    def _sift_up(self):
        pass

    def _sift_down(self):
        pass

    @property
    def items(self):
        return self._items

    def check(self):
        for i in range(1, self.count):
            idx = i + 1
            parent_idx = self._parent(idx)
            print(idx, parent_idx)
            assert self._items[parent_idx-1] > self._items[idx-1]
            # assert self._items[idx - 1] > self._items[2*idx]
            # assert self._items[idx - 1] > self._items[2 * idx+1]


def max_heapify(heap, heapSize, root):
    left = 2 * root + 1
    right = 2 * root + 2

    max_node = root

    if left < heapSize and heap[left] > heap[max_node]:
        max_node = left
    if right < heapSize and heap[right] > heap[max_node]:
        max_node = right
    if max_node != root:
        heap[max_node], heap[root] = heap[root], heap[max_node]
        max_heapify(heap, heapSize, max_node)


def build_max_heap(unsorted):
    n = len(unsorted)

    for i in range((n-2)//2, -1, -1):
        max_heapify(unsorted, n, i)


def heap_sort(unsorted):

    build_max_heap(unsorted)

    n = len(unsorted)
    sorted_list = []
    for i in range(n - 1, -1, -1):
        unsorted[0], unsorted[-1] = unsorted[-1], unsorted[0]
        sorted_list.append(unsorted.pop(-1))
        max_heapify(unsorted, len(unsorted), 0)
    return sorted_list


array = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

res = heap_sort(array)
print(res)
