def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    origin = [0, 0]
    points.sort(key=lambda x: (x[0] - origin[0]) ** 2 + (x[1] - origin[1]) ** 2)
    return points[:k]

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    points.sort(key=lambda c: c[0]**2 + c[1]**2)
    return points[:k]

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points, k))

import heapq

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    minHeap = []
    
    for x,y in points:
        distanceToOrigin = x**2 + y**2
        minHeap.append([distanceToOrigin, x,y])
    
    heapq.heapify(minHeap)
    
    result = []
    while k > 0:
        distance, x, y= heapq.heappop(minHeap)
        result.append([x,y])
        k -= 1

    return result

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points, k))


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    for i, point in enumerate(points):
                point.insert(0, point[0] ** 2 + point[1] ** 2)
            
            heapify(points)
            lowest_k = []        
            for i in range(k):
                dist_squared, x, y = heappop(points)
                lowest_k.append([x, y])

            return lowest_k 


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        # O(k*logn) time complexity

        heap = []
        ans = []

        for x, y in points:
            # calculate distance to 0,0 using the Euclidean distance
            # no need to sqrt since we're not looking for actual distance
            distance = (x**2) + (y**2)
            heap.append([distance, x, y])
        
        # O(n)
        heapq.heapify(heap)
        
        # now the closest element (with smallest distance) is at [0]
        for i in range(k):
            # O(logn) (for every k)
            distance, x, y = heapq.heappop(heap)
            ans.append([x, y])
        
        return ans