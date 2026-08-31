class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        freq = [0] * (len(nums)+1)
        # print(hashmap)
        for el in hashmap:
            idx = hashmap[el]
            if freq[idx] == 0:
                freq[idx] = [el]
            else:
                freq[idx].append(el)
        # print(freq)
        res = []
        count= 0
        for i in range(len(freq)-1, 0, -1):
            # this freqeuncy has no elements
            if freq[i] == 0:
                continue
            else:
                idx = 0
                while(idx < len(freq[i]) and count < k):
                    res.append(freq[i][idx])
                    idx += 1
                    count += 1
                if count == k:
                    return res
        # numsFreq = []
        # for i, (key, value) in enumerate(hashmap.items()):
        #     numsFreq.append((key, value))
        # numsFreq.sort(key = lambda x:x[1], reverse = True)
        # res = []
        # for i in range(k):
        #     res.append(numsFreq[i][0])
        # return res