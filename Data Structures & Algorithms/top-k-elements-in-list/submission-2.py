import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        heap = []

        for (key,value) in counts.items() :
            heapq.heappush(heap,(value,key))
            
            if (len(heap)>k) :
                heapq.heappop(heap)
            
        return [num for freq,num in heap]

        
        