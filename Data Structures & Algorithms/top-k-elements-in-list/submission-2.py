class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        res = []

        for n in count:
            heapq.heappush_max(heap, (count[n], n))

        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        
        return res