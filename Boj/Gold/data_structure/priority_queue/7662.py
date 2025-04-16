import sys
import heapq
from collections import Counter

input = sys.stdin.readline


class DualPriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.count = Counter()

    def __clean_min_heap(self):
        while self.min_heap:
            value = self.min_heap[0]
            if self.count[value] > 0:
                break
            heapq.heappop(self.min_heap)

    def __clean_max_heap(self):
        while self.max_heap:
            value = -self.max_heap[0]
            if self.count[value] > 0:
                break
            heapq.heappop(self.max_heap)

    def __insert(self, value: int):
        heapq.heappush(self.min_heap, value)
        heapq.heappush(self.max_heap, -value)
        self.count[value] += 1

    def __delete(self, value):
        if not self.count:
            return

        if value == 1:
            if self.max_heap:
                self.__clean_max_heap()
                max_val = -heapq.heappop(self.max_heap)
                self.count[max_val] -= 1
                if not self.count[max_val]:
                    del self.count[max_val]

        else:
            if self.min_heap:
                self.__clean_min_heap()
                min_val = heapq.heappop(self.min_heap)
                self.count[min_val] -= 1
                if not self.count[min_val]:
                    del self.count[min_val]

    def run(self, instruction: str, value: int):
        if instruction == "I":
            self.__insert(value)
        else:
            self.__delete(value)

    def print_min_max(self):
        self.__clean_min_heap()
        self.__clean_max_heap()

        if not self.count:
            print("EMPTY")
        else:
            print(-self.max_heap[0], self.min_heap[0])


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        k = int(input())
        dpq = DualPriorityQueue()

        for _ in range(k):
            inst, val = input().split()
            val = int(val)
            dpq.run(inst, val)

        dpq.print_min_max()

# A self-implementation without built-in heapq.
# Logically solid, but takes too much time.

# import sys
# from collections import Counter
#
# input = sys.stdin.readline
#
#
# # TC = O(tlogk) = O(tlog10^6)
# # SC = O(2 * 10^6) = 2* 4bytes * 10^3 * 10^3 = 80MB
#
# class DPQ:
#     class MinHeap:
#         def __init__(self):
#             self.queue = [None]
#             self.last = 0
#
#         def top(self):
#             return self.queue[1]
#
#         def push(self, value: int):
#             self.queue.append(value)
#             self.last += 1
#             idx = self.last
#
#             # Bubble up
#             while idx > 1 and self.queue[idx] < self.queue[idx // 2]:
#                 self.queue[idx], self.queue[idx // 2] = self.queue[idx // 2], self.queue[idx]
#                 idx //= 2
#
#         def pop(self):
#             if not self.last:
#                 return
#
#             root = self.queue[1]
#             self.queue[1] = self.queue[self.last]
#             self.queue.pop()
#             self.last -= 1
#
#             # Bubble down
#             idx = 1
#             while self.last > idx:
#                 smallest = idx
#                 left = 2 * idx
#                 right = 2 * idx + 1
#
#                 if left <= self.last and self.queue[left] < self.queue[smallest]:
#                     smallest = left
#                 if right <= self.last and self.queue[right] < self.queue[smallest]:
#                     smallest = right
#
#                 if smallest == idx:
#                     break
#
#                 self.queue[idx], self.queue[smallest] = self.queue[smallest], self.queue[idx]
#                 idx = smallest
#
#             return root
#
#     class MaxHeap:
#         def __init__(self):
#             self.queue = [None]
#             self.last = 0
#
#         def top(self):
#             return self.queue[1]
#
#         def push(self, value: int):
#             self.queue.append(value)
#             self.last += 1
#             idx = self.last
#
#             # Bubble up
#             while idx > 1 and self.queue[idx] > self.queue[idx // 2]:
#                 self.queue[idx], self.queue[idx // 2] = self.queue[idx // 2], self.queue[idx]
#                 idx //= 2
#
#         def pop(self):
#             if not self.last:
#                 return
#
#             root = self.queue[1]
#             self.queue[1] = self.queue[self.last]
#             self.queue.pop()
#             self.last -= 1
#
#             # Bubble down
#             idx = 1
#             while True:
#                 largest = idx
#                 left = 2 * idx
#                 right = 2 * idx + 1
#
#                 if left <= self.last and self.queue[left] > self.queue[largest]:
#                     largest = left
#                 if right <= self.last and self.queue[right] > self.queue[largest]:
#                     largest = right
#
#                 if largest == idx:
#                     break
#
#                 self.queue[idx], self.queue[largest] = self.queue[largest], self.queue[idx]
#                 idx = largest
#
#             return root
#
#     def __init__(self):
#         self.min_heap = self.MinHeap()
#         self.max_heap = self.MaxHeap()
#         self.valid = Counter()
#
#     # synchronize two heaps nodes
#     def _clean_min(self):
#         while self.min_heap.last > 0:
#             top = self.min_heap.top()
#             if self.valid[top] > 0:
#                 break
#             self.min_heap.pop()
#
#     def _clean_max(self):
#         while self.max_heap.last > 0:
#             top = self.max_heap.top()
#             if self.valid[top] > 0:
#                 break
#             self.max_heap.pop()
#
#     def d(self, value):
#         if not self.valid:
#             return
#
#         if value == 1:
#             self._clean_max()
#             if self.max_heap.last > 0:
#                 max_val = self.max_heap.pop()
#                 self.valid[max_val] -= 1  # synchronize
#                 if not self.valid[max_val]:
#                     del self.valid[max_val]
#
#         else:
#             self._clean_min()
#             if self.min_heap.last > 0:
#                 min_val = self.min_heap.pop()
#                 self.valid[min_val] -= 1  # synchronize
#                 if not self.valid[min_val]:
#                     del self.valid[min_val]
#
#     def i(self, value: int):
#         self.min_heap.push(value)
#         self.max_heap.push(value)
#         self.valid[value] += 1  # synchronize
#
#     def run(self, instruction: str, value: int):
#         if instruction == "D":
#             self.d(value)
#         else:
#             self.i(value)
#
#     def print_min_max(self):
#         self._clean_min()
#         self._clean_max()
#
#         if not self.valid:
#             print("EMPTY")
#             return
#
#         max_val = self.max_heap.top()
#         min_val = self.min_heap.top()
#         print(max_val, min_val, sep=" ")
#
#
# if __name__ == "__main__":
#     # T test cases are given.
#     # If instruction == "I":
#     #   insert the value into a queue
#     # If instruction == "D":
#     #   if value == 1:
#     #       delete the maximum value in the queue
#     #   else:
#     #       delete the minimum value in the queue
#
#     # Constraints
#     # TIME 6000ms
#     # SPACE 256MB
#     # 1. k <= 10^6
#     # 2. -2^31 <= Qi <= (2^31)-1
#     #   which represents 4byte integer
#
#     # Approach
#     # 1. Both max, min heap queue is required.
#     # 2. Tracking the size is needed for check if it is empty.
#     # 3. if instruction == "D" and not queue.size: return
#     # 4. print(heap[1] and heap[size], sep=" ") if heap.size else "EMPTY"
#
#     t = int(input())
#     for _ in range(t):
#         Q = DPQ()
#         k = int(input())
#
#         for i in range(k):
#             instruction, value = input().split()
#             Q.run(instruction, int(value))
#
#         Q.print_min_max()
