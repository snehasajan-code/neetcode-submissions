class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        numsFreq = []
        for i, (key, value) in enumerate(hashmap.items()):
            numsFreq.append((key, value))
        numsFreq.sort(key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(numsFreq[i][0])
        return res