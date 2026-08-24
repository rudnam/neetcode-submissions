class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashArr = defaultdict(int)
        for n in nums:
            hashArr[n] += 1
        
        return sorted(hashArr.keys(), key=lambda x: hashArr[x], reverse=True)[:k]
