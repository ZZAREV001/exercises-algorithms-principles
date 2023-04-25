# Closest points to the origin
# Brute force approach. O(n.log(n)) time with n number of points
import heapq


def calculateDistance(p):
    return p[0] * p[0] + p[1] * p[1]

def findClosestPoints(points, k):
    points = sorted(points, key = lambda x: calculateDistance(x))
    return points[:k]

# Heap data structure approach. For the comparator function, we will need a tuple (Python).
# running in O(k.log(n)). Space complexity is linear because we store in the heap n points.
def findClosestPoints2(points, k):
    data = []
    for p in points:
        data.append((calculateDistance(p), p))
    heapq.heapify(data)

    result = []
    for i in range(k):
        result.append(heapq.heappop(data)[1])
    return result


print(findClosestPoints([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
print(findClosestPoints2([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))