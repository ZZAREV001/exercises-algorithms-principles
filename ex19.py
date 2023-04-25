# Top K frequent elements solved with heap data structure:
import heapq
import collections     # for using the Python default dictionary

class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.defaultdict(int)       # defaultdict() initializes the value to 0 in the loop and encodes it.
        for n in nums:
            count[n] += 1

        heap = []                           # initialize the elements in the heap and append it to the heap.
        for num, c in count.items():
            heap.append((-c, num))          # Python sorts the heap using the value of the first item, so for (-c, num) it sorts using the value '-c'.
        heapq.heapify(heap)
        print(heap)

        # Pop the heap k times and returns the result in an array:
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


print(Solution().topKFrequent([1, 1, 2, 2, 3], 2))    # we want to top K = 2 elements
# expected answer is [1, 2]