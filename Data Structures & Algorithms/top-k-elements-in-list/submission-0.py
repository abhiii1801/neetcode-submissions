class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1

        for v,f in hmap.items():
            heapq.heappush(heap, (f,v))
            if len(heap) > k:
                heapq.heappop(heap)

        return [h[1] for h in heap]


