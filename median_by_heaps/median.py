import math


class Heap:
    def __init__(self):
        self.heap_size = 0
        self.arr = []

    def add_element(self, element):
        self.arr.insert(0, element)
        self.heap_size += 1
        self.heapify(0)

    def del_element(self, ind):
        del self.arr[ind]
        self.heap_size -= 1
        self.heapify(ind)

    def parent(self, ind):
        return math.floor((ind - 1) / 2)

    def left(self, ind):
        l_ind = 2 * ind + 1
        if l_ind <= self.heap_size:
            return l_ind
        else:
            return ind

    def right(self, ind):
        l_ind = 2 * ind
        if l_ind <= self.heap_size:
            return 2 * ind + 2
        else:
            return ind

    def heap_peak(self):
        return self.arr[0]

    def compare(self, comp_els):
        """
        Compare three elements in comp_els according to specific implementation in inheriter's method.
        :param comp_els: List of tuples (index, value) of three elements.
        :return: Index of the element which has to hold the highest position.
        """
        pass

    def pop_peak(self):
        if self.heap_size < 1:
            return None
        peak_el = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.heap_size -= 1
        self.heapify(0)
        return peak_el

    def build(self, input_arr):
        self.arr = input_arr
        self.heap_size += len(input_arr)

    def heapify(self, ind):
        r_succ = self.right(ind)
        l_succ = self.left(ind)
        comp_els = [(ind, self.arr[ind])]
        if (r_succ < self.heap_size):
            comp_els.append((r_succ, self.arr[r_succ]))
        if (l_succ < self.heap_size):
            comp_els.append((l_succ, self.arr[l_succ]))
        higher = self.compare(comp_els)
        if higher != ind:
            self.arr[higher], self.arr[ind] = self.arr[ind], self.arr[higher]
            self.heapify(higher)


class MaxHeap(Heap):
    def compare(self, comp_els):
        """ Compare to get the gratest of three elements."""
        return max(comp_els, key=lambda x: x[1])[0]


class MinHeap(Heap):
    def compare(self, comp_els):
        """ Compare to get the least of three elements."""
        return min(comp_els, key= lambda x: x[1])[0]


class Median:
    def __init__(self):
        self.lower_heap = MaxHeap()
        self.upper_heap = MinHeap()

    def _move_element(self, source_heap, recieve_heap):
        mov_peak_el = source_heap.pop_peak()
        recieve_heap.add_element(mov_peak_el)
        # source_heap.del_element(0)

    def add_element(self, element):
        if not self.lower_heap.arr:
            self.lower_heap.add_element(element)
        elif element < self.lower_heap.heap_peak():
            self.lower_heap.add_element(element)
        else:
            self.upper_heap.add_element(element)
        # Even the number of elements.
        size_difference = (self.lower_heap.heap_size - self.upper_heap.heap_size)
        if size_difference > 1:
            self._move_element(self.lower_heap, self.upper_heap)
        elif size_difference < -1:
            self._move_element(self.upper_heap, self.lower_heap)

    def get_median(self):
        if self.lower_heap.heap_size == self.upper_heap.heap_size:           # heaps contain equal number of elements
            med_1, med_2 = self.lower_heap.heap_peak(), self.upper_heap.heap_peak()
            return med_1 if med_1 == med_2 else (med_1, med_2)
        else:                                                              # return peak of bigger heap
            big_heap = max([self.upper_heap, self.lower_heap], key=lambda x: x.heap_size)
            med = big_heap.heap_peak()
            return med


    def get_maxheap_elements(self):
        return self.lower_heap.arr

    def get_minheap_elements(self):
        return  self.upper_heap.arr




if __name__ == "__main__":

    # Basic test.
    m = Median()
    for i in range(1, 101):
        m.add_element(i)
        print(m.get_median())
    # for i in range(m.lower_heap.heap_size):
        # print(m.lower_heap.arr[i], i, ':', m.lower_heap.parent(i), m.lower_heap.left(i), m.lower_heap.right(i))
    print(m.lower_heap.arr)
    print("\nMedian result:", m.get_median())


